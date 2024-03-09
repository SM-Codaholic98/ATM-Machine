import random
import math
d={}
ANS='a' or 'A'
while ANS=='a' or ANS=='A':
    print()
    print('*********************************************************************************************************************')
    print('                                                ATM MACHINE                                                          ')
    print('                                        !!! Welcome To SSU Bank !!!                                                     ')
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
    ans='Y' or 'y'
    while ans=='Y' or ans=='y':
        print()
        print('****************************************************************************************************************')
        print("                                                  MENU")
        print()
        print("                               To Create your account press either : 'c' or 'C'")
        print("                               If you want to Deposit your money press eihter : 't' or 'T'")
        print("                               If you want to Withdraw your amount press eihter : 'w' or 'W'")
        print("                               To do PIN change press eihter : 'p' or 'P'")
        print("                               If you want to check your balance press eihter : 'b' or 'B'")
        print()
        ch=input("Enter your choice: ")
        print()
        if ch=='c' or ch=='C':
            print('--------------------------------------------START PAGE-------------------------------------------------------')
            print()
            try:
                n=input("Enter your Username: ")
                pin=int(input("Create your own PIN-(4 digit in numeric form): "))
                pin2=int(input("Retype your PIN once again: "))
                if (len(str(pin))==4 and len(str(pin2))==4):
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
                        print("PINs do not match, please try to make your account once again")
                else:
                    print()
                    print("Please enter 4(four)-Digit PIN in numeric form")
            except:
                print()
                print("Please enter 4(four)-Digit PIN in numeric form")
        elif ch=='t' or ch=='T':
            print('---------------------------------------------DEPOSIT PAGE----------------------------------------------------')
            print()
            p=int(input("Enter your PIN: "))
            id2=input("Enter your unique id: ")
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
                print("No such pin found, please enter your correct pin")
        elif ch=='w' or ch=='W':
            print('--------------------------------------------WITHDRAW PAGE----------------------------------------------------')
            a=d.keys()
            p=int(input("Enter your PIN: "))
            id2=input("Enter your unique id: ")
            print()
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
                print("No such pin found, please enter your correct pin")
        elif ch=='p' or ch=='P':
            print('-------------------------------------------PIN CHANGE PAGE----------------------------------------------------')
            p=int(input("Enter your current pin: "))
            id2 = input("Enter your unique id: ")
            print()
            for i in d:
                if i == id2:
                    if d[i][2] == p:
                        prst_bal = d[i][1]
                        try:
                            new_pin = int(input("Create your own new pin-(4 digit in numeric form): "))
                            new_pin2 = int(input("Retype your new PIN once again: "))
                            if new_pin >= 1000 and new_pin <= 9999:
                                if new_pin2 >= 1000 and new_pin2 <= 9999:
                                    if new_pin == new_pin2:
                                        d[i][2] = new_pin
                                        name = d[i][0]
                                        prst_bal = d[i][1]
                                        print()
                                        print("Your PIN has been changed successfully")
                                    else:
                                        print()
                                        print("New PINs do not match, please try to change your PIN once again")
                            else:
                                print()
                                print("Please enter 4(four)-Digit PIN in numeric form")
                        except:
                            print()
                            print("Please enter 4(four)-Digit PIN in numeric form")
            print()
        elif ch=='b' or ch=='B':
            p = int(input("Enter your PIN: "))
            id2 = input("Enter your unique id: ")
            print()
            for i in d:
                if i == id2:
                    if d[i][2] == p:
                        print()
                        print("Your Username: ", d[i][0])
                        print("Your current balance is: ", d[i][1])
        else:
            print()
            print("You have entered wrong choice")

        print()
        exit=input("Press either 'e' or 'E' to Exit 'OR' else press any key: ")
        print()
        if exit=='e' or exit=='E':
            print('****************************************************************************************************************')
            print('''                                    THANK YOU FOR USING ATM MACHINE OF SSU BANK _/\_,
                                                                    PLEASE VISIT AGAIN....''')
            print('****************************************************************************************************************')
            print()
            ans=input("Press either 'y' or 'Y' to go MENU option 'OR' else press any key: ")
            ANS=input("""Press either 'a' or 'A' to run ATM (If you do not wish to run ATM then please do not press any other key,
                                                               If you Press either'y' or 'Y' to go MENU option then you can press any key: """)
