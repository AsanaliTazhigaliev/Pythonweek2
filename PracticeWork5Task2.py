a=str(input("Write a text: "))
print(list(a))
b=0
for i in range(len(a)):
    if a[i]==':':
        a.replace(":","%")
        b+=1
print(str(b),"amount of replacement")
