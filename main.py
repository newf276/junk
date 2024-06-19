import requests

country = "epg"
xml = f"https://i.mjh.nz/Roku/{country}.xml"
output_xml = "programme/rtv.xml"
    
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
xml = f"https://github.com/matthuisman/i.mjh.nz/raw/master/PlutoTV/{country}.xml"
output_xml = "programme/ptv.xml"

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



