def mergeSort(a):
    if(len(a)==1):
        return a
    elif(len(a)==2):
        if(a[0]<a[1]):
            return a
        else: return [a[1], a[0]]
    else:
        splitPoint=len(a)//2
        topSortedArr=mergeSort(a[0:splitPoint])
        bottomSortedArr=mergeSort(a[(splitPoint):len(a)])
        i,j=0,0
        mergedArr=[]

        # Merging Sorted Sub-Arrays
        while(1):
            if(i>=len(topSortedArr)):
                mergedArr.extend(bottomSortedArr[j:len(bottomSortedArr)])
                break
            if(j>=len(bottomSortedArr)):
                mergedArr.extend(topSortedArr[i:len(topSortedArr)])
                break
            if(topSortedArr[i]<bottomSortedArr[j]):
                mergedArr.append(topSortedArr[i])
                i=i+1
            else:
                mergedArr.append(bottomSortedArr[j])
                j=j+1
        return mergedArr
                    
# TESTING
inpArr=[5,4,6,2,9,3,1]
print(mergeSort(inpArr))