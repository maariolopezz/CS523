import time
import os
import csv

for y in range(10):

	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')

	comm = "aws s3 cp " + "mylargeFile-" + str(y) + " s3://mariomediabucket/native/tesFileLarge-" + str(y)

	tinit = time.time()

	os.system(comm)
	lapse =  time.time() - tinit
	with open('./stats/nativeWriteLarge.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("native: " + str(lapse))

	time.sleep(1)
