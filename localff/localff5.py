import time
import os
import csv

for y in range(5):

	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')

	tinit = time.time()
	os.system("ffmpeg -r 60 -start_number 874 -i \"/home/centos/movedFiles/Timelapse/parte-1/DSC09%03d.JPG\" -c:v libx264 -b:v 25000k -vf scale=1920:1080 -framerate 60 /home/centos/movedFiles/sTimel2.mp4 -loglevel fatal")
	lapse =  time.time() - tinit

	with open('./stats/localff5.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])

	print("local: " + str(lapse))
	os.system('rm -rf /home/centos/movedFiles/sTimel2.mp4')
	time.sleep(1)
