import csv
import os

os.chdir('/Users/Agraynel/Desktop/ECE4950/hw0') #set working directory
reader = list(csv.reader(open('heightsagetest.csv'))) 
dic = []
for row in reader:
	age = int(row[1])
	boy = int(row[2])
	if ((boy == 1 and age > 8) or (boy == 0 and age > 11)):
		print '1'
	else:
		print '0'