import time
import os
import csv

for y in range(10):

	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')

	tinit = time.time()
	os.system("aws s3 cp s3://mariomediabucket/native ./smallFiles --recursive")
	lapse =  time.time() - tinit
	with open('./stats/nativeReadMany.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("native: " + str(lapse))

	time.sleep(1)
