# quick sort
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

m=0
def quicksort(myList, start, end):
    global m
    if start < end:
        # partition the list
        m+=end-start
        split = partition(myList, start, end)
        # sort both halves
        m+=abs(start-(split-1))
        quicksort(myList, start, split-1)
        m+=abs((split+1)-end)
        quicksort(myList, split+1, end)
    return myList




#####austin quicksort
'''
def partition(myList, start, end):
    pivot = myList[start]#this is the leftmost part of the array
    print("pivot!", pivot)
    i = start+1 #the barrier between the sorted and what is not sorted
    j = start # the index of the pivot
    right = end #iterate through what should eb checked ans sorted

    finished=False
    while right>j:
        print("compare", pivot, myList[right], right, j)
        if myList[right]<pivot:
             myList = myList[:start] + [myList[right]] + myList[start:]
             del myList[right+1]
             right+=1
             
             
                if right!=len(myList)-1:
                    myList = [myList[:j]] + [myList[right]]+ [myList[j]] + [myList[j+1:right]] + [myList[right+1:]]
                else:
                    myList = myList[:j] + [myList[right]] + [myList[j]] + [myList[j+1:right]]
            
             j+=1
        right-=1
        print(myList)
    return j

def quicksort(myList, start, end):
    if end>start:
        split = partition(myList, start, end)

        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList


'''


def main():
    myList = [int(x) for x in open("list.txt", "r").readlines()]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
main()
print(m)




        
