import requests
import re

o=requests.get('https://cokebar.github.io/gfwlist2dnsmasq/dnsmasq_gfwlist.conf').text
pattern = re.compile(r'(?<=/).*?(?=/)')
result1 = pattern.findall(o)
output=''
for one in result1:
  output+='address=/%s/::\n'%one
#print(output)
com=requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').text
com=re.sub('#.*\n','',com).split('\n')
com.remove('')
for one in com:
  output+='address=/%s/::\n'%one
with open('ip4.conf','w') as f:
  f.write(output)
