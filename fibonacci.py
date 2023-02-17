def fibonacci(prev1, prev2, stop, times,myList):
    if times >= stop:
        myList.append(prev1+prev2)
        return prev1+prev2
    else:
        times+=1
        myList.append(prev1+prev2)
        return fibonacci(prev1+prev2,prev1,stop,times,myList)


myList = []
counter = 99
fibonacci(0,1,20,0,myList)
print("My fibonacci serie: ")
print(myList)