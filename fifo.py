#!/usr/bin/env python
import sys
from collections import deque

if __name__ == '__main__' :
    print
    print "\t\t*****CREATING QUEUE****"
    print

    new_queue = deque ([])
    while True:
        print "\t 1. Push a number. "
        print "\t 2. Pop a number. "
        print "\t 3. Imprimir cola. "
        print "\t 4. Exit. "
        stop = int( raw_input (" :: "))

        if stop == 1 :
            to_insert = int( raw_input (" \nNumber to insert? "))
            new_queue.append(to_insert)
            print "\n\n"

        elif (stop == 2):
            if not new_queue :
                print "The queue is empty "
                sys.exit("Abort\n\n")
            else :
                print new_queue.popleft()
        
        elif (stop == 3):
            if not new_queue :
                print "The queue is empty \n\n"
            else :
                print new_queue
            
        else :
            break
    
