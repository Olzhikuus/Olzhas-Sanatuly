def palindrome(text):
    i = 0
    j = len(text)-1
    while i < len(text)/2:
        if text[i] != text[j]:
            return 'No palindrome'
        i+=1
        j-=1
    return 'palindrome'

text = input()
print(palindrome(text))