import threading 
import time
import os
import csv
import subprocess


def writeFile(x_write): 

	comm = "dd if=/dev/zero of=/storage/3rclone/rclone/tesFileLarge-" + str(x_write) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	os.system(comm)


def readFile(x_read): 
    
	comm = "dd if=/storage/3rclone/rclone/tesFileLarge-" + str(x_read) + " of=/dev/null bs=1MB iflag=nocache oflag=nocache status=none"
	os.system(comm)


for x in range(10):

	os.system('rm -rf /root/.cache/rclone/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo rclone mount --cache-chunk-no-memory --vfs-cache-mode off s3-rclone-bucket:mariomediabucket /storage/3rclone &')
	
	time.sleep(5)


	tinit = time.time()


	writer1 = threading.Thread(target=writeFile, args=(0,)) 
	writer2 = threading.Thread(target=writeFile, args=(1,))
	writer3 = threading.Thread(target=writeFile, args=(2,))
	writer4 = threading.Thread(target=writeFile, args=(3,))
	writer5 = threading.Thread(target=writeFile, args=(4,))

	reader1 = threading.Thread(target=readFile, args=(5,)) 

	writer1.start() 
	writer2.start()
	writer3.start()
	writer4.start()
	writer5.start()

	reader1.start()

	writer1.join() 
	writer2.join()
	writer3.join()
	writer4.join()
	writer5.join()

	reader1.join() 

	lapse =  time.time() - tinit
	with open('./stats/rcloneConc5w1r.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("rclone: " + str(lapse))


	result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)
	while result > 150:
		print('ps -eaf | grep rclone')
		time.sleep(7)
		result = len(subprocess.run(['ls', '-la', '/storage/3rclone'], stdout=subprocess.PIPE).stdout)

	time.sleep(1)




