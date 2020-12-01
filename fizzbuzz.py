def FizzBuzz(number_list):
    for number in number_list:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == '__main__':
    list_size = 15

    FizzBuzz(list(range(1, list_size+1)))


