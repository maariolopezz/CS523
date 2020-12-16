import time
import os
import csv

for y in range(10):

	os.system('rm -rf /tmp/riofs/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	time.sleep(3)

	tinit = time.time()

	os.system("ffprobe -v error -show_format -show_streams /storage/riofsS3nc/Test\ Media/C0001-HD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/riofsS3nc/Test\ Media/C0002-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/riofsS3nc/Test\ Media/C0003-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/riofsS3nc/Test\ Media/C0005-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	lapse =  time.time() - tinit
	with open('./stats/rioff1.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("riofs: " + str(lapse))
	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(2)
