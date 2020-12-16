import time
import os
import subprocess
import csv

for y in range(5):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode writes s3-rclone-bucket:mariomediabucket /storage/3rclone &')
	time.sleep(5)

	tinit = time.time()

	os.system("ffmpeg -r 60 -start_number 874 -i \"/storage/3rclone/Test Media/Timelapse/parte-1/DSC09%03d.JPG\" -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /storage/3rclone/rclone/cTimel.mp4 -loglevel fatal")	

	lapse =  time.time() - tinit
	with open('./stats/rcloneff5.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("rclone: " + str(lapse))
	os.system('rm -rf /storage/3rclone/rclone/cTimel.mp4')
	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
	while result > 150:
		print('ps -eaf | grep rclone')
		time.sleep(7)
		result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

	time.sleep(4)
