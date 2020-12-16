import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs -o direct_io')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/s3fsnc/Test\ Media/C0003-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/s3fsnc/s3fs/sTrans1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("s3fs-1: " + str(lapse))
os.system("ffmpeg -i /storage/s3fsnc/Test\ Media/C0002-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/s3fsnc/s3fs/sTrans2.mp4 -loglevel fatal")
lapse =  time.time() - tinit

print("s3fs-2: " + str(lapse))

with open('./stats/s3fsff4.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

os.system('rm -rf /storage/s3fsnc/s3fs/sTrans1.mp4')
os.system('rm -rf /storage/s3fsnc/s3fs/sTrans2.mp4')
os.system('fusermount -u /storage/s3fsnc/')
time.sleep(2)
