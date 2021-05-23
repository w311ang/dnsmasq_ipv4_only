import dns.resolver
import sys
import requests
import logging
import tldextract

domain=sys.argv[1]
logger = logging.getLogger('mylogger')
logger.addHandler(logging.StreamHandler())
if '--debug' in sys.argv:
  logger.setLevel(logging.DEBUG)

def query(domain,nameserver,tcp=False):
  router=dns.resolver.Resolver(configure=False)
  router.nameservers=[nameserver]
  ans=router.resolve(domain,'A',tcp=tcp)
  iplist=[]
  for i in ans:
    iplist.append(str(i))
  return iplist

def geoip(ip):
  json=requests.get('https://api.ip.sb/geoip/'+ip).json()
  org=json['organization']
  country=json['country']
  return {'ip':ip,'org':org,'cy':country}

def wrong(domain):
  global right
  right=query(domain,'8.8.8.8',tcp=True)
  logger.debug([geoip(right[0]),right])
  wrong=query(domain,'8.8.8.8')
  logger.debug([geoip(wrong[0]),wrong])
  iswrong=sorted(right)!=sorted(wrong)
  return iswrong

iswrong=wrong(domain)
logger.info('劫持：'+str(iswrong))

if iswrong:
  text=requests.get('https://w311ang.github.io/dnsmasq_ipv4_only/gfwipv4.conf').text
  tlds=tldextract.extract(domain)
  string='server=/%s/127.0.0.1#5353'
  strings=[string%(tlds.domain+'.'+tlds.suffix),string%domain,string%tlds.suffix]
  logger.debug(strings)
  solved=False
  for i in strings:
    if i in text:
      solved=True
      break
  logger.info('修复：'+str(solved))
  chinaip=False
  for i in right:
    cy=geoip(i)['cy']
    if cy=='China':
      chinaip=True
      break
  printtext=''
  if solved==False:
    printtext+='已被污染，未解决'
  if chinaip:
    printtext+='，请将此IP从白名单中移除'
  print(printtext)
