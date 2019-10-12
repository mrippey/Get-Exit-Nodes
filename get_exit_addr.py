# Title: get_exit_addr.py
#
# Author: Mike
#
# Twitter: @nahamike01


import urllib.request
from bs4 import BeautifulSoup
import re

get_nodes = "https://check.torproject.org/exit-addresses"

get_url = urllib.request.urlopen(get_nodes)

get_soup = BeautifulSoup(get_url, "html.parser").encode("utf-8")

with open("/Users/m_a_t/Documents/tor_output.html", "w") as f:
    f.write(str(get_soup))

input("Press Enter to Continue...")

file = open("/Users/m_a_t/Documents/tor_output.html", "r")
exit_addrs = []
for txt in file.readlines():
    txt = txt.rstrip()
    reg = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',txt)
    if reg:
        exit_addrs.extend(reg)

for nodes in exit_addrs:
    output_file = open("/Users/m_a_t/Documents/tor_exit_nodes.txt", "a")
    addrs = "".join(nodes)
    if '' not in addrs:
        print("Tor Exit Node IP: %s" % addrs)
        output_file.write(addrs)
        output_file.write("\n")


file.close()
output_file.close()
