import time
import os
import subprocess
import csv


os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode writes s3-rclone-bucket:mariomediabucket /storage/3rclone &')
time.sleep(5)

tinit = time.time()
os.system("ffmpeg -i /storage/3rclone/Test\ Media/C0003-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/3rclone/rclone/cTrans1.mp4 -loglevel fatal")
lapse =  time.time() - tinit
print("rclone-1: " + str(lapse))
os.system("ffmpeg -i /storage/3rclone/Test\ Media/C0002-UHD.MP4 -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/3rclone/rclone/cTrans2.mp4 -loglevel fatal")
lapse =  time.time() - tinit

print("rclone-2: " + str(lapse))

with open('./stats/rcloneff4.csv', 'a', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([lapse])

os.system('rm -rf /storage/3rclone/rclone/cTrans1.mp4')
os.system('rm -rf /storage/3rclone/rclone/cTrans2.mp4')
result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
while result > 150:
	print('ps -eaf | grep rclone')
	time.sleep(7)
	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

time.sleep(4)
