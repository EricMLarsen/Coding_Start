## Lets get you trying to see how to add multiply substract and divide in programming

# This is really easy as long as you have the values, but we are going to make it
# Easier for you to put in values from the line and then tell the computer what you want

# First lets get two values from the user

#Since are are looking for numbers we need to cast the values to a float format to include decimal points
#Value 1
value1 = float(input("What is your first value?"))
#Value 2
value2 = float(input("What is your second value?"))

#Now this is were we are going to ask the user what they want to do
print("What Operation would you like to do? (Divide, Multiply, Add, Subtract, or Remainder)")

#These are all the operations in math python is going to be able to do, everything else comes from these

#So what we need to do is intake the users desired operation desired, making sure it is spelled like in the prompt
Operation = input("Desired Operation:")

#Now we will build a case structure using if statements

#An if statement is the way the computer has to check logical statements, basically, If the statement is true
#then the computer will perform the operation
#Lets go ahead and try it

#Addition
# our logical statement of if the operation is add then we want to do addition
if(Operation == 'Add'):
    #now we tell it what to do
    value3 = value1 + value2
# We can then chain this operation of logic checks by using something called elif standing for else if
# It tells the computer that if the first if statement is not true then check this
elif(Operation == "Substract"):
    #Now we can say substract what we need
    value3 = value1 - value2
#Now we will continue these until we have all the operations listed
#Mulitplication
elif(Operation == "Multiply"):
    value3 = value1 * value2
#Division
elif(Operation == "Divide"):
    value3 = value1 / value2
#Remainder: will return the remainder value interger of value 1 divided by value 2
elif(Operation == "Remainder"):
    value3 = value1 % value2
#now we have to check if they did not input an operation that was valid
else:
    print("You did not input a correct operation")

#Assuming there is a value, this checks if the value has been assigned before moving forward
try:
    value3
except NameError:
    value3_exists = False
else:
    value3_exists = True

#now lets print the value as long as the value exists
if(value3_exists):
    print(f"Your value from operation '{Operation}' is : {value3}")

