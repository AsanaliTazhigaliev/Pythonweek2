a=str(input("Write a text: "))
b=0
list(a)
for i in range(len(a)):
    if a[i]=="a":
        a.replace("a","")
        b+=1
print(str(b), "amount of removed")