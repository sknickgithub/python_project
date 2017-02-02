import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('stream.xml')
root = tree.getroot()

Stream_data = open('streamdata.csv', 'w')

csvwriter = csv.writer(Stream_data)

for i in range(1,1500,1):
	stream = []
	z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	detector = z.getchildren()[0].text
	stream.append(detector)
	status = z.getchildren()[1].text
	stream.append(status)	
	csvwriter.writerow(stream)

Stream_data.close()

