from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        ...

    @abstractmethod
    def pop_back(self):
        ...

class StackObj:

    def __init__(self, data, next_obj=None):
        self._data = data
        self._next = next_obj
    

class Stack(StackInterface):

    def __init__(self):
        self._top = None


    def push_back(self, obj):
        obj._next = self.top
        self._top = obj

    
    def pop_back(self):
        if self._top:
            res = self._top
            self.top = self._top._next
            return res
        return None
