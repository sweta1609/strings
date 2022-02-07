from sys import stdin

def removeConsecutiveDuplicates(string) :
    chars = []
    prev = None
 
    for i in string:
        if prev != i:
            chars.append(i)
            prev = i
 
    return ''.join(chars)
#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
