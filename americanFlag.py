counter1 = 0
counter2 = 0
star = "*"
minus = "-"
voidString = ""


# Stampo le prime linee della bandiera con le stelle

while counter1 < 5:
    line = voidString
    counter2=0
    while counter2 < 7:
        line+=star
        counter2+=1
    while counter2 < 20:
        line+=minus
        counter2+=1
    print(line)
    counter1+=1

# Stampo le successive linee della bandiera senza stelle
while counter1 < 10:
    line = voidString
    counter2=0
    while counter2 < 20:
        line+=minus
        counter2+=1
    print(line)
    counter1+=1