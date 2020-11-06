from abc import abstractmethod,ABCMeta



class Adapter():
    __metaclass__ = ABCMeta

    def __init__(self): pass

    @abstractmethod
    def getLogFormat(self): pass

    @abstractmethod
    def parse(self): pass

    @abstractmethod
    def getLogFormatByConfStr(self): pass