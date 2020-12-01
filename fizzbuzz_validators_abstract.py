from abc import ABC, abstractmethod


class FizzBuzzHandler(ABC):
    """
    Interface base para nossa corrente de validadores
    Possui um método para encadear o próximo handler da corrente e
    um método para executar a validação de cada regra do FizzBuzz
    """


    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def validate(self, number):
        pass


class AbstractFizzBuzzHandler(FizzBuzzHandler):
    """
    Esta é a classe base do nosso validador.
    Ela determina o comportamento padrão dos dois métodos definidos na interface

    """

    _next_handler = None

    def set_next_handler(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def validate(self, number):
        if self._next_handler:
            return self._next_handler.validate(number)
        return number
