import time
import os
import subprocess
import csv

for y in range(10):

	os.system('rm -rf /root/.cache/rclone/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode off s3-rclone-bucket:mariomediabucket /storage/3rclone &')
	time.sleep(5)

	tinit = time.time()

	for x in range(y*100+1,(y+1)*100+1):
		os.system("dd if=/storage/3rclone/Test\ Media/Timelapse/parte-2/DSC00" + str(x).zfill(3) + ".JPG of=/dev/null bs=1 count=1 iflag=nocache oflag=nocache status=none")
	lapse =  time.time() - tinit

	with open('./stats/rcloneReadFirst.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("rclone: " + str(lapse))
	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
	while result > 150:
		print('ps -eaf | grep rclone')
		time.sleep(7)
		result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

	time.sleep(2)




