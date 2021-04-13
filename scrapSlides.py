import json
import requests
import os



# url_slides_bbb = "https://bbb2.centrale-marseille.fr/bigbluebutton/presentation/8683b52416ed6a1523a20c825650d513fe167030-1612873337346/8683b52416ed6a1523a20c825650d513fe167030-1612873337346/0c0fb75c9b49485c4a21634d165bdb517bec9660-1612873602910/svg/"
#url_slides_bbb = "https://bbb4.centrale-marseille.fr/bigbluebutton/presentation/8d68fed661e8362aaa428bd0d55ab529b85f6cc3-1616136849092/8d68fed661e8362aaa428bd0d55ab529b85f6cc3-1616136849092/c909a2907a375a1ca13051fbab715756f3bf1a6d-1616136849259/svg/"
#url_slides_bbb = "https://bbb4.centrale-marseille.fr/bigbluebutton/presentation/6eb3f9a996681318e243a1ca44d0a4045ab72c03-1617000007834/6eb3f9a996681318e243a1ca44d0a4045ab72c03-1617000007834/e50b4945ebae759590ca57ff911974022eca7a6e-1617000060343/svg/"
#url_slides_bbb = "https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/b7cee96775ef5eadb6991f601d09683c81021d53-1618301816466/svg/"
url_slides_bbb = "https://bbb1.centrale-marseille.fr/bigbluebutton/presentation/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/72a40bfaabf993f8314ef45ca5ba0d053dcacfd7-1618301407645/03e419217621df6af41303f9504397b2d0e44eb0-1618306059443/svg/"
nb_max = 60

cookies = { }

headers = { "Host": "bbb2.centrale-marseille.fr",
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
        with open("slides/slide" + str(i) +".svg", 'wb') as f:
            f.write(r.content)
            i += 1
    else:
        print(f"Scrap des {i-1} slides effectué")
        break
