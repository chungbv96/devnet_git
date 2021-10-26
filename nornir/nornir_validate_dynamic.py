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


print("Nhap lenh show can kiem tra (neu can kiem tra nhieu lenh show thi moi lenh cach nhau 1 dau phay, Yeu Cau: Can phai nhap dung cu phap lenh):")
commands = input("Enter your command: ")
cmds = commands.split(",")

for cmd in cmds:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(
        task=netmiko_send_command, 
        command_string=cmd
        )
    print_result(result)

# def function_tasks(task):
#     commands = input("Enter your command: ")
#     cmds = commands.split(",")
#     for cmd in cmds:
#     #task.run(name="Show interface status", task=netmiko_send_command, command_string=commands)
#         task.run(name="Create a loopback interface", task=netmiko_send_config, config_commands=cmd)
    
# tasks_result = nr.run(task=function_tasks)
# print_result(tasks_result)