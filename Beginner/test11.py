x = list(input("give input: ")) #['1','2','3','4,'5']
y = list()
for i in x:
    i = int(i)
    y.append(i)
print(y)
while len(y) > 1:
    total = sum(y) #12345
    y = [int(digit) for digit in str(total)]
print(y[0])
