from exceptions import WrongOutputValueException


class AbstractOutput(object):
    pass


class Output(AbstractOutput):
    def __init__(self, value: float, script_pub_sig: str) -> None:
        if value <= 0:
            raise WrongOutputValueException()

        self.__value = value
        self.__script_pub_sig = script_pub_sig
