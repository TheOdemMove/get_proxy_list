from bs4 import BeautifulSoup
import urllib       


def get_proxy_list():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    url = 'https://free-proxy-list.net/'

    req = urllib.request.Request(url=url, headers=headers)
    open_url = urllib.request.urlopen(req)
    proxy_list = []

    soup = BeautifulSoup(open_url, 'html.parser')
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        ip_column = row.findAll('td')[0].contents
        port_column = row.findAll('td')[1].contents
        ipv4 = ",".join(ip_column)
        port = ",".join(port_column)
        proxy_list.append(str(ipv4) + ":" + str(port)) 

    return proxy_list

print(get_proxy_list())
