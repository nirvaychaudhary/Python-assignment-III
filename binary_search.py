#Binary Search

pos =-1
mylist = [12, 5, 11, 9, 3, 7, 10, 4, 1]
newlist = sorted(mylist)
num = int(input("Enter any num to search: "))

def binarysearch(newlist, n):
    lowerbound = 0
    upperbound = len(newlist)-1

    while lowerbound <= upperbound:
        mid = (lowerbound + upperbound)// 2
        
        if newlist[mid] == n:
            globals() ['pos'] = mid
            return True

        else:
            if newlist[mid] < n:
                lowerbound = mid+1

            else:
                upperbound = mid-1

    return False


if binarysearch(newlist, num):
    print("found at ", pos + 1)

else:
    print("Not Found")

    

