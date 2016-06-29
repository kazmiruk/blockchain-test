class BlockChainException(Exception):
    message = "Internal error in blockchain element"


class UselessBlockException(BlockChainException):
    message = "Creating of useless block (without transactions)"


class TransactionException(Exception):
    message = "Internal error in transaction element"


class WrongTransactionException(TransactionException):
    message = "Invalid transaction initiation"


class WrongOutputValueException(TransactionException):
    message = "Wrong output value for transaction (should be more than 0)"
