def program8():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       data = f1.read()
       data=data.replace(' ','-')
    with open("merge.txt","w") as f1:
        f1.write(data)
