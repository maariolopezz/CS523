import time
import os
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(1)

	tinit = time.time()
	for x in range(100):
		os.system("dd if=/storage/goofysS3/goofys/testfile-" + str(x) + ".txt of=/dev/null bs=1MB count=1 oflag=nocache iflag=nocache status=none")

	lapse =  time.time() - tinit

	with open('./stats/goofysReadMany.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(1)
