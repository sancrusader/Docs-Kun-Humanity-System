from web3 import Web3

# Ganti dengan URL endpoint Alchemy Anda
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_API_KEY"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Verifikasi koneksi
if web3.is_connected():
    print("Connected to Alchemy")
else:
    print("Failed to connect to Alchemy")

# Ganti dengan kunci privat MetaMask Anda
private_key = "YOUR_METAMASK_PRIVATE_KEY"

# Ambil alamat dari kunci privat
account = web3.eth.account.privateKeyToAccount(private_key)
print("Account address:", account.address)

# Ganti dengan alamat tujuan
to_address = "0xRecipientAddress"  # Ganti dengan alamat tujuan yang valid

# Membuat transaksi
transaction = {
    'to': to_address,
    'value': web3.toWei(0.1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': web3.eth.getTransactionCount(account.address),
    'chainId': 1  # Mainnet
}

# Tanda tangani transaksi dengan kunci privat
signed_txn = web3.eth.account.signTransaction(transaction, private_key)

# Kirim transaksi
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print("Transaction sent with hash:", web3.toHex(tx_hash))
