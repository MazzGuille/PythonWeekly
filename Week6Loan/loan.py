from turtle import goto


print("Hello, thanks for choosing us to help you with your loan! I will ask you a series of questions to help determine your best credit option.")
print("===========================================================")
print("Please, tell me your name:")
name = input()
print()

repeat = True
while repeat == True:
    print("What is the loan amount you are requesting?")
    loan_amount = float(input())
    if loan_amount < 50000:
        print("Your loan amount is too small, please try again.")
        repeat = True
    elif loan_amount > 150000:
        print("Your loan amount is too large, please try again.")
        repeat = True 
    else:
        repeat = False        
print()

print("Between 1 and 10, being 10 perfect and 1 terrible, how would you rate your credit score?")
personal_cs = int(input())
print()


print("Indicate your monthly income:")
income = float(input())
print()
    

print("How large is your downpayment?")
downpayment = float(input())
print()

credit_socre = 0

if loan_amount >= 50000 and loan_amount <= 60000:
    credit_socre += 10
elif loan_amount >= 60000 and loan_amount <= 70000:
    credit_socre += 9
elif loan_amount >= 70000 and loan_amount <= 80000:
    credit_socre += 8
elif loan_amount >= 80000 and loan_amount <= 90000:
    credit_socre += 7
elif loan_amount >= 90000 and loan_amount <= 100000:
    credit_socre += 6
elif loan_amount >= 100000 and loan_amount <= 110000:
    credit_socre += 5
elif loan_amount >= 110000 and loan_amount <= 120000:
    credit_socre += 4
elif loan_amount >= 120000 and loan_amount <= 130000:
    credit_socre += 3
elif loan_amount >= 130000 and loan_amount <= 140000:
    credit_socre += 2
elif loan_amount >= 140000 and loan_amount <= 150000:
    credit_socre += 1

    

    
if personal_cs == 1 :
    credit_socre += 1
elif personal_cs == 2 :
    credit_socre += 2
elif personal_cs == 3 :
    credit_socre += 3
elif personal_cs == 4 :
    credit_socre += 4
elif personal_cs == 5 :
    credit_socre += 5
elif personal_cs == 6 :
    credit_socre += 6
elif personal_cs == 7 :
    credit_socre += 7
elif personal_cs == 8 :
    credit_socre += 8
elif personal_cs == 9 :
    credit_socre += 9
else :
    credit_socre += 10

    
if income >= 5000 and income <= 10000:
    credit_socre += 1
elif income >= 10001 and income <= 20000:
    credit_socre += 2
elif income >= 20001 and income <= 30000:
    credit_socre += 3
elif income >= 30001 and income <= 40000:
    credit_socre += 4
elif income >= 40001 and income <= 50000:
    credit_socre += 5
elif income >= 50001 and income <= 60000:
    credit_socre += 6
elif income >= 60001 and income <= 70000:
    credit_socre += 7
elif income >= 70001 and income <= 80000:
    credit_socre += 8
elif income >= 80001 and income <= 90000:
    credit_socre += 9
elif income >= 90001 and income <= 100000:
    credit_socre += 10

    
if downpayment >= 5000 and downpayment <= 10000:
    credit_socre += 1
elif downpayment >= 10001 and downpayment <= 15000:
    credit_socre += 2
elif downpayment >= 15001 and downpayment <= 20000:
    credit_socre += 3
elif downpayment >= 20001 and downpayment <= 25000:
    credit_socre += 4
elif downpayment >= 25001 and downpayment <= 30000:
    credit_socre += 5
elif downpayment >= 30001 and downpayment <= 35000:
    credit_socre += 6
elif downpayment >= 35001 and downpayment <= 40000:
    credit_socre += 7
elif downpayment >= 40001 and downpayment <= 45000:
    credit_socre += 8
elif downpayment >= 45001 and downpayment <= 50000:
    credit_socre += 9
elif downpayment >= 50001 and downpayment <= 55000:
    credit_socre += 10
    
if (loan_amount *1.12) / 12 < (income * 0.3):
    credit_socre += 1
if (loan_amount *1.12) / 12 < (income * 0.2):
    credit_socre += 2
if (loan_amount *1.12) / 12 < (income * 0.1):
    credit_socre += 3
    


print() 
print("===========================================================")
print()
print(f"Your credit score is: {credit_socre}")
print()
print("===========================================================")
if (loan_amount *1.12) / 12 < (income * 0.3):
    print("Your monthly payment is too high for yor income, please try again with a lower amount.")
    
loan = False

if loan_amount >= 100000
    


    
    