import requests

country = "epg"
xml = f"https://i.mjh.nz/Roku/{country}.xml"
output_xml = "rtv.xml"
    
try:
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
    

country = "all"
xml = f"https://i.mjh.nz/PlutoTV/{country}.xml"
output_xml = "ptv.xml"

try:
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

    
xml = f"https://tinyurl.com/newf276"
output_xml = "newf.xml"

try:
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

    
xml = f"https://xmltv.tvkaista.net/guides/ontvtonight.com_us.xml"
output_xml = "ontvtonight_us.xml"

try:
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

    
xml = f"https://xmltv.tvkaista.net/guides/sky.com.xml"
output_xml = "sky.xml"

try:
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

    
xml = f"https://raw.githubusercontent.com/AqFad2811/epg/main/epg.xml"
output_xml = "aqfad.xml"

try:
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
    

xml = f"https://raw.githubusercontent.com/dp247/Freeview-EPG/master/epg.xml"
output_xml = "freeview.xml"

try:
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
    
    

        
        