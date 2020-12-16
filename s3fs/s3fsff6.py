import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/s3fsnc/Test\ Media/C0003-UHD.MP4 -ss 00:00:05 -t 00:00:15 /storage/s3fsnc/s3fs/sCuts1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("s3fs-1: " + str(lapse))
os.system("ffmpeg -i /storage/s3fsnc/Test\ Media/C0003-UHD.MP4 -ss 00:00:15 -t 00:00:25 /storage/s3fsnc/s3fs/sCuts2.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("s3fs-2: " + str(lapse))
os.system("ffmpeg -i /storage/s3fsnc/Test\ Media/C0003-UHD.MP4 -ss 00:00:40 -t 00:00:50 /storage/s3fsnc/s3fs/sCuts3.mp4 -loglevel fatal")

lapse =  time.time() - tinit
print("s3fs-3: " + str(lapse))

with open('./stats/s3fsff6.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

os.system('fusermount -u /storage/s3fsnc/')
time.sleep(2)
