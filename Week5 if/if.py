
price = input('How much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = .07    
else:
    tax = 0
print(f'The tax is {tax}')    #when it's not indented, it's out of the statement and will always run.

#convert to upper or lower case
#value.upper() or value.lower()

country = input('What country are you from? ')
country = country.lower()

if country == 'canada':
    province = input('What province are you in? ')
    province = province.lower()
    if province in ('alberta',\
        'nunavut','yukon'):
        tax = .05
    elif province == 'ontario':
        tax = .13
    else:
        tax = .15
else:
    tax = 0
print(f'The tax is {tax}')

    