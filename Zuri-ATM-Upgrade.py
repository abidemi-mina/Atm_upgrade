
def ATM():
    print('WELCOME TO OUR BANK, HOW CAN WE BE OF HELP TO YOU')
    print('1. Do you want to register')
    print('2. Already have an account, login')
    request = int(input('select an answer : '))

    
    if request == 1:
        Firstname  = input('Enter your firstname :')
        Lastname = input('Enter your lastname :')
        Age = int(input('Enter your age :'))
        Gender = input('Enter you gender (Male,Female) :')
        Date_of_Birth = int(input('Enter your date of birth :'))
        Next_of_kin = input('Enter your next of kin name :')
        Password =input('Enter a paasword and it must be at least 8 characters :')
        if len(Password) >=  8 :
            confirm = input('Confirm password :')
            if confirm == Password:
                print('password created successfully')
                print (f'Dear {Lastname} {Firstname} , your account has being created successfully')
                print('Your account number is 210956782')
            else:
                print('Password not the same')
        else:
            print('password is not up to eight')

    elif request == 2 :
        name = input('enter your account name :')
        password = input('enter your password :')
        if not name:
            print ('   Incorrect input , try again ')
        else:
            print ('Login succesful')
            import datetime
            date =datetime.datetime.now()
            print(f' Login in details {date} ')
            print('These are the services we render , please kindly choose an option')

        options =[
            " 1. Withdrawal",
            " 2. Deposit",
            " 3. Comlpaints"
        ]
        
        for s in options :
            print(s)

        answer = int(input('Select an option :'))
        if(answer == 1):
            option1 = input('How much would you like to withdraw :')
            print('Take your cash')

        elif (answer == 2):
            option2 = int(input('How much will you like to deposit: '))
            balance = float(option2 + 50000)
            print(f'Your current balance is {balance}')

        elif(answer == 3):
            complaint = input('What issue will you like to report :')
            print("Thank you for contacting us")
            
        else :
            print('Invalid option selected')

        print ('CLOSING PAGE' )

        import datetime
        time =datetime.datetime.now() 
        print(f' Thank you {name} for banking with us' )
        print(time)     
ATM()







