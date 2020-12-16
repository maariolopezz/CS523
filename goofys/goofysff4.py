import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/goofysS3/Test\ Media/C0003-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/goofysS3/goofys/gTrans1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("goofys-1: " + str(lapse))
os.system("ffmpeg -i /storage/goofysS3/Test\ Media/C0002-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/goofysS3/goofys/gTrans2.mp4 -loglevel fatal")

lapse =  time.time() - tinit

with open('./stats/goofysff4.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

print("goofys-2: " + str(lapse))
os.system('rm -rf /storage/goofysS3/goofys/gTrans1.mp4')
os.system('rm -rf /storage/goofysS3/goofys/gTrans2.mp4')
os.system('fusermount -u /storage/goofysS3/')
time.sleep(2)
