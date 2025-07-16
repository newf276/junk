import requests
import re
from datetime import datetime

UPSTREAM_URL = "https://pigzillaaa-scraper.vercel.app/tims"
EPG_URL = "https://tinyurl.com/merged2423-epg"
OUTPUT_FILE = "Tims247.m3u8"
FORCED_GROUP = "Tims247"

def force_group_title(line):
    if line.startswith("#EXTINF"):
        if 'group-title="' in line:
            return re.sub(r'group-title="[^"]*"', f'group-title="{FORCED_GROUP}"', line)
        else:
            return line.replace('#EXTINF:', f'#EXTINF:-1 group-title="{FORCED_GROUP}" ', 1)
    return line

def main():
    res = requests.get(UPSTREAM_URL, timeout=15)
    res.raise_for_status()
    lines = res.text.strip().splitlines()

    output_lines = [
        f'#EXTM3U url-tvg="{EPG_URL}"',
        f'# Last forced update: {datetime.utcnow().isoformat()}Z'
    ]

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#EXTM3U"):
            continue  # skip upstream playlist header lines
        output_lines.append(force_group_title(line))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")

    print(f"[✅] Playlist saved to {OUTPUT_FILE} with group '{FORCED_GROUP}'.")

if __name__ == "__main__":
    main()
