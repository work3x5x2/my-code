#!/usr/bin/env python3

import os
import paramiko

t = paramiko.Transport("10.10.2.3", 22) #ip and port
t.connect(username="bender", password='alta3')

sftp = paramiko.SFTPClient.from_transport(t)

for x in os.listdir("/home/student/filestocopy/"):
    if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything else
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move files

sftp.close()
