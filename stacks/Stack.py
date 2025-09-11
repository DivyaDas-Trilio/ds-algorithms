from abc import ABC, abstractmethod
import typing

class IStack(ABC):
    @abstractmethod
    def push(self, o: object): pass
    
    @abstractmethod
    def pop(self): pass
    
    @abstractmethod
    def _is_empty(self): pass
    
    @abstractmethod
    def _is_full(self): pass
    
    @abstractmethod
    def print_stack(self): pass
    
class SimpleStack(IStack):
    def __init__(self, size):
        self.__size: int = size
        self.__stack: typing.List = []
        self.__stackpointer = -1
        
    @typing.override
    def _is_empty(self)-> bool:
        if(self.__stackpointer == -1):
            return True
        return False
    
    @typing.override
    def _is_full(self) -> bool:
        if(self.__stackpointer >= self.__size - 1):
            return False
        return True
    
    @typing.override
    def push(self, o: object) -> bool:
        if(self._is_full()):
            self.__stack.append(o)
            self.__stackpointer += 1
            return True
        raise Exception("Stack Overflow Exception.")
    
    @typing.override
    def print_stack(self):
        for each in self.__stack:
            print(each, end=" ")
    
    @typing.override
    def pop(self) -> None:
        if(self._is_empty()):
            raise Exception("Stack Underflow.")
        self.__stack.pop()
    
# Driver code.
if __name__ == "__main__":
    ss = SimpleStack(5)
    while True:
        item = input("Enter item to put in Stack:- ")
        # ss.push(item)
        ss.pop()
        ss.print_stack()