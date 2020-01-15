import serial
import time

addresslist = []
ard = serial.Serial("COM3",2000000)
def send_to(data, address):
    ard.write(b"sendto")
    time.sleep(0.002)
    ard.write(bytes(str(int(address, 8)), "utf-8"))
    time.sleep(0.002)
    ard.write(bytes(str(data), "utf-8"))
    time.sleep(0.002)
    while 1:
        for i in ard.readline().decode().split("\r\n"):
            print(i)
            if i == "succ":
                break
        else:
            continue
        break
def build_room_hub(datas):
    if len(addresslist) > 0:
        
        for i in addresslist:
            if datas[2] in i[0]:
                print("ok")
                
                return 0
    print
    addresslist.append([datas[2], datas[1], datas[3][:3], []])
def add_module_to_room(datas,):
    
    for teg in range(len(addresslist)):
        if addresslist[teg][1] == datas[1]:
            if len(addresslist[teg][3]) > 0:
                for deg in addresslist[teg][3]:
                    if deg[1] == datas[3] or deg[0] == datas[2]:
                        return 0 
              
            addresslist[teg][3].append([datas[2], datas[3], datas[4]])
            
                
                
                        
while 1:
    data = ard.readline()
    print(data)
    data = data.decode().split("\r\n")
    for i in data:
        if i != "":
            print(i)
            datas = i.split(" ")
            if datas[0] == "br":
                build_room_hub(datas)
            if datas[0] == "am":
                print("hay")
                if add_module_to_room(datas) != 0:
                    pass
                        

    print(addresslist) 
