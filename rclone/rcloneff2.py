import time
import os
import subprocess
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode off s3-rclone-bucket:mariomediabucket /storage/3rclone &')
	time.sleep(5)

	tinit = time.time()

	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/3rclone/Test\ Media/C0001-HD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/3rclone/Test\ Media/C0002-UHD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/3rclone/Test\ Media/C0003-UHD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/3rclone/Test\ Media/C0005-UHD.MP4")
	lapse =  time.time() - tinit
	with open('./stats/rcloneff2.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("rclone: " + str(lapse))

	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
	while result > 150:
		print('ps -eaf | grep rclone')
		time.sleep(7)
		result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

	time.sleep(4)
