from typing import List
from random import randint

from decorators import singleton
from exceptions import UselessBlockException
from transaction import AbstractTransaction
from utils import get_hash


class AbstractBlock(object):
    def get_header_hash(self) -> str:
        raise NotImplementedError()


@singleton
class StartBlock(AbstractBlock):
    def __init__(self, transactions: List[AbstractTransaction]) -> None:
        self.chain_seed = str(randint(0, 1000000000))
        self.__transactions = transactions

    def get_header_hash(self) -> str:
        return get_hash(self.chain_seed)


class Block(AbstractBlock):
    __transactions = []
    __previous_block_hash = None

    def __init__(self, previous_block: AbstractBlock, transactions: List[AbstractTransaction]) -> None:
        if len(transactions) == 0:
            raise UselessBlockException()

        self.__transactions = transactions
        self.__previous_block_hash = previous_block.get_header_hash()

    @property
    def __merkle_root(self) -> str:
        def __do_iteration(data: List[str]) -> str:
            new_data = []
            len_data = len(data)

            for i in range(0, len_data, 2):
                row = data[i]

                if (i + 1) == len_data:
                    row += data[i]
                else:
                    row += data[i + 1]

                new_data.append(get_hash(row))

            if len(new_data) == 1:
                return new_data[0]

            return __do_iteration(new_data)

        return __do_iteration([el.txid for el in self.__transactions])

    def get_header_hash(self) -> str:
        return get_hash(self.__previous_block_hash + self.__merkle_root)
