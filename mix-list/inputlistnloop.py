#!/usr/bin/env python3
def main():
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        # append
        #rstrip
        #split
        #the results
        networklists.append(sline.rstrip("\n").split(' '))
        print(networklists) 
        for driveandip in networklists:
            print('SSH to ' + driveandip[1] + ' using driver ' +driveandip[0])

            main()

