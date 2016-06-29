from typing import List

from decorators import singleton
from exceptions import WrongTransactionException
from input import AbstractInput
from output import AbstractOutput


class AbstractTransaction(object):
    @property
    def txid(self) -> str:
        raise NotImplementedError()


@singleton
class StartTransaction(AbstractTransaction):
    def __init__(self, outputs: List[AbstractOutput], version: int = 0) -> None:
        if len(outputs) == 0:
            raise WrongTransactionException("Start transaction should have at least one output")

        self.__version = version
        self.__outputs = outputs

    @property
    def txid(self) -> str:
        return ""


class Transaction(AbstractTransaction):
    def __init__(self, inputs: List[AbstractInput], outputs: List[AbstractOutput], version: int = 0) -> None:
        if len(inputs) == 0:
            raise WrongTransactionException("Transaction should have at least one input")

        if len(outputs) == 0:
            raise WrongTransactionException("Transaction should have at least one output")

        self.__version = version
        self.__inputs = inputs
        self.__outputs = outputs

    @property
    def txid(self) -> str:
        return ""
