import serial
addresslist = []
ard = serial.Serial("COM4",2000000,timeout= 2)
def build_room_hub(datas):
    if len(addresslist) > 0:
        for i in datas:
            if datas[2] in i or datas[1] in i:
                #print("ok")
                
                return 0
    addresslist.append([datas[2], datas[1], datas[3], []])
def add_module_to_room(datas,):
    
    for teg in range(len(addresslist)):
        if addresslist[teg][1] == datas[1]:
            if len(addresslist[teg][3]) > 0:
                for deg in addresslist[teg][3]:
                    if deg[1] == datas[3] or deg[0] == datas[2]:
                        return 0 
              
            addresslist[teg][3].append([datas[2], datas[3], datas[4]])
           

    
def get_address(id_):
    if len(addresslist) > 0:
        for i in addresslist:
            if id_ in i:
                datam = i[-1]
                baceid = i[0].replace("0", "")
                deg = int("55555"[0:5-len(baceid)])
                tick = 0
                output = []
                while deg >= tick:
                    output.append(tick)
                    tick += 1
                compiled = []
                for i in range(len(output)-1):
                    megd = output[i]
                    data = str(megd)
                    done = True
                    for d in data:
                        intvar = int(d)
                        if intvar > 5 or intvar == 0:
                            done = False
                            break
                    if done:
                        compiled.append(output[i])
                compiled = ["0"+str(x)+baceid for x in compiled]
                fcompiled = []
                usedaddresses = []
                for t in datam:
                    usedaddresses.append(t[0])
                for peg in compiled:
                    if peg not in usedaddresses:
                        fcompiled.append(peg)
                return fcompiled[0]
            
                
                
                        
while 1:
    data = ard.readline().decode().split("\r\n")
    for i in data:
        if i != "":
            print(i)
            datas = i.split(" ")
            if datas[0] == "br":
                build_room_hub(datas)
            if datas[0] == "am":
                #print("hay")
                add_module_to_room(datas)
                ard.write(b"sendto")
                ard.write(b"011")
                ard.write(b"datalol")
    print(addresslist)   
  #  print(get_address("hub"))
