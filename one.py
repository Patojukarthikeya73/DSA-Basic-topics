'''program to check wheather the give string is palindrome or not and count the palandromic characters which are repeated 
str=madam
output:{'m':2,'a':2,'d':1}
str=malayalam'''

text=input("enter the name:")
if text==text[::-1]:
  print("palindrome")
else:
  print("text")
freq={}
for i in text:
    freq[i]=freq.get(i,0)+1
    print(freq)
