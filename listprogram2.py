n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    x = int(input("Enter the element: "))
    l.append(x)

uq = []
for i in l:
    if i not in uq:
        uq.append(i)

print(uq)