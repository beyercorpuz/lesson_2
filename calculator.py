def prompt(message):
    print(f'==> {message}')

prompt('Welcome to Calculator!')

prompt("what's the first number?")
number1 = input()
prompt("what's the second number?")
number2 = input()

prompt('what operation would you like to perform?\n'
      '1) Add 2) Subtact 3) Multiply 4) Divide')
operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f'The result is {output}')
  
        