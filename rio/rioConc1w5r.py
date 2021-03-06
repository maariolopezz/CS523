import threading 
import time
import os
import csv



def writeFile(x_write): 

	comm = "dd if=/dev/zero of=/storage/riofsS3nc/riofs/tesFileLarge-" + str(x_write) + " bs=1MB count=2000 oflag=nocache iflag=nocache status=none"
	os.system(comm)


def readFile(x_read): 
    
	comm = "dd if=/storage/riofsS3nc/riofs/tesFileLarge-" + str(x_read) + " of=/dev/null bs=1MB iflag=nocache oflag=nocache status=none"
	os.system(comm)


for x in range(10):

	os.system('rm -rf /tmp/riofs/*')
	os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
	os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
	
	time.sleep(1)


	tinit = time.time()


	writer1 = threading.Thread(target=writeFile, args=(0,)) 

	reader1 = threading.Thread(target=readFile, args=(5,)) 
	reader2 = threading.Thread(target=readFile, args=(6,)) 
	reader3 = threading.Thread(target=readFile, args=(7,)) 
	reader4 = threading.Thread(target=readFile, args=(8,)) 
	reader5 = threading.Thread(target=readFile, args=(9,)) 

	writer1.start() 

	reader1.start()
	reader2.start()
	reader3.start()
	reader4.start()
	reader5.start()

	writer1.join() 

	reader1.join() 
	reader2.join() 
	reader3.join() 
	reader4.join() 
	reader5.join() 

	lapse =  time.time() - tinit
	with open('./stats/rioConc1w5r.csv', 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([lapse])
	print("riofs: " + str(lapse))

	os.system('fusermount -u /storage/riofsS3nc/')
	time.sleep(1)




