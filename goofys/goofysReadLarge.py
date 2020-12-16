import time
import os
import csv

for y in range(10):
	
	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(1)

	tinit = time.time()
	os.system("dd if=/storage/goofysS3/goofys/tesFileLarge-" + str(y) + " of=/dev/null bs=1MB oflag=nocache iflag=nocache status=none")

	lapse =  time.time() - tinit

	with open('./stats/goofysReadLarge.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(1)
