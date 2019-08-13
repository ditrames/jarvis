comp_data = ""
load_data = ""

mf_loaddata = 0


data = [["light control",["lights on", "lights off"]], ["blind control", ["blinds open", "blinds close"]]]
for i in enumerate(data):
    load_data = ""
    mf_loaddata = i[0]+1
    print(mf_loaddata)
    load_data += ",mf,{},{}/".format(str(mf_loaddata), i[1][0])
    load_data = str(len(load_data)) + load_data
    comp_data += load_data
for i in enumerate(data):
    sf_loaddata = i[0]+1
    for d in enumerate(i[1][1]):
        print(d)
        load_data = ""
        load_data += ",sf,{},{},{}/".format(str(sf_loaddata), d[1], d[0]+1)
        load_data = str(len(load_data)) + load_data
        comp_data += load_data
print(comp_data)



