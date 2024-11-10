import asyncio
import requests
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json
import re
import xml.etree.ElementTree as ET
import os
from urllib.parse import unquote
from datetime import datetime

async def fetch_channel_list(playwright):
    browser_args = ["--no-sandbox"]
    browser = await playwright.firefox.launch(headless=True, args=browser_args)
    page = await browser.new_page()

    try:
        # Step 1: Visit the main page to collect necessary headers/cookies
        main_url = "https://tubitv.com/"
        print(f"Visiting {main_url} to collect headers/cookies...")
        await page.goto(main_url, timeout=60000)
        await page.wait_for_timeout(5000)

        # Step 2: Navigate to the live page
        live_url = "https://tubitv.com/live"
        print(f"Visiting {live_url} to fetch channel data...")
        await page.goto(live_url, timeout=60000)
        await page.wait_for_timeout(5000)

        html_content = await page.content()
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all <script> tags and look for the one containing window.__data
        script_tags = soup.find_all("script")
        target_script = None
        for script in script_tags:
            if script.string and script.string.strip().startswith("window.__data"):
                target_script = script.string
                break

        if not target_script:
            print("Error: Could not locate the JSON-like data in the page.")
            await browser.close()
            return None

        start_index = target_script.find("{")
        end_index = target_script.rfind("}") + 1
        json_string = target_script[start_index:end_index]

        json_string = json_string.encode('utf-8', errors='replace').decode('utf-8')
        json_string = json_string.replace('undefined', 'null')
        json_string = re.sub(r'new Date\("([^"]*)"\)', r'"\1"', json_string)

        print(f"Extracted JSON-like data (first 500 chars): {json_string[:500]}...")
        data = json.loads(json_string)
        print(f"Successfully decoded JSON data!")
        await browser.close()
        return data
    except Exception as e:
        print(f"Error fetching data using Playwright: {e}")
        await browser.close()
        return None

def create_group_mapping(json_data):
    group_mapping = {}
    content_ids_by_container = json_data.get('epg', {}).get('contentIdsByContainer', {})
    for container_list in content_ids_by_container.values():
        for category in container_list:
            group_name = category.get('name', 'Other')
            for content_id in category.get('contents', []):
                group_mapping[str(content_id)] = group_name
    return group_mapping

def fetch_epg_data(channel_list):
    epg_data = []
    group_size = 150
    grouped_ids = [channel_list[i:i + group_size] for i in range(0, len(channel_list), group_size)]

    for group in grouped_ids:
        url = "https://tubitv.com/oz/epg/programming"
        params = {"content_id": ','.join(map(str, group))}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Failed to fetch EPG data for group {group}. Status code: {response.status_code}")
            continue

        try:
            epg_json = response.json()
            epg_data.extend(epg_json.get('rows', []))
        except json.JSONDecodeError as e:
            print(f"Error decoding EPG JSON: {e}")

    return epg_data

def create_m3u_playlist(epg_data, group_mapping, country):
    sorted_epg_data = sorted(epg_data, key=lambda x: x.get('title', '').lower())
    playlist = f"#EXTM3U url-tvg=\"https://github.com/newf276/junk/raw/master/programme/tub.xml\"\n"
    seen_urls = set()

    for elem in sorted_epg_data:
        channel_name = elem.get('title', 'Unknown Channel')
        stream_url = unquote(elem['video_resources'][0]['manifest']['url']) if elem.get('video_resources') else ''
        #print(stream_url)
        stream_url = clean_stream_url(stream_url)
        #print(stream_url)
        tvg_id = str(elem.get('content_id', ''))
        logo_url = elem.get('images', {}).get('thumbnail', [None])[0]
        group_title = group_mapping.get(tvg_id, 'Other')

        if stream_url and stream_url not in seen_urls:
            playlist += f'#EXTINF:-1 tvg-name="{channel_name}" tvg-id="{tvg_id}" tvg-logo="{logo_url}" group-title="{group_title}",{channel_name}\n{stream_url}\n'
            seen_urls.add(stream_url)

    return playlist

def save_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File saved: {filename}")

def save_epg_to_file(tree, filename):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, filename)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"EPG XML file saved: {file_path}")

def create_epg_xml(epg_data):
    root = ET.Element("tv")

    for station in epg_data:
        channel = ET.SubElement(root, "channel", id=str(station.get("content_id")))
        display_name = ET.SubElement(channel, "display-name")
        display_name.text = station.get("title", "Unknown Title")

        icon = ET.SubElement(channel, "icon", src=station.get("images", {}).get("thumbnail", [None])[0])

        for program in station.get('programs', []):
            programme = ET.SubElement(root, "programme", channel=str(station.get("content_id")))

            # Convert start and stop times to XMLTV format
            start_time = convert_to_xmltv_format(program.get("start_time", ""))
            stop_time = convert_to_xmltv_format(program.get("end_time", ""))

            programme.set("start", start_time)
            programme.set("stop", stop_time)

            title = ET.SubElement(programme, "title")
            title.text = program.get("title", "")

            if program.get("description"):
                desc = ET.SubElement(programme, "desc")
                desc.text = program.get("description", "")

    tree = ET.ElementTree(root)
    return tree

def convert_to_xmltv_format(iso_time):
    try:
        dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
        xmltv_time = dt.strftime("%Y%m%d%H%M%S +0000")
        return xmltv_time
    except ValueError:
        return iso_time

def process_and_save_data(json_data):
    if json_data:
        print("Processing channel list...")
        channel_list = []
        content_ids_by_container = json_data.get('epg', {}).get('contentIdsByContainer', {})

        for container_list in content_ids_by_container.values():
            for category in container_list:
                channel_list.extend(category.get('contents', []))

        group_mapping = create_group_mapping(json_data)
        epg_data = fetch_epg_data(channel_list)

        if epg_data:
            m3u_playlist = create_m3u_playlist(epg_data, group_mapping, "us")
            epg_tree = create_epg_xml(epg_data)
            save_file(m3u_playlist, "tub.m3u")
            save_epg_to_file(epg_tree, "tub.xml")
        else:
            print("No EPG data found.")
    else:
        print("No JSON data to process.")

def clean_stream_url(url):
    clean_url = re.sub(r'(\.m3u8).*', r'\1', url)
    return clean_url

async def main():
    async with async_playwright() as playwright:
        print("Fetching channel list...")
        json_data = await fetch_channel_list(playwright)

        if json_data:
            process_and_save_data(json_data)

if __name__ == "__main__":
    asyncio.run(main())
