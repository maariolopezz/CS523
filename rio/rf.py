import time
import os
import csv

for y in range(10):

        os.system('rm -rf /tmp/riofs/*')
        os.system('(echo 3 | sudo tee /proc/sys/vm/drop_caches) > /dev/null')
        os.system('sudo riofs -c ~/.config/riofs/riofs.conf.xml -o direct_io mariomediabucket /storage/riofsS3nc')
        time.sleep(1)


        tinit = time.time()
        for x in range(10):
                os.system("dd if=/storage/riofsS3nc/riofs/tesFileLarge-" + str(x) + " of=/dev/null bs=1 count=1 oflag=nocache iflag=nocache status=none")

        lapse =  time.time() - tinit
        with open('./stats/rioReadFirst.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([lapse])

        print("riofs: " + str(lapse))

        os.system('fusermount -u /storage/riofsS3nc/')
        time.sleep(1)
