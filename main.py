class Shivaylb():
    def __init__(self,list,Lname):
        self.booklist=list
        self.Lname=Lname

    def addbook(self):
        num=int(input("Enter the number of books that you want to insert\n"))
        for i in range(num):
            book=input("Enter a book name")
            self.booklist.append(book)
        print(self.booklist)
    
    def displaybook(self):
        print("Welcome to the {} Library \n".format(self.Lname))
        print(self.booklist)

    def lenbook(slef,username):
        pass

rohan=Shivaylb(["python","javascript"],"shivay")

def main():
    print("press 1 for enter a book")
    print("Press 2 for show boook")
    
    a=int(input("Enter the number"))
    if a==2:
        rohan.displaybook()
    if a==1:
        rohan.addbook()
   
    


if __name__=="__main__":
    while True:
        main()
        print("Press q for quit and c for continue")
        b=input("Enter a key")
        if b=='q':
            break
        else:
            pass