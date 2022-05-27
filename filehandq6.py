def program3():
    with open("MyFile.txt","r") as f1:
       data=f1.read()
    with open("intro.txt","r") as f2:
        data1=f2.read()
    with open("merge.txt","w") as f3:
        f3.write(data)
        f3.write(data1)
