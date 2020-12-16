import time
import os
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(1)

	tinit = time.time()

	for x in range(y*100+1,(y+1)*100+1):
		os.system("dd if=/storage/goofysS3/Test\ Media/Timelapse/parte-2/DSC00" + str(x).zfill(3) + ".JPG of=/dev/null bs=1 count=1 iflag=nocache oflag=nocache status=none")
	lapse =  time.time() - tinit

	with open('./stats/goofysReadFirst.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(1)
