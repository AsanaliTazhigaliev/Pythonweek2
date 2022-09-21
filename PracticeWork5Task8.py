a=str(input("Write a text: "))
b=0
list(a)
for i in range(len(a)):
    if a[i]==" ":
        b+=1
print(str(b+1),"amount of words")