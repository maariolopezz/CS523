import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/goofysS3/Test\ Media/C0003-UHD.MP4 -ss 00:00:05 -t 00:00:15 /storage/goofysS3/goofys/gCuts1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("goofys-1: " + str(lapse))
os.system("ffmpeg -i /storage/goofysS3/Test\ Media/C0003-UHD.MP4 -ss 00:00:15 -t 00:00:25 /storage/goofysS3/goofys/gCuts2.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("goofys-2: " + str(lapse))
os.system("ffmpeg -i /storage/goofysS3/Test\ Media/C0003-UHD.MP4 -ss 00:00:40 -t 00:00:50 /storage/goofysS3/goofys/gCuts3.mp4 -loglevel fatal")

lapse =  time.time() - tinit
print("goofys-3: " + str(lapse))


with open('./stats/goofysff6.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

os.system('fusermount -u /storage/goofysS3/')
time.sleep(2)
