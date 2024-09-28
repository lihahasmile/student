from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

# TODO: Fill this in with your private key.
my_private_key = CBitcoinSecret(
    'cSkiv2NN78J7c2ubGbXZryeyw81syKnX1AcGC6B2QDM18jsJvfCZ')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

faucet_address = CBitcoinAddress('tb1qerzrlxcfu24davlur5sqmgzzgsal6wusda40er')
