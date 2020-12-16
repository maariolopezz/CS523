import time
import os
import csv

os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
time.sleep(1)

tinit = time.time()

os.system("ffmpeg -i /home/centos/movedFiles/Test\ Media/C0003-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /home/centos/movedFiles/sTrans1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("local-1: " + str(lapse))
os.system("ffmpeg -i /home/centos/movedFiles/Test\ Media/C0002-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /home/centos/movedFiles/sTrans2.mp4 -loglevel fatal")
lapse =  time.time() - tinit

print("local-2: " + str(lapse))

with open('./stats/localff4.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

