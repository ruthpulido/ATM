print('Welcome to Sparkasse! ')
account = [
    ["11","1111"],   # account is a table with: [0]=account number, [1]=pin 
    ["22","2222"],
    ["33","3333"]
]                          
balance_01 = int(1000)     # some balance belongs to some pin and to some account number in the table "accounts"
balance_02 = int(2000)      # for exemple: the owner of account "11" has pin "1111" and has 1000€ in the account (balance_01)
balance_03 = int(3000)
trying = 3
enter_your_chois = 'Enter "d" to deposit \nenter "w" to withdraw \nenter "b" to balance \nenter "e" to exit '
goodbye = "Thank you for using Sparkasse! Don't forget you card. "
unvalid = "That is not a valid option, please choose an option from the menu"
while trying != 0:
    accont_number_input = input(str('Enter your account number, 2 digits '))   # <-- customer enters account number (2 digits).
    pin_input = input(('Enter your pin, 4 digits '))      # <-- customer enters pin (4 digits).
    data_input =[accont_number_input, pin_input]
    if (data_input not in account):                # <-- while loop checks that account number and pin are correct and match. 
        trying = trying - 1                         # <- There are three attempts
        print('invalid pin or account number! You have {} tries left. ' .format(trying) )
    else:
        user_choise = input(enter_your_chois)
        if user_choise == 'd':
            deposit = float(input('Enter the Amount, put the money and press Enter ')) # <-- customer enters how much money to deposit
            if data_input == account[0] :
                balance_01 = balance_01 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_01))
                print(goodbye)
            elif data_input == account[1] :
                balance_02 = balance_02 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_02))
                print(goodbye)
            else:
                balance_03 = balance_03 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_03))
                print(goodbye)
        elif user_choise == 'w':
            withdraw = float(input('Enter the Amount: '))  # <-- customer enters how much money to withdraw
            if data_input == account[0] and withdraw < balance_01:
                balance_01 = balance_01 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_01))
                print(goodbye)
            elif data_input == account[1] and withdraw < balance_02:
                balance_02 = balance_02 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_02))
                print(goodbye)
            elif data_input == account[2] and withdraw < balance_03:
                balance_03 = balance_03 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_03))
                print(goodbye)
            elif (data_input == account[0] and withdraw > balance_01) or (data_input == account[1] and withdraw > balance_02) or (data_input == account[2] and withdraw > balance_03):
                print("you don't have enough money in your account.")   
                print(goodbye)  
            elif (data_input == account[0] and withdraw == balance_01) or (data_input == account[1] and withdraw == balance_02) or (data_input == account[2] and withdraw == balance_03):
                balance_01 = balance_01 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_01)) #This was added to show when balance is 0€
                print(goodbye) 
        elif user_choise == 'e':
                print(goodbye)
        elif user_choise == 'b': # <-- check balance
            if data_input == account[0]:
                print("Your balance is {} € " .format(balance_01))
                print(goodbye)
            elif data_input == account[1]:
                print("Your balance is {} € " .format(balance_02))
                print(goodbye)
            else:
                print("Your balance is {} € " .format(balance_03))
                print(goodbye)
        else:
            print(unvalid)

