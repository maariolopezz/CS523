import time
import os
import csv

for y in range(5):

	os.system('rm -rf /tmp/riofs/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	time.sleep(3)

	tinit = time.time()
	os.system("ffmpeg -r 60 -start_number 874 -i \"/storage/riofsS3nc/Test Media/Timelapse/parte-1/DSC09%03d.JPG\" -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/riofsS3nc/riofs/rTimel.mp4 -loglevel fatal")
	lapse =  time.time() - tinit

	with open('./stats/rioff5.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("riofs: " + str(lapse))
	os.system('rm -rf /storage/riofsS3nc/riofs/rTimel.mp4')
	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(2)
