import time
import os
import csv

os.system('rm -rf /tmp/riofs/*')
os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
time.sleep(3)

tinit = time.time()

os.system("ffmpeg -i /storage/riofsS3nc/Test\ Media/C0003-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/riofsS3nc/riofs/rTrans1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("riofs-1: " + str(lapse))
os.system("ffmpeg -i /storage/riofsS3nc/Test\ Media/C0002-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/riofsS3nc/riofs/rTrans2.mp4 -loglevel fatal")

lapse =  time.time() - tinit

print("riofs-2: " + str(lapse))

with open('./stats/rioff4.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

os.system('rm -rf /storage/riofsS3nc/riofs/rTrans1.mp4')
os.system('rm -rf /storage/riofsS3nc/riofs/rTrans2.mp4')
os.system('fusermount -u /storage/riofsS3nc/')
time.sleep(2)
