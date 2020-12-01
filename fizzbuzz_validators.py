from fizzbuzz_validators_abstract import AbstractFizzBuzzHandler

"""
Em cada classe concreta iremos implementar apenas uma das regras de validação. 

"""
class MultipleOf3And5Handler(AbstractFizzBuzzHandler):

    def validate(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        return super().validate(number)


class MultipleOf3Handler(AbstractFizzBuzzHandler):

    def validate(self, number):
        if number % 3 == 0:
            return "Fizz"
        return super().validate(number)


class MultipleOf5Handler(AbstractFizzBuzzHandler):

    def validate(self, number):
        if number % 5 == 0:
            return "Buzz"
        return super().validate(number)



"""
Vamos criar um método que ira criar e retornar nossa corrente de handlers 
"""
def get_fizzbuzz_validator():
    # Vou criar o validador a partir do primeiro handler que eu quero que seja executado
    validator = MultipleOf3And5Handler()

    # Depois encadeamos os próximos handler na sequencia desejada
    # Lembre-se que podemos chamar o método .set_next_handler() sequencialmente pois definimos que o
    # retorno do método é o próprio handler informado como parâmetro
    validator.set_next_handler(MultipleOf3Handler()).set_next_handler(MultipleOf5Handler())

    # E retornamos o validador criado e já encadeado
    return validator

