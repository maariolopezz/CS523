import time
import os
import csv

os.system('rm -rf /tmp/riofs/*')
os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml mariomediabucket /storage/riofsS3nc')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/riofsS3nc/Test\ Media/C0003-UHD.MP4 -ss 00:00:05 -t 00:00:15 /storage/riofsS3nc/riofs/rCuts1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("riofs-1: " + str(lapse))
os.system("ffmpeg -i /storage/riofsS3nc/Test\ Media/C0003-UHD.MP4 -ss 00:00:15 -t 00:00:25 /storage/riofsS3nc/riofs/rCuts2.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("riofs-2: " + str(lapse))
os.system("ffmpeg -i /storage/riofsS3nc/Test\ Media/C0003-UHD.MP4 -ss 00:00:40 -t 00:00:50 /storage/riofsS3nc/riofs/rCuts3.mp4 -loglevel fatal")

lapse =  time.time() - tinit
print("riofs-3: " + str(lapse))

with open('./stats/rioff6.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])
os.system('fusermount -u /storage/riofsS3nc/')
time.sleep(2)
