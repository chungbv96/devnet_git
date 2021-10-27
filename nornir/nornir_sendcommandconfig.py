#!/usr/bin/env python

# Filename:                     nornir-tutorial.py
# Command to run the program:   python nornir-tutorial.py

# Import dependencies
from logging import config
from nornir import InitNornir
from nornir.core.inventory import Group
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
#from nornir.core.filter import F


print("Nhap cac lenh muon cau hinh tren cong. Yeu cau: Nhap dung cu phap. Moi lenh cach nhau boi 1 dau phay (,) ")
print("VIDU cu phap nhap nhu sau:  int gi1/0/5, shutdown, switchport access vlan 500")

#commands = input("Enter your command: ")
#cmds = commands.split(",")

# for cmd in commands:
#     nr = InitNornir(config_file="config.yaml")
#     result = nr.run(
#         task=netmiko_send_config, 
#         config_commands=cmd
#         )
#     print_result(result)

nr = InitNornir(config_file="config.yaml")


def function_tasks(task):
    commands = input("Enter your command: ")
    cmds = commands.split(",")
    #task.run(name="Show interface status", task=netmiko_send_command, command_string=commands)
    task.run(name="Cau hinh tuy chon", task=netmiko_send_config, config_commands=cmds)
    
tasks_result = nr.run(task=function_tasks)
print_result(tasks_result)