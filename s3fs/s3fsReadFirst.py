import time
import os
import csv

for y in range(10):

	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs -o del_cache')
	time.sleep(1)

	tinit = time.time()

	for x in range(y*100+1,(y+1)*100+1):
		os.system("dd if=/storage/s3fsnc/Test\ Media/Timelapse/parte-2/DSC00" + str(x).zfill(3) + ".JPG of=/dev/null bs=1 count=1 iflag=nocache oflag=nocache status=none")

	lapse =  time.time() - tinit
	with open('./stats/s3fsReadFirst.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])


	print("s3fs: " + str(lapse))

	os.system('fusermount -u /storage/s3fsnc/')
	time.sleep(1)
