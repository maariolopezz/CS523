import time
import os
import csv

for y in range(5):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(3)

	tinit = time.time()
	os.system("ffmpeg -r 60 -start_number 874 -i \"/storage/goofysS3/Test Media/Timelapse/parte-1/DSC09%03d.JPG\" -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/goofysS3/goofys/gTimel.mp4 -loglevel fatal")
	lapse =  time.time() - tinit

	with open('./stats/goofysff5.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("goofys: " + str(lapse))
	os.system('rm -rf /storage/goofysS3/goofys/gTimel.mp4')
	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(2)
