import requests
import zipfile

xml = f"https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz"
output_xml = "epg_ripper_CA1.xml.gz"

    with zipfile.ZipFile('epg_ripper_CA1.xml.gz.zip', 'r') as zip_ref:
        zip_ref.extractall()


if __name__ == '__master__':
    master()