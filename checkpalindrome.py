from sys import stdin


def isPalindrome(string) :
    n = len (string)
    for i in range (0 , int(n/2)):
        if string[i] != string[n-i-1]:
            return False
    return True
    
     
        
#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

