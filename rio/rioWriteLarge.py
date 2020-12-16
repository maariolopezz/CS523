import time
import os
import csv

for x in range(10):
	os.system('rm -rf /tmp/riofs/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	time.sleep(1)

	comm = "dd if=/dev/zero of=/storage/riofsS3nc/riofs/tesFileLarge-" + str(x) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	tinit = time.time()
	os.system(comm)
	lapse =  time.time() - tinit

	with open('./stats/rioWriteLarge.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("riofs: " + str(lapse))

	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(1)
