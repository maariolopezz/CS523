import time
import os
import csv

for y in range(10):

	os.system('rm -rf /tmp/riofs/*')
	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	time.sleep(1)
	tinit = time.time()
	for x in range(100):
		os.system("dd if=/dev/zero of=/storage/riofsS3nc/riofs/testfile-" + str(x) + ".txt bs=1MB count=1 oflag=nocache iflag=nocache status=none")

	lapse =  time.time() - tinit
	with open('./stats/rioWriteMany.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("riofs: " + str(lapse))
	if y != 9:
		os.system('rm -rf /storage/riofsS3nc/riofs/testfile-*')
		time.sleep(3)
	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(1)
