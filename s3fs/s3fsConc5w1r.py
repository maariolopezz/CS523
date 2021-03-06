import threading 
import time
import os
import csv



def writeFile(x_write): 

	comm = "dd if=/dev/zero of=/storage/s3fsnc/s3fs/tesFileLarge-" + str(x_write) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	os.system(comm)


def readFile(x_read): 
    
	comm = "dd if=/storage/s3fsnc/s3fs/tesFileLarge-" + str(x_read) + " of=/dev/null bs=1MB iflag=nocache oflag=nocache status=none"
	os.system(comm)


for x in range(10):

	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo s3fs mariomediabucket /storage/s3fsnc -o passwd_file=/home/centos/.passwd-s3fs -o direct_io -o del_cache')
	
	time.sleep(1)


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
	with open('./stats/s3fsConc5w1r.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("s3fs: " + str(lapse))

	os.system('fusermount -u /storage/s3fsnc/')
	time.sleep(1)
