#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    p = 10 
    while p > 0:
        print (p)
        p -= 1
    else:
        print("Happy New Year!")
    # pass

def square_integers(int_list):
    # code goes here!
    squar = [i * i for i in int_list]
    return squar
    # pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# print(happy_new_year())
print(square_integers([1,2,3,4,5]))