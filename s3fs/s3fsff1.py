import time
import os
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs -o direct_io')
	time.sleep(3)

	tinit = time.time()

	os.system("ffprobe -v error -show_format -show_streams /storage/s3fsnc/Test\ Media/C0001-HD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/s3fsnc/Test\ Media/C0002-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/s3fsnc/Test\ Media/C0003-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	os.system("ffprobe -v error -show_format -show_streams /storage/s3fsnc/Test\ Media/C0005-UHD.MP4 > /home/centos/movedFiles/tmp.txt")
	lapse =  time.time() - tinit
	with open('./stats/s3fsff1.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("s3fs: " + str(lapse))

	os.system('fusermount -u /storage/s3fsnc/')
	time.sleep(2)
