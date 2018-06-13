#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03


import a4q2 as Check

console_input = ''

print('Enter an expression to check if the parentheses are balanced.',
        'Enter \'quit\' to end program:')
while True:
    console_input = input('>')
    if console_input == 'quit':
        break
    else:
        result = Check.check_balance(console_input)
        print(result)
print("Goodbye!")
