import time
import os
import csv

for x in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(1)

	comm = "dd if=/dev/zero of=/storage/goofysS3/goofys/tesFileLarge-" + str(x) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	tinit = time.time()
	os.system(comm)
	lapse =  time.time() - tinit
	with open('./stats/goofysWriteLarge.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(1)
