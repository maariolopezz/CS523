import threading 
import time
import os
import csv



def writeFile(x_write): 

	comm = "dd if=/dev/zero of=/storage/goofysS3/goofys/tesFileLarge-" + str(x_write) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	os.system(comm)


def readFile(x_read): 
    
	comm = "dd if=/storage/goofysS3/goofys/tesFileLarge-" + str(x_read) + " of=/dev/null bs=1MB iflag=nocache oflag=nocache status=none"
	os.system(comm)


for x in range(10):

	os.system('sync')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo goofys -o allow_other mariomediabucket /storage/goofysS3')

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
	with open('./stats/goofysConc5w1r.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("goofys: " + str(lapse))

	os.system('fusermount -u /storage/goofysS3/')
	time.sleep(1)




