#!/usr/bin/env python

# Filename:                     nornir-tutorial.py
# Command to run the program:   python nornir-tutorial.py

# Import dependencies
from nornir import InitNornir
from nornir.core.inventory import Group
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
from nornir.core.filter import F



# Initialize Nornir
nr = InitNornir(config_file="config.yaml")


# switch1 = nr.filter(F(groups_contains="cisco"))

# cach1: normal
# results = switch1.run(netmiko_send_command, command_string="show ip int brief")
# output = nr.run(netmiko_send_config, config_commands="interface loopback100")
#output = nr.run(netmiko_send_config, config_commands=["interface loopback101","description Configured with nornir-netmiko","ip add 10.1.7.1 255.255.255.255"])
#results = nr.run(netmiko_send_command, command_string="show version")

# cach2: su dung ham
def function_tasks(task):
    task.run(name="Show interface status", task=netmiko_send_command, command_string="show interface gi1/0/1 status")
    task.run(name="Create a loopback interface", task=netmiko_send_config, config_commands=["interface loop12", "description Created by nornir-netmiko"])

tasks_result = nr.run(task=function_tasks)


print_result(tasks_result)
#print_result(output)

