from fizzbuzz_validators import get_fizzbuzz_validator


def fizz_buzz(number_list):
    fizzbuzz_validator = get_fizzbuzz_validator()
    for number in number_list:
        print(fizzbuzz_validator.validate(number))


if __name__ == '__main__':
    list_size = 15

    fizz_buzz(list(range(1, list_size+1)))


