#!/usr/bin/env python

# Filename:                     nornir-tutorial.py
# Command to run the program:   python nornir-tutorial.py

# Import dependencies
from nornir import InitNornir
from nornir.core.inventory import Group
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
import json
from nornir.core.filter import F #thu vien dung de loc thiet bi 

# Initialize Nornir
#nr = InitNornir(config_file="config.yaml")

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

# results = nr.run(
#     task=napalm_get, getters=["facts", "interfaces"] # show interface tren devices (toan bo cac thiet bi)
# )

cisco_hosts = nr.filter(platform="ios") # chi lay nhung thiet bi la cisco
#juniper_hosts = nr.filter(platform="junos") # chi lay nhung thiet bi la juniper
get_interfaces_ip_result = cisco_hosts.run(napalm_get, getters=['get_interfaces_ip']) #lay dia chi IP cua nhung interface tren thiet bi

print_result(get_interfaces_ip_result)

#print_result(results)

