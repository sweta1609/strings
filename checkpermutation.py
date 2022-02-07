rom sys import stdin

NO_OF_CHARS = 256
def isPermutation(string1, string2) :
	#Your code goes here

    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for i in string1:
        count1[ord(i)] += 1
    for i in string2:
        count2[ord(i)] += 1

    if (len(string1) != len(string2)):
        return False
    for i in range(NO_OF_CHARS):
        if (count1 != count2):
            return False
    return True
























	


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

