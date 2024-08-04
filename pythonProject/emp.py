class Employee:
    def __init__(self):
        self.__no=None
        self.__name=None
        self.__sal=None
    def setEmployee(self,n,na,sal):
        self.__no=n
        self.__name=na
        self.__sal=sal
    def printEmployee(self):
        print(f'{self.__no},{self.__name},{self.__sal}')