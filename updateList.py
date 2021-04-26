import requests

pw=os.getenv('pw')

proxies = {
    'http': 'socks5://localhost:1080',
    'https': 'socks5://localhost:1080'
}
session = requests.Session()
session.proxies.update(proxies)

requests.post('http://192.168.2.1/Shadowsocks_action.asp',data='connect_action=Update_gfwlist',auth=('w311ang',pw)
