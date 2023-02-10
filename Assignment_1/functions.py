from turtle import update


def test(dataPath):

    resultedFile= []
    totalRows = 0
    print(dataPath)
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
            # print(updatedFile)
    return resultedFile, totalRows

def minimumSupport(totalRows,percentage):
    minimum_confidence_percent = percentage
    return (int(totalRows)*minimum_confidence_percent)/100

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

def count_item(singleItemSet, Transactions):
    counter = 0
    for i in range(len(Transactions)):
        if set(singleItemSet).issubset(set(Transactions[i])):
            counter = counter+1
    return counter

def get_frequent(itemSet, initialTransactions, threshold,discarded_transactions):
    tempL = []
    newDiscardedValue = []
    itemCount = []
    for i in range(len(itemSet)):
        isDiscarded = False
        if len(discarded_transactions.keys()) > 0:
            for k in discarded_transactions[len(discarded_transactions.keys())]:
                
                if set(k).issubset(set(itemSet[i])):
                    isDiscarded = True
                    break
        if isDiscarded == False:
            itemCounter = count_item(itemSet[i],initialTransactions)
            if itemCounter >= threshold:
                tempL.append(itemSet[i])
                itemCount.append(itemCounter)
            else:
                newDiscardedValue.append(itemSet[i])

    return tempL,itemCount,newDiscardedValue

def join_two_itemsets(firstItem,secondItem,sortedOrder):
    # firstItem.sort(key=lambda y: sortedOrder.index(y))
    # secondItem.sort(key=lambda j: sortedOrder.index(j))

    for i in range(len(firstItem)):
        # print(firstItem[i],secondItem[i],'comparing')
        if firstItem[i] == secondItem[i]:
            return []
    # print(sortedOrder.index(firstItem[-1]), sortedOrder.index(secondItem[-1]),sortedOrder.index(firstItem[-1])< sortedOrder.index(secondItem[-1]))
    if sortedOrder.index(firstItem[-1]) < sortedOrder.index(secondItem[-1]):
            
            # print(firstItem + [secondItem[-1]],'joining')
            return firstItem + [secondItem[-1]]

    return []

def joinItemset(items,initialItem):
    tempC = []
    for i in range(len(items)-1):
        for j in range(i+1,len(items)):
            # print('sending',items[i],items[j],initialItem)
            itOut = join_two_itemsets(items[i],items[j],initialItem)
            if len(itOut)>0 and itOut not in tempC:

                tempC.append(itOut)

    # print('getting out ')
    return tempC
            
        