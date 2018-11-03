""" Text file encloses partial data into <d> tags. And Other information is separated by "^" """
import xml.etree.ElementTree as et
import json
with open("./data/Set_Top_Box_Data.txt", "r") as f:
    draw = []
    for l in f:
        data = l.split("^")
        sui = data[0]
        rt = data[1]
        ei = data[2]
        ts = data[3]
        xmld = data[4]
        di = data[5]
        st = data[6].strip("\n")
        root = et.fromstring(str(xmld))
        draw = dict({"server_unique_id": sui, "request_type": rt, "event_id": ei, "timestamp": ts, "device_id": di,
                     "secondary_timestamp": st})
        for nv in root.iter("nv"):
            d = dict(nv.attrib)
            key = d["n"]
            value = d["v"]
            draw.update(dict({key : value}))
        with open("./data/Set_Top_Box_Data.json", "a+") as w:
            w.write(str(draw))
        print(draw)


