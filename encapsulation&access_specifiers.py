# ENCAPSULATION AND ACCESS SPECIFIERS:

class bank:
    def __init__(self):
        self.__value = 10
        print("value:", self.__value)
        print("-------------------")

    def __ram(self):
        print("Ac no:24123543458")
        print("name:DAVID")
        print("STATE BANK")

    def __sam(self):
        print("Ac no:2412323543458")
        print("name:vishal")
        print("INDIAN BANK")


o = bank()
o._bank__ram()
o._bank__sam()
o._bank__value


