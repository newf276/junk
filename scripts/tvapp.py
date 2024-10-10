import requests
m3u = f"https://tinyurl.com/multiservice21?region=all&include=SamsungTVPlus-USBC39000171G,SamsungTVPlus-US4000033L,SamsungTVPlus-USAJ3400011A8,SamsungTVPlus-CA15000018F,SamsungTVPlus-CABC2300009KD,SamsungTVPlus-USBA370000104,SamsungTVPlus-GBBD8000016N,SamsungTVPlus-CA1400004AE,SamsungTVPlus-GBAJ4900020VP,SamsungTVPlus-USBD700003L7,SamsungTVPlus-GBBD1100002L5,SamsungTVPlus-GBBB1600008R3,SamsungTVPlus-USBA300024TN,SamsungTVPlus-CAAJ2700011IF,SamsungTVPlus-USBA300028QU,SamsungTVPlus-USBD3000073N,SamsungTVPlus-USBB52000022Q,SamsungTVPlus-GBAJ2400003DD,SamsungTVPlus-CABC23000223U,SamsungTVPlus-USAJ4300005PJ,SamsungTVPlus-GBBC900015D3,SamsungTVPlus-CABA3700001DB,SamsungTVPlus-USBD25000138Y,SamsungTVPlus-CABD1200010LE,SamsungTVPlus-CABD1200012B8,SamsungTVPlus-CABC5200006AL,SamsungTVPlus-CABD1200043OK,SamsungTVPlus-USBA3800005NI,SamsungTVPlus-CABC5200020WJ,SamsungTVPlus-CA14000028T,SamsungTVPlus-CA14000105P,SamsungTVPlus-CA1400005SO,SamsungTVPlus-CA1400009E5,SamsungTVPlus-CAAJ3400016J9,SamsungTVPlus-USBD700016JY,SamsungTVPlus-USBC6000225M,SamsungTVPlus-CAAJ2700029OC,SamsungTVPlus-CA900008L6,SamsungTVPlus-CAAJ2700027GW,SamsungTVPlus-CABB2500021YQ,SamsungTVPlus-GBBA2200005ZA,SamsungTVPlus-USBC21000142T,SamsungTVPlus-USAJ3000006X5,SamsungTVPlus-CABC5200022N1,SamsungTVPlus-USAJ2200009C2,SamsungTVPlus-GBBA220000751,SamsungTVPlus-USBD300002TU,SamsungTVPlus-USBC24000223S,SamsungTVPlus-CABC2300001X9,SamsungTVPlus-CABB26000192D,SamsungTVPlus-USBA3400003IP,SamsungTVPlus-GBBD500001F5,SamsungTVPlus-CAAJ3400017AE,SamsungTVPlus-CAAJ34000089L,SamsungTVPlus-CAAJ270002855,SamsungTVPlus-GBBB1000005IO,SamsungTVPlus-USBA3000043LH,SamsungTVPlus-GBBD3100006XM,SamsungTVPlus-CABC2300021DQ,SamsungTVPlus-CABD1200002T9,SamsungTVPlus-CABC5200002OG,SamsungTVPlus-USBB3500002FL,SamsungTVPlus-USBA300019WF,SamsungTVPlus-GBBC300003UQ,SamsungTVPlus-GBBC900004G9,SamsungTVPlus-GBBB5000002PL,SamsungTVPlus-GBBC4300002RW,SamsungTVPlus-CABC2300002VB,SamsungTVPlus-USAK3508706A,SamsungTVPlus-CABB19000010Y,SamsungTVPlus-CABD1200001SY,SamsungTVPlus-USBD270001633,SamsungTVPlus-GB12000052F,SamsungTVPlus-US18000163F,SamsungTVPlus-USBB5200019FO,SamsungTVPlus-GBBB3800003JH,SamsungTVPlus-USBD17000117B,SamsungTVPlus-USBC3900018K6,SamsungTVPlus-USAJ26000054W,SamsungTVPlus-USBA300017PK,SamsungTVPlus-GBAJ4900006TU,SamsungTVPlus-GBAJ4900007I2,SamsungTVPlus-GBAJ49000081B,SamsungTVPlus-GBBA3300020DM,SamsungTVPlus-GB19000017P,SamsungTVPlus-GBBC90001660,SamsungTVPlus-GBAJ400042T1,SamsungTVPlus-CABD1200036YT,SamsungTVPlus-CABD1200037BS,SamsungTVPlus-CABD1200025IX,SamsungTVPlus-CABC52000165E,SamsungTVPlus-CABC52000180Z,SamsungTVPlus-CABB2600017ZU,SamsungTVPlus-CABB2600018T4,SamsungTVPlus-CABD1200023UJ,SamsungTVPlus-CABD120001993,SamsungTVPlus-CABD1200038NZ,SamsungTVPlus-CABD1200039HG&service=SamsungTVPlus&sort=name"
xml = f"https://github.com/matthuisman/i.mjh.nz/raw/master/SamsungTVPlus/all.xml"
output_m3u = "samsung.m3u"
output_xml = "samsung.xml"
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
