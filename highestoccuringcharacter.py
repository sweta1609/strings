from sys import stdin

ASCII_SIZE = 256
def highestOccuringChar(string) :
	#Your code goes here
    count = [0]* ASCII_SIZE
    max = -1
    c = ''
    for i in string:
        count[ord(i)]+= 1;
    for i in string:
        if max< count [ord(i)]:
            max = count [ord(i)]
            c = i
    return c
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
