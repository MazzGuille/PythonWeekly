#EXAMPLE A
#{
from multiprocessing import Condition


freez = float(input("What is the frezzing in Farenheit?"))
boil = float(input("What is the boiling in Farenheit?"))

#Function to convert a Ferenheit temperature to Celsius
farenheits_to_celcius_F = ( freez - 32) * 5 / 9;
farenheits_to_celcius_B = ( boil - 32) * 5 / 9;

print(f"The freezing point in celcius is {farenheits_to_celcius_F:.1f}")
print(f"The boiling point in celcius is {farenheits_to_celcius_B:.1f}") 
#}

#EXAMPLE B
#{
freez = float(input("What is the frezzing in Farenheit?"))
boil = float(input("What is the boiling in Farenheit?"))

#Function to convert a Ferenheit temperature to Celsius
#farenheits_to_celcius =  ({} - 32) * 5 / 9;

#print(f"The freezing point in celcius is {farenheits_to_celcius{freez}:.1f}")
#print(f"The boiling point in celcius is {farenheits_to_celcius{boil}:.1f}") 
#}



