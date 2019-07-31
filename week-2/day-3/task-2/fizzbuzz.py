def fizzbuzz(num):
    if num % 3 is 0 and num % 5 is 0:
        print 'FizzBuzz'
    elif num % 2 is 0:
        print 'Fizz'
    elif num % 5 is 0:
        print 'Buzz'
    else:
        print num

fizzbuzz(15)