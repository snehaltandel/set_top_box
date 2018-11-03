''' Text file encloses partial data into <d> tags. And Other information is separated by "^" '''
import xml.etree.ElementTree as et
def file():
    with open('./data/Set_Top_Box_Data.txt', 'r') as f:
        for l in f:
            data = l.split('^')
            return data

def data2():
    data = file()
    sui = str(data[0])
    rt = str(data[1])
    ei = str(data[2])
    ts = str(data[3])
    di = str(data[5])
    st = str(data[6].strip('\n'))
    draw = dict({'server_unique_id' : sui, 'request_type' : rt, 'event_id' : ei, 'timestamp' : ts, 'device_id' : di, 'secondary_timestamp' : st})
    return draw

def data3():
    data = file()
    xmld = str(data[4])
    root = et.fromstring(str(xmld))
    kv2 = {}
    for nv in root.iter('nv'):
        d = dict(nv.attrib)
        key = d['n']
        value = d['v']
        kv2 = dict({key : value})
        draw = data2()
        draw.update(kv2)   #Unable to iterate through all the nv tags with n,v data
        return draw

obj2 = data2()
print(obj2)
obj3 = data3()
print(obj3)

