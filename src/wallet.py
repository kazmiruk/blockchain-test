from ecdsa import SECP256k1, SigningKey
from pip.utils import cached_property


class AbstractWallet(object):
    pass


class Wallet(AbstractWallet):
    def __init__(self, private_string: str = None) -> None:
        if private_string is not None:
            self.__signing_key = SigningKey.from_string(private_string, curve=SECP256k1, hashfunc='sha256')
        else:
            self.__signing_key = SigningKey.generate(curve=SECP256k1, hashfunc='sha256')
        self.__verification_key = self.__signing_key.get_verifying_key()

    @cached_property
    def public_key(self) -> str:
        return self.__verification_key.to_pem()

    @cached_property
    def private_key(self) -> str:
        return self.__signing_key.to_pem()

    def save(self, private_path: str, public_path: str) -> None:
        open(private_path, "wb").write(self.private_key)
        open(public_path, "wb").write(self.public_key)
