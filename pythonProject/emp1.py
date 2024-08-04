class Employee:
    def __init__(self):
        self.__n=None
        self.__na=None
        self.__sal=None
    def set(self,n,na,sal):
        self.__n=n
        self.__na=na
        self.__sal=sal
    def get(self):
        print(f'{self.__n},{self.__na},{self.__sal}')