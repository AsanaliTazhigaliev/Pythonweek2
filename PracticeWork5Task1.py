a=str(input("Write a string containing Russian text: "))
print(a.split(' '))
b=0
if a[0]=='е':
    b+=1
for i in range(len(a)-1):
    if a[i]==' ':
        if a[i+1]=='е':
            b+=1
    i+=1
print(str(b),"number of words beginning with the letter 'e'")
