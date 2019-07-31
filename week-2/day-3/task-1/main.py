num = raw_input('Enter a number: ')
# num = int(num)

try:
    num = int(num)
    if 0 < num <= 10:
        if num % 2 > 0 or num is 2:
            print 'Your number is prime'
        else:
            print 'Not prime'
    else:
        print 'Enter a number between 1 and 10'
except ValueError as error:
    print 'Not an integer'

# if type(num) != type(int()):
#     print 'Not an integer'
# elif num < 1 or num > 10:
#     print 'Out of range'
# elif num % 2 == 0:
#     if num == 2:
#         print 'Your number is prime'
#     else:
#         print 'Your number is not prime'
# else:
#     if num == 3 or num == 5 or num == 7:
#         print 'Ypour number is prime'
#     else:
#         print 'Your number is not prime'