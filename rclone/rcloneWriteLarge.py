import time
import os
import subprocess
import csv

for y in range(10):
	os.system('rm -rf /root/.cache/rclone/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode off s3-rclone-bucket:mariomediabucket /storage/3rclone &')
	time.sleep(4)


	comm = "dd if=/dev/zero of=/storage/3rclone/rclone/tesFileLarge-" + str(y) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"

	tinit = time.time()


	os.system(comm)
	lapse =  time.time() - tinit
	
	with open('./stats/rcloneWriteLarge.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("rclone: " + str(lapse))
	
	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
	while result > 150:
		print('ps -eaf | grep rclone')
		time.sleep(7)
		result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

	time.sleep(10)
