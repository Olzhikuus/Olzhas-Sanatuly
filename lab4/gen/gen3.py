
def div(n):
    for i in range(0,n):
        if i % 3== 0 and i % 4 ==0:
            yield i
n = div(int(input("Enter a num:")))
print(*n)
