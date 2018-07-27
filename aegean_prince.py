from re import I, findall, search
import requests 
import time

site = 'http://www.loveulicious.co.uk'


def decode(string):
    return string.encode('utf-8')

def get_all_plugins(site):
    # plugins = []
    r = requests.get(url=site)
    print(r.content)
    plugins = findall(decode('/wp-content/plugins/(.+?)/'), r.content)
    for i in plugins:
        #length = len(str(i))
        print(i)
    return None

st = time.time()
get_all_plugins(site)
#s = "b'xoxoxoxo'"
#l = len(s)
#print(s[2:l-1])
end = time.time()

print(end-st)