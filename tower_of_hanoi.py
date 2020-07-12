# i) Tower of Hanoi problem for ‘n’ number of disks.

def hanoi(n, src, temp, dest):
    if n == 1:
        print("Move disk from %s from %s ---> %s" %(n, src, dest)) 

    else:
        hanoi(n-1, src, dest, temp)
        print("Move disk from %s from %s ---> %s" %(n, src, dest))
        hanoi(n-1, temp, src, dest)

    return "Given num is %s" %(n)    
src = 'source'
temp= 'temporary'
dest = 'destination'
n = int(input("Enter any number to solve from tower of Hanoi: "))
print(hanoi(n, src, temp, dest))