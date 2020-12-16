import time
import os
import csv

for y in range(10):

	os.system('rm -rf /tmp/riofs/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	time.sleep(1)

	tinit = time.time()
	for x in range(100):
		os.system("dd if=/storage/riofsS3nc/riofs/testfile-" + str(x) + ".txt of=/dev/null bs=1MB count=1 oflag=nocache iflag=nocache status=none")

	lapse =  time.time() - tinit

	with open('./stats/rioReadMany.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("riofs: " + str(lapse))

	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(1)
