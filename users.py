from database import*
from datetime import *
import re

class User(dB):

    def __init__(self):
        self.session = False
        self.email = ""

    def request_books(self):
        if self.session:
            books = dB.book_collection
            reqDict = {}
            reqBooks = dB.requested_books
            email = self.email
            isValidID = False
            book_id = int(input('Enter book ID : '))
            reqDict['book_id'] = book_id
            reqDict['email'] = email
            available_copy = 0
            isAvailable = False
            isInList = True
            
            for i in range(len(books)):
                if books[i]['book_id']==book_id:
                    if books[i]['available_copy']>0:
                        available_copy = books[i]['available_copy']
                        isAvailable = True
                        break
                    else:
                        isAvailable = False
                        break            
            if isAvailable==True:
                if reqBooks:
                    for i in range(len(reqBooks)):
                        if reqBooks[i]['email']==email and reqBooks[i]['book_id']==book_id:
                            print(f'Book with id {book_id} is already in the list, Please contact admin for approval')
                            isInList = False
                            break
                    for i in range(len(books)):
                        if books[i]['book_id']==book_id:
                            isValidID=True
                            break
                    else:
                        print('Invalid Book ID')

                    if isValidID==True:
                        if isInList==True:
                            dB.requested_books.append(reqDict)
                            print(f'Book id {book_id} has been submited to admin')
                            for i in range(len(books)):
                                if books[i]['book_id']==book_id:
                                    books[i]['available_copy']-=1
                else:
                    for i in range(len(books)):
                        if books[i]['book_id']==book_id:
                            isValidID=True
                            break
                    else:
                        print('Invalid Book ID')

                    if isValidID==True:
                        dB.requested_books.append(reqDict)
                        print(f'Book id {book_id} has been submited to admin')
                        for i in range(len(books)):
                            if books[i]['book_id']==book_id:
                                books[i]['available_copy']-=1
            else:
                print('There are no available copies')
        else:
            print('You are not logged in to request books')

    def register(self):
        users = dB.users_dB
        isDOB = False
        dobReg = '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
        isContact = False
        isEmail = False
        isExist = True
        emailReg = '[a-z.@]\.com$'
        userDict = {}
        
        name = input('Enter your name : ')
        dob = input('Enter your date of birth (dd-mm-yyyy format): ')
        if bool(re.search(dobReg, dob)):
            isDOB = True
        contact = input('Enter your contact number (10 digit only): ')
        if contact.isdigit():
            if len(contact)==10:
                isContact = True
        else:
            isContact = False
        email = input('Enter your email : ')
        for i in range(len(users)):
            mail = users[i]['Email']
            if mail==email:
                isExist=True
                break
        else:
            isExist=False
        if bool(re.search(emailReg, email)):
            isEmail = True
           
        password = input('Enter your password : ')
        
        if isDOB==True and isContact==True and isEmail==True and isExist==False:
            contact = int(contact)
            userDict['Name'] = name
            userDict['DoB'] = dob
            userDict['Contact'] = contact
            userDict['Email'] = email
            userDict['Password'] = password

            dB.users_dB.append(userDict)
            # print(dB.users_dB)
            if userDict:
                print('Your account has been created successfully', end=" ")
                print("\U0001F604")
            else:
                print('There is some error in creating your account')
        elif isDOB == False:
            print('Please enter dob in correct format!', end=" ")
            print("\U0001F61F")
        elif isContact == False:
            print('Contact can only be of 10 digits!', end=" ")
            print("\U0001F61F")
        elif isEmail==False:
            print('Please enter a valid email!', end=" ")
            print("\U0001F61F")
        elif isExist==True:
            print('This email already exists, Please login', end=" ")
            print("\U0001F61F")



    def login(self):
        users = dB.users_dB
        username = input('Enter your username : ')
        password = input('Enter your password : ')
        if len(users)>0:
            for i in range(len(users)):
                if users[i]['Email']==username and users[i]['Password']==password:
                    # breakpoint()
                    self.session = True
                    self.email = username
                    books = dB.users_borrowing_history
                    email=username
                    book_id_for_submitting = 0
                    month = 0
                    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

                    for i in books:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            book_id_for_submitting = innerDict[innerDictKey]
                                        for book_ids in book_id_for_submitting:
                                            if innerDictKey==book_ids:
                                                book_key = innerDict[innerDictKey]
                                                for value in book_key:
                                                    length_of_book_key = len(book_key)-1
                                                    remaining_days = book_key[2]
                                                    current_day = date.today()
                                                    date_convertor = str(book_key[1]).split()
                                                    for i in range(1, len(Months)):
                                                        if date_convertor[0]==Months[i]:
                                                            month = i+1
                                                    day = int(date_convertor[1].replace(',', ""))
                                                    year = int(date_convertor[2])

                                                    returning_date = date(year, month, day)

                                                    day = returning_date-current_day
                                                    days_remaining = day.days

                                                    if book_key[length_of_book_key]=='Pending':
                                                        book_key.pop(length_of_book_key-1)
                                                        book_key.insert(length_of_book_key-1, days_remaining)

                                                    elif book_key[length_of_book_key]=='Returned':
                                                        pass

                                                    else:
                                                        book_key.pop()
                                                        book_key.append(days_remaining)
                                                    break
                    print('Welcome to uLibrary', end=" ")
                    print("\U0001F604")
                    break
                else:
                    pass
            else:
                print('Password or username is incorrrect')
        else:
            print('No users')
        
    def view_books(self):
        print(self.session)
        if self.session==True:
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
            print('You are not logged in to view books')

    def my_borrowed_list(self):
        if self.session:
            email = self.email
            books = dB.users_borrowing_history
            book_history = []
            custom_dict = {}
            seperate_book_history = []
            for i in books:

                for keys in i.items():
                    mail = keys[0]
                    if mail==email:
                        for innerDict in keys[1]:
                            for innerDictKey in innerDict:
                                if innerDictKey=='books':
                                    book_key = innerDict[innerDictKey]
                                    for value in book_key:
                                        book_history.append(value)
                                if innerDictKey in book_history:
                                    for book_id in book_history:
                                        books_id = innerDict[book_id]
                                        custom_dict[book_id]=innerDict[book_id]
                                    seperate_book_history.append(custom_dict)
                                    break
            for i in range(len(seperate_book_history)):
                for book_id in book_history:
                    values = seperate_book_history[i][book_id]
                    for individual_value in values:
                        print(book_id, "\t", individual_value, end="\t")
                        book_id = ""
                    print('\n')
                    
        else:
            print('You are not logged in to view books')



    def return_books(self):
        if self.session:
            email = self.email
            books = dB.users_borrowing_history
            book_history = []
            seperate_book_history = []
            number = None
            submit_book = []
            custom_dict = {}
            my_books = []
            book_id_for_submitting = int(input("Enter the book id to return : "))
            for i in books:

                for keys in i.items():
                    mail = keys[0]
                    if mail==email:
                        for innerDict in keys[1]:
                            for innerDictKey in innerDict:
                                if innerDictKey=='books':
                                    book_key = innerDict[innerDictKey]
                                    for value in book_key:
                                        book_history.append(value)
                                if innerDictKey in book_history:
                                    for book_id in book_history:
                                        books_id = innerDict[book_id]
                                        custom_dict[book_id]=innerDict[book_id]
                                    seperate_book_history.append(custom_dict)
                                    break
            for i in range(len(seperate_book_history)):
                for j in book_history:
                    my_books.append(j)
                    l = seperate_book_history[i][j]
                    if j==book_id_for_submitting:
                        number = l[2]

            if book_id_for_submitting in my_books:
                submit_book.append(book_id_for_submitting)
                submit_book.append(email)
                submit_book.append(number)
                dB.return_book.append(submit_book)
                for i in books:
                    for keys in i.items():
                        mail = keys[0]
                        if mail==email:
                            for innerDict in keys[1]:
                                for innerDictKey in innerDict:
                                    if innerDictKey==book_id_for_submitting:
                                        book_key = innerDict[innerDictKey]
                                        for value in book_key:
                                            book_key.append('Pending')
                                            break
                print('Book has been submitted to admin, Please check my account after some time')
            else:
                print('Please check the id of your book!')
        else:
            print('Please login to return books')



    def logout(self):
        self.session=False
        print('Thank you for visiting uLibrary')
