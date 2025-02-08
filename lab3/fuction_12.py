def histogram(gist):
    i = 0
    while i < len(gist):
        j = 0
        while j < gist[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

gist = input()
gist = gist.split()
gist = [int(num) for num in gist]
histogram(gist)