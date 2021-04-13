import json
import requests
import os


def scrap_slides(url_slides_bbb, temp_path):
    nb_max = 60
    cookies = {}
    headers = {"Host": "bbb2.centrale-marseille.fr",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding": "gzip, deflate, br",
               "DNT": "1",
               "Connection": "keep-alive",
               "Upgrade-Insecure-Requests": "1"
               }
    i = 1
    while True:
        url = url_slides_bbb + str(i)
        r = requests.get(url, cookies=cookies, headers=headers)
        if r.status_code == 200:
            with open(temp_path + "/slides/slide" + str(i) + ".svg", 'wb') as f:
                f.write(r.content)
                i += 1
        else:
            print(f"Scrap des {i-1} slides effectué")
            break
