a=str(input("Write a text: "))
b=0
list(a)
for i in range(len(a)):
    if a[i]=="a":
        a.replace("a","o")
        b+=1
print(str(b),"amount of replacement")
print(len(a.replace(' ','')),"amount of characters")