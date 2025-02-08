def reverse(s): 
   res = "" 
   for word in s.split(" "): 
        res = word + " " + res 
   return res
c=str(input())
print(reverse(c))