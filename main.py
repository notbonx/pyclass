from abc import abstractmethod
from multipledispatch import dispatch
import inspect


class BankAccount:
    @dispatch(str, int, int)  # конструктор не нужно перегружать
    def __init__(self, UserName, Number, Value):
        self.__UserName = UserName
        self.__Number = Number
        self.__Value = Value

    @dispatch(str, str, str)
    def __init__(self, UserName, Number, Value):
        self.__UserName = UserName
        self.__Number = Number
        self.__Value = Value

    def setData(self, UserName, Number, Value):  # setter
        self.__UserName = UserName
        if (BankAccount.checkInt(self.__Number)):
            self.__Number = Number
        else:
            print("Error value")
        self.__Value = Value

    def getData(self):  # getter
        return self.__UserName, self.__Number, self.__Value

    @staticmethod
    def checkInt(val):
        if isinstance(val, int) or isinstance(val, int):
            return True
        return False

    def addValue(self, val):
        self.setData(self.__UserName, self.__Number, self.__Value + val)

    @staticmethod
    def Check_key():
        pass

    @abstractmethod
    def info_print(self):
        pass

    @abstractmethod
    def datasetinfo(self):
        pass

    def __str__(self):
        return "({0},{1},{2})".format(self.__UserName, self.__Number, self.__Value)

    def __add__(self, other):
        UserName = self.__UserName
        Number = self.__Number
        Value = self.__Value + other.__Value
        return BankAccount(UserName, Number, Value)


# создать дочерние классы с двумя полями
class BankAccCard(BankAccount):
    def __int__(self, UserName, Number, Value, CardNumber, DateCard):
        super().__init__(self, UserName, Number, Value)
        self.__CardNumber = CardNumber
        self.__DateCard = DateCard


# class BankAccCardCredit(BankAccCard):
#     def __init__(self, UserName, Number, Value, CardNumber, DateCard, CreditValue, CreditCurrency):
#         BankAccCard.__init__(self, UserName, Number, Value, CardNumber, DateCard, CreditValue, CreditCurrency)
#         self.__CreditValue = CreditValue
#         self.__CreditCurrency = CreditCurrency
#
#     def getData(self):
#         pass


def main():
    user = BankAccCard(432, 530, 1000, 42551901, 823)  # constructor
    print(user.getData())

    user = BankAccCard("Anton", "530 str", "1000 val")  # konstructor
    print(user.getData())


if __name__ == '__main__':
    main()
# i hate my life but i hate you more
# i love little girls
