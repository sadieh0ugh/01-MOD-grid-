#Hey Guys it's Connall here and I'm on Sadies computer right now
array = []
for i in range(10):
    if i % 2 == 0:
        line1 = []
        for i in range(10):
            num1 = i % 2
            line1.append(num1)
        array.append(line1)
    elif i % 2 == 1:
        line2 = []
        for i in range(1,11):
            num2 = i % 2
            line2.append(num2)
        array.append(line2)

for i in array:
    line = ""
    for x in i:
        line = line + str(x) + " "
    print(line)




