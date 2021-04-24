import requests
import re

ori=requests.get('https://cokebar.github.io/gfwlist2dnsmasq/dnsmasq_gfwlist.conf').text
with open('ownlist.txt') as f:
  ori+='\n'
  for line in f:
    line=line.replace('\n','')
    print(line)
    ori+='server=/%s/127.0.0.1#5353\n'%line
pattern = re.compile(r'(?<=/).*?(?=/)')
result1 = pattern.findall(ori)

com=requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').text
com=re.sub('#.*\n','',com).split('\n')
com.remove('')

output=''
for one in result1:
  output+='address=/%s/::\n'%one
output+='\n'
for one in com:
  output+='server=/%s/211.142.211.124\n'%one
  output+='address=/%s/::\n'%one
#print(output)
with open('docs/gfwipv4.conf','w') as f:
  f.write(ori+'\n'+output)
