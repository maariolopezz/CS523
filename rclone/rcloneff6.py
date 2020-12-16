import time
import os
import subprocess
import csv


os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode writes s3-rclone-bucket:mariomediabucket /storage/3rclone &')
time.sleep(5)

tinit = time.time()

os.system("ffmpeg -i /storage/3rclone/Test\ Media/C0003-UHD.MP4 -ss 00:00:05 -t 00:00:15 /storage/3rclone/rclone/cCuts1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("rclone-1: " + str(lapse))
os.system("ffmpeg -i /storage/3rclone/Test\ Media/C0003-UHD.MP4 -ss 00:00:15 -t 00:00:25 /storage/3rclone/rclone/cCuts2.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("rclone-2: " + str(lapse))
os.system("ffmpeg -i /storage/3rclone/Test\ Media/C0003-UHD.MP4 -ss 00:00:40 -t 00:00:50 /storage/3rclone/rclone/cCuts3.mp4 -loglevel fatal")

lapse =  time.time() - tinit
print("rclone-3: " + str(lapse))

with open('./stats/rcloneff6.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
while result > 150:
	print('ps -eaf | grep rclone')
	time.sleep(7)
	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

time.sleep(4)
