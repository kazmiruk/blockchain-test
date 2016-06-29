class AbstractInput(object):
    pass


class Input(AbstractInput):
    def __init__(self, previous_txid, output_index, script_sig):
        self.__previous_txid = previous_txid
        self.__output_index = output_index
        self.__script_sig = script_sig
