from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    chars =[]
    for i in string:
        if i != ch:
            chars.append(i)
            i = ch
    return ''.join(chars)


string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
