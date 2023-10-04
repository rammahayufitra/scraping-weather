from requests_html import HTMLSession 

s = HTMLSession() 


def weather(query):
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'})
    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text 
    description = r.html.find('span#wob_dc', first=True).text
    date = r.html.find('div#wob_dts', first=True).text
    Precipitation = r.html.find("span#wob_pp", first=True).text
    Wind = r.html.find("span#wob_ws", first=True).text
    Humadity = r.html.find("span#wob_hm", first=True).text

    print(" Daerah :", query,"\n",
        f'Temperatur Saat ini : {temp+unit}' ,"\n",
        "Deskripsi :", description,"\n",
        "Laju Angin :", Wind,"\n",
        "Precipitation :", Precipitation, "\n",
        "Kelembapan :", Humadity,"\n")

    print("Next Days Prediction :")

    for angka in range(len(r.html.find("div.wob_df"))):
        days = r.html.find(f'div.wob_df[data-wob-di="{angka}"] div.Z1VzSb', first=True).text
        print(f'=============================  {days}  ==================================')
        max_temp = r.html.find(f'div.wob_df[data-wob-di="{angka}"] div.gNCp2e span.wob_t', first=True).text
        min_temp = r.html.find(f'div.wob_df[data-wob-di="{angka}"] div.QrNVmd span.wob_t', first=True).text
        description = r.html.find(f'div.wob_df[data-wob-di="{angka}"] img[alt]', first=True)
        print(f' Max Temp : {max_temp}{unit}', "\n",f'Min Temp : {min_temp}{unit}', "\n", "Description : ", description.attrs.get('alt'))

if __name__ == "__main__":
    query = 'jakarta'
    weather(query)    

