from users import *
from admin import *
from books import *

class Library(User, Admin):
    user = User()
    admin = Admin()
    book = Books()
    j=1
    try:
        while j!=0:
            print('\n***********************************')
            print('|| Select any one of the options ||')
            print('***********************************')
            print('** | 1.| User                    **')
            print('** | 2.| Admin                   **') 
            print('** | 3.| Exit                    **') 
            print('***********************************')
            req = int(input('Enter input : '))

            if req==1:
                i = 1
                try:
                    while i!=0:
                        print('\n***********************************')
                        print('|| Select any one of the options ||')
                        print('***********************************')
                        print('** | 1.| Login to Library        **')
                        print('** | 2.| Register to Library     **') 
                        print('** | 3.| View Books              **')
                        print('** | 4.| My Books                **')
                        print('** | 5.| Request Books           **')
                        print('** | 6.| Return Books            **')
                        print('** | 7.| Logout                  **')
                        print('***********************************')
                        req = int(input('Enter input : '))
                    
                        if req==1:
                            user.login()
                        elif req==2:
                            user.register()
                        elif req==3:
                            user.view_books()
                        elif req==4:
                            user.my_borrowed_list()
                        elif req==5:
                            user.request_books()
                        elif req==6:
                            user.return_books()
                        elif req==7:
                            user.logout()
                            i=0
                        else:
                            print('Invalid input')
                except:
                    print('No option selected! Program exiting users...........', end=" ")
                    print("\U0001F61F")
            elif req==2:
                i = 1
                try:
                    while i!=0:
                        print('\n**************************************')
                        print('||   Select any one of the options   ||')
                        print('***************************************')
                        print('** | 1.| Admin Login                 **')
                        print('** | 2.| Create Admins               **') 
                        print('** | 3.| View Books                  **')
                        print('** | 4.| Edit Books                  **')
                        print('** | 5.| Delete Books                **')
                        print('** | 6.| Add Books                   **')
                        print('** | 7.| Check Book Requests         **')
                        print('** | 8.| Approve Requested Books     **')
                        print('** | 9.| List Borrowers              **')
                        print('** | 10.| Check Return Requests List **')
                        print('** | 11.| Accept Returned Books      **')
                        print('** | 12.| Logout                     **')
                        print('***************************************')
                        req = int(input('Enter input : '))
                        
                        if req==1:
                            admin.admin_login()
                        elif req==2:
                            admin.create_admin()
                        elif req==3:
                            admin.view_books()
                        elif req==4:
                            admin.edit_books()
                        elif req==5:
                            admin.delete_books()
                        elif req==6:
                            admin.add_books()
                        elif req==7:
                            admin.check_request_list()
                        elif req==8:
                            admin.approve_book()
                        elif req==9:
                            admin.list_borrowers()
                        elif req==10:
                            admin.check_return_book_list()
                        elif req==11:
                            admin.accept_return_books()
                        elif req==12:
                            admin.admin_logout()
                            i=0
                            print('Thank you')
                        else:
                            print('Invalid input')
                except:
                    print('No option selected! Program exiting admin...........', end=" ")
                    print("\U0001F61F")
            elif req==3:
                print('Thank you for visiting uLibrary')
                break
            else:
                print('Invalid input')
    except:
        print('No option selected! Program stopping...........', end=" ")
        print("\U0001F61F")

lib = Library()