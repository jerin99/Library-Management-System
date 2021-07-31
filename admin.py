from database import*
from datetime import *
import re

#Admin related activities
class Admin(dB):
    #Default session for admin
    Session = False
    admin_users = [{'Username': 'admin', 'Password': 'admin'},]

    #Admin can add books when this function is called
    def add_books(self):
        if Admin.Session:
            books = {}

            isISBN = True

            book_title = input('Enter book title : ')
            author_name = input('Enter author name : ')
            total_page = int(input('Enter total pages : '))
            available_copy = int(input('Enter number of available copies : '))
            ISBN = int(input('Enter ISBN : '))
            published_year = int(input('Enter pulished year : '))
            if len(str(ISBN))!=13:
                isISBN=False
            else:
                books['book_id'] = dB.book_id+1
                dB.book_id+=1
            if isISBN==True:
                books['book_title'] = book_title
                books['author_name'] = author_name
                books['total_page'] = total_page
                books['available_copy'] = available_copy
                books['ISBN'] = ISBN
                books['published_year'] = published_year

                dB.book_collection.append(books)  
                print('Book added successfully')
            elif isISBN==False:
                print('Please enter a valid ISBN of 13 digits!')
        else:
            print('Please login to add books')

    #Admin can view all books that are in the db
    def view_books(self):
        if Admin.Session:
            books = dB.book_collection
            if len(books):
                for i in range(len(books)):
                    print(books[i]['book_id'], end = "\t")  
                    print(books[i]['book_title'], end = "\t")   
                    print(books[i]['author_name'], end = "\t") 
                    print(books[i]['total_page'], end = "\t") 
                    print(books[i]['available_copy'], end = "\t") 
                    print(books[i]['published_year'], end = "\t") 
                    print("\n")
            else:
                print('There are no books in collection')
        else:
            print('Please login to view books')

    #Admin can edit the books except book id by entering a valid book id
    def edit_books(self):
        if Admin.Session:
            book_id = int(input('Enter book id : '))
            books = dB.book_collection
            for i in range(len(books)):
                if books[i]['book_id'] == book_id:
                    field_chosen = ""
                    isField = True
                    print('Please choose from the following fields-')
                    print('1. Book Title')
                    print('2. Author Name')
                    print('3. Total Pages')
                    print('4. Available Copy')
                    print('5. Published Year')
            
                    field = int(input('Select the field from the above options : '))
                    if field==1:
                        field_chosen = 'book_title'
                    elif field==2:
                        field_chosen = 'author_name'
                    elif field==3:
                        field_chosen = 'total_page'
                    elif field==4:
                        field_chosen = 'available_copy'
                    elif field==5:
                        field_chosen = 'published_year'
                    else:
                        isField = False
                       
                    if isField==True:
                        field_data = input('Enter the data : ')
                        dB.book_collection[i][field_chosen]=field_data
                        print(f'Book id {book_id} has been updated successfully')
                    else:
                        print('Invalid field')
                    break                  
        else:
            print('Please login to edit books')

    #Admin can delete a book by entering a valid book id
    def delete_books(self):
        if Admin.Session:
            book_id = int(input('Enter book id : '))
            books = dB.book_collection
            for i in range(len(books)):
                if books[i]['book_id'] == book_id:
                    del dB.book_collection[i]
                    print(f'Book id {book_id} has been deleted successfully')
                    break              
        else:
            print('Please login to delete books')

    #Admin can create new admins with the help of this function
    def create_admin(self):
        if Admin.Session:
            user = {}
            userName = input('Enter admin username : ')
            passwd = input('Enter admin password : ')
            user['Username'] = userName
            user['Password'] = passwd
            Admin.admin_users.append(user)
            print('Admin has been created successfully')
        else:
            print('Please login to create new admins')

    #Admin can check the requests submitted for books by the users
    def check_request_list(self):
        if Admin.Session:
            reqList = dB.requested_books
            if reqList:
                for i in range(len(reqList)):
                    print(reqList[i]['book_id'], "\t", reqList[i]['email'])
            else:
                print('No new requests')
        else:
            print('Please login to check requested lists')

    #Admin can approve a book which has been requested by the user by entering the correspoding book id
    def approve_book(self):
        if Admin.Session:
            book_id = int(input('Enter book ID to approve : '))
            reqList = dB.requested_books
            users = dB.users_dB
            borrowing_history = dB.users_borrowing_history

            email = ""
            isValidID = True
            isSuccess = False
            borrower_dict = {}
            contact = ""
            name = ""
            today, return_date, days_remaining = "", "", ""
            for i in range(len(reqList)):
                if reqList[i]['book_id']==book_id:
                    email = reqList[i]['email']
                    isValidID = True
                    break
            else:
                print('Invalid book id, Please check the check list')
                isValidID = False

            if isValidID==True:
                for i in range(len(users)):
                    if users[i]['Email']==email:
                        name = users[i]['Name']
                        contact = users[i]['Contact']
                        break
            if isValidID==True:
                for i in range(len(reqList)):
                    if reqList[i]['book_id']==book_id:
                        current_day = date.today()
                        returning_day = current_day+timedelta(15)
                        day = returning_day-current_day
                        days_remaining = day.days


                        today = current_day.strftime("%B %d, %Y")
                        new_date = datetime.today() + timedelta(15)
                        return_date = new_date.strftime("%B %d, %Y")


                        borrower_dict['book_id'] = book_id
                        borrower_dict['email'] = email
                        borrower_dict['contact'] = contact
                        borrower_dict['today'] = today
                        borrower_dict['return_date'] = return_date
                        borrower_dict['days_remaining'] = days_remaining
                        dB.borrower_list.append(borrower_dict)

                        del dB.requested_books[i]
                        print(f'Granted book with ID {book_id} for {name}')
                        isSuccess = True
                        break

            if isSuccess:
                emailDict = {}
                booksDict = {}
                KEY = book_id
                borrowDate = 101
                dueDate = 131
                remaining = 10
                if borrowing_history:
                    for i in borrowing_history:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            innerDictList = innerDict[innerDictKey]
                                            if book_id not in innerDictList:
                                                innerDictList.append(book_id)
                                        innerDict[KEY]=[today, return_date, days_remaining]
                                        break

                else:
                    booksDict['books'] = []
                    emailDict[email] = [booksDict]
                    borrowing_history.append(emailDict)
                    for i in borrowing_history:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            innerDictList = innerDict[innerDictKey]
                                            if book_id not in innerDictList:
                                                innerDictList.append(book_id)
                                        innerDict[KEY]=[today, return_date, days_remaining]
                                        break

        else:
            print('Please login to approve books')

    #Admin can list all the borrowers when this function is called
    def list_borrowers(self):
        if Admin.Session:
            borrower_list = dB.borrower_list
            if borrower_list:
                for i in range(len(borrower_list)):
                    print(borrower_list[i]['book_id'], "\t", borrower_list[i]['email'], "\t", borrower_list[i]['contact'], "\t", 
                    borrower_list[i]['today'], "\t", borrower_list[i]['return_date'], "\t", borrower_list[i]['days_remaining'])
            else:
                print('No pending borrowers in list')
        else:
            print('Please login to check borrowers list')

    #Admin can check all the requests for returning books from the user
    def check_return_book_list(self):
        if Admin.Session:
            book_list = dB.return_book
            if book_list:
                for i in book_list:
                    print(i[0], '\t', i[1], '\t', i[2], '\t')
            else:
                print('There are no new returns')
        else:
            print('Please login to check list of returned books')

    #Admin can confirm the return of a book by enterin the book id.
    #It will also fine automatically based on the returning date
    #Late by one day = Rs. 100
    #Rest days = Rs.10/day
    def accept_return_books(self):
        if Admin.Session:
            return_book = dB.return_book
            books = dB.users_borrowing_history
            fine = 0
            email = ""
            isValidID = False
            book_id = int(input('Enter book id to check : '))
            
            if return_book:

                for book in return_book:
                    for books_id in book:
                        if books_id == book_id:
                            isValidID = True
                            break
                    else:
                        isValidID = False
                
                if isValidID==True:
                
                    for i in return_book:
                        if i[0]==book_id:
                            email = i[1]
                            days = i[2]
                            if days<1:
                                for day in range(0, days, -1):
                                    if day==0:
                                        fine+=100
                                    else:
                                        fine+=10
                                    print('boommm')
                                for i in books:
                                    for keys in i.items():
                                        mail = keys[0]
                                        if mail==email:
                                            for innerDict in keys[1]:
                                                for innerDictKey in innerDict:
                                                    if innerDictKey==book_id:
                                                        book_key = innerDict[innerDictKey]
                                                        for value in book_key:
                                                            book_key.pop()
                                                            book_key.append(fine)
                                                            book_key.append('Returned')
                                                            for i in range(len(return_book)):
                                                                if return_book[i-1][0]==book_id:
                                                                    del return_book[i]
                                                                    print('Book returned back successfully')
                                                            break
                            else:
                                for i in books:
                                    for keys in i.items():
                                        mail = keys[0]
                                        if mail==email:
                                            for innerDict in keys[1]:
                                                for innerDictKey in innerDict:
                                                    if innerDictKey==book_id:
                                                        book_key = innerDict[innerDictKey]
                                                        for value in book_key:
                                                            book_key.pop()
                                                            book_key.append('Returned')
                                                            
                                                            for i in range(len(return_book)):
                                                                if return_book[i-1][0]==book_id:
                                                                    del return_book[i]
                                                                    print('Book returned back successfully')
                                                            break
                else:
                    print('Please check the id which you have entered!')
            else:
                print('There are no new returns')
        else:
            print('Please login to accept return books')

    #For admin login
    @classmethod
    def admin_login(cls):
        username = input('Enter username : ')
        password = input('Enter password : ')
        admin = cls.admin_users
        for i in range(len(admin)):
            if admin[i]['Username']==username and admin[i]['Password']==password:
                print('You are logged in')
                cls.Session = True
                break
            else:
                print('Username or password is incorrect')

    #For admin Logout
    @classmethod
    def admin_logout(cls):
        cls.Session = False
        print('Logged out successfully')
