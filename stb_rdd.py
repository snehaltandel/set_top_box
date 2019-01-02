from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('stb_scratch').setMaster('local')
sc = SparkContext(conf=conf)

lines = sc.textFile("Set_Top_Box_Data.txt")
d_id = lines.map(lambda x:x.split("^")[5])
xmld = lines.map(lambda x:x.split("^")[4])

''' Define a Function to Parse Values from xmld '''

import xml.etree.ElementTree as ET
def xml_data(a):
    data = a.map(lambda x:str(x))
    data = ET.fromstring(a)
    values = []
    for child in data.iter('nv'):
        kv = dict(child.attrib)
        k = kv["n"]
        v = kv["v"]
        values.append(v)
	return values

obj = xml_data(xmld)
print(obj.take(2))
