import requests
import re

with open('gfwlist.conf') as f:
  o=f.read()
#o=requests.get('https://cokebar.github.io/gfwlist2dnsmasq/dnsmasq_gfwlist.conf').text
pattern = re.compile(r'(?<=/).*?(?=/)')
result1 = pattern.findall(o)
output=''
for one in result1:
  output+='address=/%s/::\n'%one
#print(output)
with open('ipv4only.conf','w') as f:
  f.write(output)
