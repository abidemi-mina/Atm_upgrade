
def ATM():

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







