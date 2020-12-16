import time
import os
import csv

for y in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	time.sleep(1)

	tinit = time.time()
	os.system("ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 /home/centos/movedFiles/C0001-HD.MP4")
	os.system("ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 /home/centos/movedFiles/C0002-UHD.MP4")
	os.system("ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 /home/centos/movedFiles/C0003-UHD.MP4")
	os.system("ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 /home/centos/movedFiles/C0005-UHD.MP4")
	lapse =  time.time() - tinit

	with open('./stats/localff3.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("local: " + str(lapse))

	time.sleep(1)
