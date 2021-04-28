import requests
import os
import time

pw=os.getenv('pw')
cmd='cat /etc/storage/gfwlist/dnsmasq_gfwlist.conf'

proxies = {
    'http': 'socks5://localhost:1080',
    'https': 'socks5://localhost:1080'
}
session = requests.Session()
session.proxies.update(proxies)

session.post('http://192.168.2.1/Shadowsocks_action.asp',data='connect_action=Update_gfwlist',auth=('w311ang',pw))
session.get('http://192.168.2.1/Logout.asp')

time.sleep(3)
session.post('http://192.168.2.1/apply.cgi',data={'action_mode':' SystemCmd ','current_page':'console_response.asp','next_page':'console_response.asp','SystemCmd':cmd},auth=('w311ang',pw))
rep=session.get('http://192.168.2.1/console_response.asp',auth=('w311ang',pw)).text
with open('docs/gfwipv4.conf') as f:
  be=f.read()
if not rep==be:
  session.get('http://192.168.2.1/Logout.asp')
  raise Exception('未能同步')
session.get('http://192.168.2.1/Logout.asp')
