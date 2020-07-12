#linear search
pos = -1
mylist = [5,2,7,9,3,8,4]
newlist = sorted(mylist)
n = int(input("Enter number to search in list: "))

def search(newlist, n):
    i = 0

    for i in newlist:
        if i<len(newlist):
            if newlist[i] == n:
                globals()['pos'] = i
                return True
    print(newlist)

if search(newlist, n):
    print("Found ", pos+1)

else:
    print("Not Found")