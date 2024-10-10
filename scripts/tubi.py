import requests
m3u = f"https://github.com/dtankdempse/tubi-m3u/raw/refs/heads/main/tubi_playlist_us.m3u"
xml = f"https://github.com/dtankdempse/tubi-m3u/raw/refs/heads/main/tubi_epg_us.xml"
output_m3u = "tubi.m3u"
output_xml = "tubi.xml"
try:
    response = requests.get(m3u)
    if response.status_code == 200:
        print("GET request successful.")

        with open(output_m3u, "w") as f:
            f.write(response.text)
            print(f"Response saved to {output_m3u}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    response = requests.get(xml)
    if response.status_code == 200:
        print("GET request successful.")

        with open(output_xml, "w") as f:
            f.write(response.text)
            print(f"Response saved to {output_xml}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Error making GET request:", e)
