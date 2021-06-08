https://w311ang.github.io/dnsmasq_ipv4_only/ipv4only.conf

https://w311ang.github.io/dnsmasq_ipv4_only/gfwipv4.conf

```shell
wget https://raw.githubusercontent.com/w311ang/dnsmasq_ipv4_only/main/dnscheck.py -O $PREFIX/bin/dnscheck
```

[Edit](https://github.com/w311ang/dnsmasq_ipv4_only/edit/main/ownlist.txt)

`dnsmasq.conf`
```
no-resolv
strict-order
```
WAN口DNS设置192.168.2.1
