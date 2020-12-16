import time
import os
import csv

for y in range(5):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs -o direct_io')
	time.sleep(3)

	tinit = time.time()
	os.system("ffmpeg -r 60 -start_number 874 -i \"/storage/s3fsnc/Test Media/Timelapse/parte-1/DSC09%03d.JPG\" -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/s3fsnc/s3fs/sTimel2.mp4 -loglevel fatal")
	lapse =  time.time() - tinit
	with open('./stats/s3fsff5.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("s3fs: " + str(lapse))
	os.system('rm -rf /storage/s3fsnc/s3fs/sTimel2.mp4')
	os.system('fusermount -u /storage/s3fsnc/')
	time.sleep(2)
