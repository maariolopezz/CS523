import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
time.sleep(1)

tinit = time.time()

os.system("ffmpeg -i /home/centos/movedFiles/Test\ Media/C0003-UHD.MP4 -ss 00:00:05 -t 00:00:15 /home/centos/movedFiles/sCuts1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("local-1: " + str(lapse))
os.system("ffmpeg -i /home/centos/movedFiles/Test\ Media/C0003-UHD.MP4 -ss 00:00:15 -t 00:00:25 /home/centos/movedFiles/sCuts2.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("local-2: " + str(lapse))
os.system("ffmpeg -i /home/centos/movedFiles/Test\ Media/C0003-UHD.MP4 -ss 00:00:40 -t 00:00:50 /home/centos/movedFiles/sCuts3.mp4 -loglevel fatal")

lapse =  time.time() - tinit
print("local-3: " + str(lapse))

with open('./stats/localff6.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])


