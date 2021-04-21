import requests
import re

ori=requests.get('https://cokebar.github.io/gfwlist2dnsmasq/dnsmasq_gfwlist.conf').text

with open('ownlist.txt') as f:
  global ori
  ori+='\n'
  for line in f:
    ori+='server=/%s/127.0.0.1#5353\n'%line
pattern = re.compile(r'(?<=/).*?(?=/)')
result1 = pattern.findall(ori)
output=''
for one in result1:
  output+='address=/%s/::\n'%one
#print(output)
with open('output/gfwipv4.conf','w') as f:
  f.write(ori+'\n'+output)
