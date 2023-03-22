import datetime
import os

class LMS:
    def __init__(self,listOfBooks='LibraryBooks.txt',libraryName="People's Library"):
        self.listOfBooks='LibraryBooks.txt'
        self.libraryName=libraryName
        self.booksDict={}
        self.Id=101
        with open (self.listOfBooks) as bk:
            content=bk.readlines()
        for line in content:
            self.booksDict[self.Id]={'BooksTitle':line.replace('\n',''),'LenderName':'','IssueDate':'','Status':'Available'}
            self.Id+=1
    
    
    def displayBooks(self):
        print('<-------------------------List Of Books--------------------------------------------->')
        print("Id           BookTitle               Status")
        for i in self.booksDict:
            print(i,'   ',self.booksDict[i]['BooksTitle'],'     ',self.booksDict[i]['Status'])
    def issueBooks(self):
        bookId=int(input('Entee the book Id:'))
        currentDate=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if bookId in self.booksDict:
            if self.booksDict[bookId]['Status']=='issued':
                print('The Book is Already issued to another person')
            else:
                yourName=input("Please ... Enter your name")
                self.booksDict[bookId]['LenderName']=yourName
                self.booksDict[bookId]['Status']='issued'
                self.booksDict[bookId]['IssueDate']=currentDate
                print('Book is Issued Successfully')
        else:
            print("The book you needed is not avilable in peoples library")
    def addBooks(self):
        newBook=input("Enter the title of the book:")
        if len(newBook)>20:
            print('Length of the title does not exceed 20 characters')
        else:
            with open(self.listOfBooks,'a') as bk:
                bk.writelines(newBook+'\n')
                self.booksDict[self.Id]={'BooksTitle':newBook.replace('\n',''),'LenderName':'','IssueDate':'','Status':'Available'}
                self.Id+=1
                print('The Book is Added SuccessFully')
    def returnBooks(self):
        bookId=int(input('Enter the book id to return'))
        if self.booksDict[bookId]['Status']=='Available':
            print('The Book is Already exists. Check the Book ID')
        else:
            self.booksDict[bookId]['LenderName']=''
            self.booksDict[bookId]['IssueDate']=''
            self.booksDict[bookId]['Status']='Available'
            print('The Book is Returned Scuccessfully')
try:
    obj=LMS()
    while True:
        pressList={'a':'ToAddBooks','i':'IssuingBooks','r':'ReturningBooks','d':'DisplayingBooks','e':'Exit'}
        keyPress=False
        for i in pressList:
            print(i+' For '+pressList[i])
        keyPress=input('Enter your choice')
        if keyPress=='i':
            print('Current Section is Issuing books')
            obj.issueBooks()
        elif keyPress=='a':
            print('Current Section is Adding books')
            obj.addBooks()
        elif keyPress=='r':
            print('CurrentSection is Returning Books')
            obj.returnBooks()
        elif keyPress=='d':
            print('CurrentSection is Displaying Books')
            obj.displayBooks()
        elif keyPress=='e':
            break
        else:
            print('Entered key is Invalid')
except Exception as e:
    print(e)