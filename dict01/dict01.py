#!/usr/bin/env python3

def main():

    ## create Dic
    switch = {'hostname' : 'sw1', 'ip' : '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}


    ##Display stuff
    print( switch['hostname'])
    print( switch['ip'])


    ## Request fake?

    #print( switch['lynx'])

    ## Request a'fake' key with .get() method
    print("First test - .get()")
    print( switch.get('lynx'))

    print("Second test - .get()")
    print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

    print( "Third test -get.()")
    print( switch.get('version'))

    print( "Forth test - .keys()")
    print( switch.keys() )
    
    print( "Fifth test - .values()")
    print( switch.values() )

    print( "Sixth test - .pop()")
    switch.pop('version') #comment here
    print( switch.keys()) #notice gone
    print(switch.values())# no 1.2 

    print ( "Seventh test - ADD a new value")
    switch['adminlogin'] = 'karl08'
    print( switch.keys())
    print( switch.values())

    print( "Eigth test- ADD a new value")
    switch['password'] = 'qwerty'
    print( switch.keys())
    print( switch.values())

    

main()

