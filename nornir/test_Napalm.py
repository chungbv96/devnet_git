from napalm import get_network_driver
import json

driver= get_network_driver('ios') #=>Device Cisco IOS
router=driver('192.168.100.3','admin','cisco123') # username cần khai báo privilege 15 thì user này sẽ by pass enable password
#router=driver('192.168.100.3','admin1','cisco123', optional_args = {"secret": "cisco"})  # user này k được khai báo privilege 15 lúc tạo nên cần nhập pass enable với tùy chọn: optional_args = {"secret": "cisco"}
router.open()
output=router.get_facts() #=>Lấy thông tin OS, serial number,hostname…
print(json.dumps(output, indent=5)) #=> in ra dạng Json
output2=router.get_arp_table()#=>Lấy bảng arp của router
print(json.dumps(output2, indent=5))

driver= get_network_driver('junos') #=> Device Juniper
router=driver('192.168.100.4','lab','lab123')
router.open()
output3=router.get_facts()
print(json.dumps(output3, indent=5))
output4=router.get_arp_table()#=>Lấy bảng arp của router
print(json.dumps(output4, indent=5))
