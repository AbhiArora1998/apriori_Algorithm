from turtle import update

"""
       Reading the file from the dataPath mentioned in the terminal 
       PreProcessing the file to start reading the file from items 
"""
def readingFile(dataPath):

    resultedFile= list()
    totalRows = 0
    with open(dataPath) as f: 
        lines = f.readlines()
    for line in lines: 
        if totalRows==0:
            totalRows=line
        else:  
            line = line.split("\t")
            updatedFile = line
            updatedFile = updatedFile[2]
            updatedFile = updatedFile.replace('\n','')
            updatedFile = updatedFile.split()
            resultedFile.append(updatedFile)
    return resultedFile, totalRows

"""
    Counting the minimum Threshold or support when user informs us with the percentage he/she would like
"""
def minimumSupport(totalRows,percentage):
    minimum_confidence_percent = percentage
    return (int(totalRows)*minimum_confidence_percent)/100

"""
    This is being used to count all the items uniquely for the first loop 
    This is being done to reduce the time complexity 
    All the values are being mapped and then are being counted using the library counter
"""
def get__allItems_with_first_count(Transactions):
    from collections import Counter
    totalRowsCounter=0
    totalItems = Counter()
   
    for line in Transactions:
        if totalRowsCounter==0:
            totalItems=(Counter(line))
        else:
            totalItems=(Counter(line)) + totalItems
        totalRowsCounter = totalRowsCounter+1
    
    totalItems=dict(totalItems)
    totalItems = list(totalItems.keys())
    return totalItems
"""
        This counts the rest of the values by checking if the given item exist in the transactions
"""

def item_counter(singleItemSet, Transactions):
    incremente_count = 0
    for i in range(len(Transactions)):
        if set(singleItemSet).issubset(set(Transactions[i])):
            incremente_count = incremente_count+1
    return incremente_count

"""
    This function checks finds all the items and checks if it subset of discarded items 
    If it is then ignore the items. Else count the amount of times it was repeated and send items back which are above threshold
"""

def get_L_and_itemCount_and_discarded_items(itemSet, initialTransactions, threshold,discarded_transactions):
    tempL,newDiscardedValue,itemCount = list(),list(),list()
     
    for i in range(len(itemSet)):
        isDiscarded = False
        if len(discarded_transactions.keys()) > 0:
            for k in discarded_transactions[len(discarded_transactions.keys())]:
                
                if set(k).issubset(set(itemSet[i])):
                    isDiscarded = True
                    break
        if isDiscarded == False:
            itemCounter = item_counter(itemSet[i],initialTransactions)
            if itemCounter >= threshold:
                tempL.append(itemSet[i])
                itemCount.append(itemCounter)
            else:
                newDiscardedValue.append(itemSet[i])

    return tempL,itemCount,newDiscardedValue

"""
    This checks if the two items have anything in common neglect it 
    They are not and we have all the items sorted 
    therefore check if the last index is greater than the previous one 
    then join that item 
"""
def inner_combine_sets(firstItem,secondItem,sortedOrder):
    lastIndex = -1
    for index in range(len(firstItem)):
        if firstItem[index] == secondItem[index]:
            return list()
    if sortedOrder.index(firstItem[lastIndex]) < sortedOrder.index(secondItem[lastIndex]):    
            return firstItem + [secondItem[lastIndex]]

    return list()

"""
    if the length of combined result from the inner_combine_sets function is greater than one and is not already in our list 
    add it and otherwise ignore it 
"""
def combineItems(items,initialItem):
    tempC = list()
    for index in range(len(items)-1):
        for innerIndex in range(index+1,len(items)):
            combinedResult = inner_combine_sets(items[index],items[innerIndex],initialItem)
            if len(combinedResult)>0 and combinedResult not in tempC:
                tempC.append(combinedResult)

    return tempC
            
        