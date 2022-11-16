import os
import time
class library():

    def __init__(self,booklist,lname):
        self.books=booklist
        self.lname=lname
    def addbook(self):
        last_key=list(self.books.keys())[-1]
        username=input("Enter your name\n")
        book_name=input("Enter a book name\n")
        print(f"{book_name} successfully added by {username}")
        self.books[last_key+1]=book_name

    def showbook(self):
        print(f"Welcome to {self.lname} Library")
        i=1
        for i in (self.books):
            print(f"{i} : {self.books[i]}")
            
        # return self.books

    
    user_lender={}

    def lendbook(self):
        self.showbook()
        print("Chose the book number that you want to lend")
        user=input("Enter your Name\n")
        lend_num=int(input("Enter a book number"))
        if lend_num in self.books.keys():
            print(f"{self.books[lend_num]} book aloted to {user}")
            self.user_lender[user]=self.books[lend_num]
            self.books.pop(lend_num)


            # print("test123")

        # self.showbook()

    def showLender(self):
        if len(self.user_lender)>0:
            for i in self.user_lender:
                print(f"{self.user_lender[i]} lended by {i}")
        
        else:
            print("There is no history of book lend")
        # print("test123")

        
    
shivay=library({101:"C++",102:"Java script"},"Shivay")
def main():
    while True:
        print("Option 1 . press 1 for show book")
        print("Option 2 . press 2 for add book")
        print("Option 3 . press 3 for lend book")
        print("Option 4 . press 4 for check book history")
        
        try:
            keypre=int(input("Please enter Your Choice\n"))
            if keypre==1:
                shivay.showbook()
            elif keypre==2:
                shivay.addbook()
            elif keypre==3:
                shivay.lendbook()
            elif keypre==4:
                shivay.showLender()
            else:
                pass
        except:
            print("Please Enter 1,2,3,4\n")
            pass
        print("Press C for continue and Q for quit")
        time.sleep(1)
        # os.system('cls')
        bree=input("Enter any key\n")
        if bree=='q':
            exit()
        elif bree=='c':
            pass

if __name__=="__main__":
    
    main()
