import time
import os
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')
	time.sleep(3)

	tinit = time.time()

	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/goofysS3/Test\ Media/C0001-HD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/goofysS3/Test\ Media/C0002-UHD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/goofysS3/Test\ Media/C0003-UHD.MP4")
	os.system("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 /storage/goofysS3/Test\ Media/C0005-UHD.MP4")
	lapse =  time.time() - tinit

	with open('./stats/goofysff2.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(2)
