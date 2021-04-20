#!/bin/sh

set -e -o pipefail

[ "$1" != "force" ] && [ "$(nvram get ss_update_gfwlist)" != "1" ] && exit 0
IPV4ONLY_URL="https://raw.githubusercontent.com/w311ang/dnsmasq_ipv4_only/main/ipv4only.conf"

logger -st "ipv4only" "Starting update..."

rm -f /tmp/ipv4only.conf
curl -k -s -o /tmp/ipv4only.conf --connect-timeout 5 --retry 3 $IPV4ONLY_URL

mkdir -p /etc/storage/gfwlist/
mv -f /tmp/ipv4only.conf /etc/storage/gfwlist/ipv4only.conf

mtd_storage.sh save >/dev/null 2>&1

restart_dhcpd
restart_dns

logger -st "ipv4only" "Update done"
