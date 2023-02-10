import time
import numpy as np
import sys
import os

from functions import test, minimumSupport,get__allItems_with_first_count,get_frequent,joinItemset

class Apriori: 
    
    initialiZations=sys.argv
    fileName = initialiZations[1]
    initalPercentage = int(initialiZations[2])
    Transactions = []
    c={}
    l={}
    discarded_transactions={} 
    supportCount  = {}
    totalSize=1
    directoryName = os.getcwd() + '/'+ fileName  
    directoryName = directoryName.replace("\\",'/') 
    print()
    print('hello I am alive')
    print('Please wait...')
    # reading the trasactions
    Transactions,totalRows=test(directoryName)
    
    #  counting the minimum threshold 
    threshold = minimumSupport(totalRows,initalPercentage)
    print('Minimum_Support',threshold)
    start = time.time()

    # received all the unique transactions
    sortedOrder = sorted(get__allItems_with_first_count(Transactions),key=int)
    # print(sortedOrder)
    c.update({1 : [[item] for item in sortedOrder] })
    discarded_transactions.update({1:[]})


    # Check and count the values for the first time
    receivedL,receiveditemCount,receivedDiscarededValue  =  get_frequent(c[1],Transactions,threshold,discarded_transactions)
    
    l.update({1:receivedL})
    supportCount.update({1:receiveditemCount})
    discarded_transactions.update({1:receivedDiscarededValue})

    totalSize = 1 + totalSize
    noMoreItems = False
    while noMoreItems == False:
        print('Almost there :)')

        joinedSet = joinItemset(l[totalSize-1],sortedOrder)
       
        c.update({totalSize:joinedSet})
        receivedL,receiveditemCount,receivedDiscarededValue = get_frequent(c[totalSize],Transactions,threshold,discarded_transactions)
        discarded_transactions.update({totalSize:receivedDiscarededValue})
        supportCount.update({totalSize:receiveditemCount})

        if len(receivedL) <1:
            noMoreItems = True
            print('Thanks for your patience')
        else: 
            l.update({totalSize:receivedL})
            totalSize = totalSize+1 
    totalSize = 0   
    
    end = time.time()

    from contextlib import redirect_stdout

    with open('out.txt', 'w') as f:
        with redirect_stdout(f):
         
             for index in range(1, len(l.keys())+1):
                print(str(l[index]))
                totalSize = totalSize + len(l[index])
             print('FPS:',totalSize)
             print('Time', end-start)



    
