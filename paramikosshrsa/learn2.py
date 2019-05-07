#!/usr/bin/env python3

import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

# x = commandissue('ls')

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

our_commands = ['touch sshworked.txt', 'touch file3.txt', 'touch create.txt', 'ls']
#our_commands = our_commands.get()

for x in our_commands:
   # print(commandissue(x))
   print(commandissue(x).decode('utf-8'))

