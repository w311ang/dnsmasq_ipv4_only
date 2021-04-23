import requests
import re

com=requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').text
com=re.sub('#.*\n','',com).split('\n')
com.remove('')
for one in com:
  output+='address=/%s/::\n'%one
with open('docs/ipv4only.conf','w') as f:
  f.write(output)
