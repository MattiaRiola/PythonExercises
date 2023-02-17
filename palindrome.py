#  tell if a word is palindrome

counter1 = 0
counter2 = 0
word = "anna"
lenght = len(word)
lastArrayIndex = lenght-1
i = 0
isPal = True
while i < lenght/2:
    charSx = word[i]
    charDx = word[lastArrayIndex-i]
    if charSx != charDx:
        isPal = False
    i+=1

if isPal:
    print(word + " is palindrome!!!")