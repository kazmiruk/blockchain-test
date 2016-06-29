from block import StartBlock
from output import Output
from transaction import StartTransaction
from wallet import Wallet


start_wallet = Wallet()
start_wallet.save("private.pem", "public.pem")
start_output = Output(100, start_wallet.public_key)
start_transaction = StartTransaction(outputs=[start_output])
start_block = StartBlock(transactions=[start_transaction])

