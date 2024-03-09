import random,math,pickle,stdiomask,pyttsx3,ascii_magic

d={'atm#01':['ssu',0,2020]}


def CREATE_ACC_PAGE():
    f=open('atmOFssuBank.dat','rb')   
    output=ascii_magic.from_image_file("2023-01-22 21 05 39.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    d={}
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    f.close()
    f=open('atmOFssuBank.dat','ab')
    ans='y'
    while ans.lower()=='y':  
     print()
     try:
        n=input("Enter your Username: ").upper()
        pin=stdiomask.getpass("Create your own PIN-(4 digit in numeric form): ")
        pin2=stdiomask.getpass("Retype your PIN once again: ")
        if (len(pin)==4 and len(pin2)==4):
            if pin==pin2:
                data="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*+</>;[]{}$()\_,.-?@!#%&"
                length=len(data)
                id=""
                for j in range(7):
                    id=id+data[math.floor(random.random()*length)]
                print()
                print("Your personal and unique identity-(id) location: ",id)
                d[id]=[n,0,pin]
            else:
                print()
                print("~~ PINs do not match, please try to make your account once again __/\__")
        else:
            print()
            print("Please enter 4(four)-Digit PIN in numeric form")
     except:
        print()
        print("Please enter 4(four)-Digit PIN in numeric form")
     print()
     ans=input("Press 'y/Y' to create more account: ")
    pickle.dump(d,f)
    f.close()
        
def DEPOSIT_PAGE():
    f=open('atmOFssuBank.dat','rb') 
    output=ascii_magic.from_image_file("2023-01-22 20 54 14.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    d={}
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    f.close()
    f=open('atmOFssuBank.dat','ab')
    ans='y'
    while ans.lower()=='y':
     print()
     p=stdiomask.getpass("Enter your PIN: ")
     id2=stdiomask.getpass("Enter your unique id: ")
     print()
     found=False
     for i in d:
        if i==id2:
            if d[i][2] == p:
                found = True
                v = d.get(i)
                name = v[0]
                prst_bal = v[1]
                print("Your present balance is: ", prst_bal)
                m = eval(input("Enter the amount to be deposited: "))
                tl_bal = prst_bal + m
                d[i][1] = tl_bal
     if found==True:
        print()
        print("Your Username: ",name)
        print("Money deposited: ",m)
        print("Your present total balance is: ",tl_bal)
     else:
        print()
        print("*** ACCOUNT NOT FOUND !!! ***....Please provide correct PIN and ID to deposit the amount __/\__")
     print()
     ans=input("Press 'y/Y' to deposit more amount: ")
    pickle.dump(d,f)
    f.close()
        
def WITHDRAW_PAGE():
    f=open('atmOFssuBank.dat','rb')
    output=ascii_magic.from_image_file("2023-01-22 20 59 15.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    d={}
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    f.close()
    f=open('atmOFssuBank.dat','ab')
    a=d.keys()
    ans='y'
    while ans.lower()=='y':
     print()
     p=stdiomask.getpass("Enter your PIN: ")
     id2=stdiomask.getpass("Enter your unique id: ")
     found=False
     for i in a:
        if i == id2:
            if d[i][2] == p:
                found = True
                v = d.get(i)
                prst_bal = v[1]
                print("Your present balance is: ", prst_bal)
                name = v[0]
                if v[1] == 0:
                    m = "You have zero balance in your savings account, so you can't withdraw money"
                    rem_bal = 0
                else:
                    m = eval(input("Enter the amount to be withdrawn: "))
                    if m<=60000:
                        if m<=v[1]:
                            v[1] = v[1] - m
                            rem_bal = v[1]
                            d[i][1] = rem_bal
                        else:
                            print()
                            m = """ In this case you need to deposite some more amoumnt 
                                of money if you want to withdraw-(Insufficient funds) """
                            rem_bal = v[1]
                    else:
                        print()
                        m="You can't withdraw money more than 60000 in one day"
                        rem_bal = v[1]
     if found==True:
        print()
        print("Your Username: ",name)
        print("Money withdrawn: ",m)
        print("Your remaining balance is: ",rem_bal)
     else:
        print()
        print("*** ACCOUNT NOT FOUND !!! ***....Please provide correct PIN and ID to withdraw the amount __/\__")
     print()
     ans=input("Press 'y/Y' to withdraw more amount: ")
    pickle.dump(d,f)
    f.close
        
def PIN_CHANGE_PAGE():
    f=open('atmOFssuBank.dat','rb')
    output=ascii_magic.from_image_file("2023-01-22 21 10 25.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    d={}
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    f.close()
    f=open('atmOFssuBank.dat','ab')
    ans='y'
    while ans.lower()=='y':
     print()
     p=stdiomask.getpass("Enter your current pin: ")
     id2 = stdiomask.getpass("Enter your unique id: ")
     print()
     found=False
     for i in d:
        if i == id2:
            if d[i][2] == p:
                found=True
                try:
                    new_pin = stdiomask.getpass("Create your own new pin-(4 digit in numeric form): ")
                    new_pin2 = stdiomask.getpass("Retype your new PIN once again: ")
                    if len(new_pin)==4 and len(new_pin2)==4:
                        #if new_pin2 >= 1000 and new_pin2 <= 9999:
                        if new_pin == new_pin2:
                            d[i][2] = new_pin
                            print()
                            print("Your PIN has been changed successfully")
                        else:
                            print()
                            print("~~ New PINs do not match, please try to change your PIN once again __/\__")
                    else:
                        print()
                        print("Please enter 4(four)-Digit PIN in numeric form")
                except:
                    print()
                    print("Please enter 4(four)-Digit PIN in numeric form")
     if found==False:
        print("*** ACCOUNT NOT FOUND !!! ***....Please provide correct current PIN and ID to change your PIN __/\__")
     else:
        print()
     ans=input("Press 'y/Y' to change the PIN of other accounts: ")
    pickle.dump(d,f)
    f.close()
    
def BAL_CHECK_PAGE():
    f=open('atmOFssuBank.dat','rb')
    output=ascii_magic.from_image_file("2023-01-22 21 13 51.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    d={}
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    ans='y'
    while ans.lower()=='y':
     print()
     p = stdiomask.getpass("Enter your PIN: ")
     id2 = stdiomask.getpass("Enter your unique id: ")
     print()
     found=False
     for i in d:
        if i == id2:
            if d[i][2] == p:
                found=True
                print()
                print("Your Username: ", d[i][0])
                print("Your current balance is: ", d[i][1])
     if found==False:
        print("*** ACCOUNT NOT FOUND !!! ***....Please provide correct PIN and ID to check your balance __/\__")
     else:
        print()
     ans=input("Press 'y/Y' to check the balance of other accounts: ")
    f.close()
    
def DEL_ACC_PAGE():
    D={}
    f=open("atmOFssuBank.dat","rb+")
    while True:
        try:
            d=pickle.load(f)
        except EOFError:
            break
    ans='y'
    while ans.lower()=='y':
     print()
     p = stdiomask.getpass("Enter your PIN: ")
     id2 = stdiomask.getpass("Enter your unique id: ")
     print()
     found=False
     for k in d:
        if k!=id2:
            found=True
            D[k]=d[k]
            pickle.dump(D,f)
     if found==False:
        print("*** ACCOUNT NOT FOUND !!! ***....Please provide correct PIN and ID to delete your account __/\__")
     else:
        print("*** YOUR ACCOUNT SUCCESSFULLY DELETED ***")
     print()
     ans=input("Press 'y/Y' to delete more accounts: ")
    f.close()
    
ANS='a'
while ANS.lower()=='a':
    print()
    output=ascii_magic.from_image_file("money-bag-atm-machine-next-260nw-1412132549.webp",columns=100,char='@')
    ascii_magic.to_terminal(output)
    print()
    print('*********************************************************************************************************************')
    print('                                                ATM MACHINE                                                          ')
    print('                                        ~~~ Welcome To SSU Bank ~~~                                                     ')
    text_speech=pyttsx3.init()
    a="welcome to automated teller machine of SSU bank"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print('''Ad-
           Banking Jobs(IBPS-SBI, RBI, BOI, SSU etc.)
           for more information, visit www.recruitment.gov ''')
    print('''                                                                                  Ad-
                                                                                               RBI kehta hai-
                                                                                               Jaankar Baniye,
                                                                                               Satark Rahiye......''')
    print(''' Please maintain following COVID-19 Protocols in the ATM centre :-
               # You must wear a musk
               # You must sanitise your hand 
               # Don't spit in the ATM centre
               # Maintain atleast 2-feet of social distance ''')
    print(''' Do's and Don'ts :-
               # Do not liters unwanted things and rappers here & there, you must put in the dustbin only
               # Do not eat food in the ATM centre, but you can drink water
               # You can use any ATM card of any bank in the ATM of SSU bank
               # You should maintain silence in the ATM centre
               # If you have sufficient amount of money in your Savings Account then, you can only able to withdraw atmost Rs.60000 money per day
               # Do not untidy the ATM centre
               # Do not share your own personal unique id and PIN with others, if you share by mistake then please contact-(consult) with SSU Bank
                 'OR' you may change your PIN-(create a new pin) ''')
    print()
    ans='y'
    while ans.lower()=='y':
        output=ascii_magic.from_image_file("cartoon-holding-credit-card-bank-vector-12235975.jpg",columns=100,char='@')
        ascii_magic.to_terminal(output)
        print()
        ch=input('''**************************************************************************************************************
                                                        MENU
                                                        
                                  1) Press either 'c' or 'C' to Create your account
                                  2) Press eihter 't' or 'T' to Deposit the money
                                  3) Press eihter 'w' or 'W' to Withdraw the amount
                                  4) Press eihter 'p' or 'P' to do PIN change
                                  5) Press eihter 'b' or 'B' to check your balance
                                  6) Press either 'q' or 'Q' to delete your account
        
        Enter your choice: ''')
        print("-------------------------------------------------------------------------------------------------------------------")
        print()
        if ch=='c' or ch=='C':
            CREATE_ACC_PAGE()
        elif ch=='t' or ch=='T':
            DEPOSIT_PAGE()
        elif ch=='w' or ch=='W':
            WITHDRAW_PAGE()
        elif ch=='p' or ch=='P':
            PIN_CHANGE_PAGE()
        elif ch=='b' or ch=='B':
            BAL_CHECK_PAGE()
        elif ch=='q' or ch=='Q':
            DEL_ACC_PAGE()
        else:
            print()
            print("~~ Sorry, You have entered wrong choice !!!")
        print("-------------------------------------------------------------------------------------------------------------------")
        print()
        exit=input("Press either 'e' or 'E' to Exit 'OR' else press any key to go MENU option: ")
        print()
        print("-------------------------------------------------------------------------------------------------------------------")
        print()
        if exit=='e' or exit=='E':
            print('****************************************************************************************************************')
            print('''                                    THANK YOU FOR USING ATM MACHINE OF SSU BANK _/\_,
                                                                    PLEASE VISIT AGAIN....''')
            print('****************************************************************************************************************')
            text_speech=pyttsx3.init()
            a="thank you for using ATM of SSU bank, please visit again"
            text_speech.setProperty("rate",110)
            text_speech.say(a)
            text_speech.runAndWait()
            print()
            ans=input("Press either 'y' or 'Y' to go MENU option 'OR' else press any key: ")
            ANS=input("""Press either 'a' or 'A' to run ATM 'OR' else press any key to exit: """)
            output=ascii_magic.from_image_file("how-to-respond-to-thank-you.webp",columns=150,char='@')
            ascii_magic.to_terminal(output)
