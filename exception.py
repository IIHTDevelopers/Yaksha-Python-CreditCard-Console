
class CardNumberAlreadyExistsError(Exception):
    def __init__(self,message):
        self.message=message

class CardBlockedError(Exception):
    def __init__(self,message):
        self.message=message

class CardNumberDoesNotExistsError(Exception):
    def __init__(self,message):
        self.message=message

class InvalidAmountError(Exception):
    def __init__(self,message):
        self.message=message

class AmountNotAvailableError(Exception):
    def __init__(self,message):
        self.message=message

class InsufficientBalanceError(Exception):
    def __init__(self,message):
        self.message=message
