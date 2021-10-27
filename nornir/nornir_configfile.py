# Cau hinh thiet bi tu file co san voi nornir + netmiko
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

def baseconfig(ipvzero):
    ipvzero.run(task=netmiko_send_config, config_file= "config_textfile") #cau hinh dua tren file co san (config_textfile)
    ipvzero.run(task=netmiko_send_command, command_string = "show ip int brief") #thua hien lenh show ip int brief tren cisco

#results = nr.run(task = baseconfig)
# notactor = nr.filter(F(groups__contains="cisco")) #chi cau hinh voi nhom thiet bi la cisco 
notactor = nr.filter(F(groups__contains="cisco") & F(eve =True))     #chi cau hinh voi nhom thiet bi la cisco va du lieu thuoc ve nhom "eve"

#notactor = nr.filter(F(groups__contains="junos")) #chi cau hinh voi nhom thiet bi la juniper

results = notactor.run(task = baseconfig)

print_title("DEPLOYING AUTOMATED BASELINE CONFIGURATIONS")
print_result(results)