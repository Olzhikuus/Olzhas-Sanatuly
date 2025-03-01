def squares(start, end):
    for i in range(start,end+1):
        yield i**2
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(*squares(a,b))
print("Test with for:")
for j in squares(a,b):
    print(j, end=" ")