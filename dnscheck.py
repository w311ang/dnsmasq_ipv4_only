#!/usr/bin/env python3
import dns.resolver
import sys
import requests
import logging
import tldextract

logger = logging.getLogger('mylogger')
logger.addHandler(logging.StreamHandler())
if '--debug' in sys.argv:
  logger.setLevel(logging.DEBUG)
domain=sys.argv[1]
domain='.'.join(tldextract.extract(domain)[:3])
logger.debug(domain)

def query(domain,nameserver,tcp=False):
  router=dns.resolver.Resolver(configure=False)
  router.nameservers=[nameserver]
  logger.debug(router.resolve(domain,tcp=tcp).answer)
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
  wrong=query(domain,'211.142.211.124')
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
    print('已被污染，请添加 %s '%domain)
  if chinaip:
    print('请将%s从白名单中移除'%','.join(right))
