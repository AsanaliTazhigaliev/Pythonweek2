a=str(input("Enter the text: "))
a=list(a)
b=0
a[0]="A"
for i in range(len(a)):
    if a[i]==" ":
        a[i+1]="A"
print(a)