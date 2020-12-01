
import requests as requests

def gethtmltext(url):
    r = requests.get(url)
    return r.text

fp = open("GVB.html","w",encoding="utf-8-sig")
fp.write(gethtmltext("http://astro.vanbuitenen.nl/comets"))
fp.close()

fp = open("COBS.html","w",encoding="utf-8-sig")
fp.write(gethtmltext("https://cobs.si/"))
fp.close()

fp = open("recents.html","w",encoding="utf-8-sig")
fp.write(gethtmltext("https://cobs.si/recent"))
fp.close()
