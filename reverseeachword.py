def reverseEachWord(string) :
	# Your code goes here
    words = string.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence   
    

    #main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
