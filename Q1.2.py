accName=input("Enter name of the customer")
f= open ("account.txt","r")
while (f.readline()):
    data=list(f.readline().split("|"))
    print("Name:[ ]".format(data[1]))
f.close()
