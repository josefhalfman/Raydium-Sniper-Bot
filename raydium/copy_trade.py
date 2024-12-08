import time
from solana.rpc.api import Client
from solana.transaction import Transaction, Account

class CopyTrade:
    def __init__(self, rpc_url, monitored_address, user_wallet, user_private_key):
        self.client = Client(rpc_url)
        self.monitored_address = monitored_address
        self.user_wallet = user_wallet
        self.user_private_key = user_private_key
        self.last_transaction_signature = None

    def monitor_transactions(self):
        print(f"Monitoring transactions for address: {self.monitored_address}...")
        while True:
            try:
                transaction = self._fetch_latest_transaction()
                if transaction:
                    print(f"New transaction detected: {transaction}")
                    self._copy_transaction(transaction)
            except Exception as e:
                print(f"Error monitoring transactions: {e}")
            time.sleep(2)  # Polling interval

    def _fetch_latest_transaction(self):
        try:
            confirmed_transactions = self.client.get_signatures_for_address(self.monitored_address, limit=1)
            if not confirmed_transactions["result"]:
                return None

            latest_transaction = confirmed_transactions["result"][0]
            signature = latest_transaction["signature"]

            if signature == self.last_transaction_signature:
                return None  # No new transaction

            self.last_transaction_signature = signature

            transaction_details = self.client.get_transaction(signature)
            return transaction_details["result"]

        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return None

    def _copy_transaction(self, transaction):
        try:
            instructions = transaction["transaction"]["message"]["instructions"]

            tx = Transaction()
            for instruction in instructions:
                tx.add(instruction)

            account = Account(bytes.fromhex(self.user_private_key))
            response = self.client.send_transaction(tx, account)

            print(f"Copied transaction to user wallet: {response}")
        except Exception as e:
            print(f"Error copying transaction: {e}")

if __name__ == "__main__":
    RPC_URL = "https://api.mainnet-beta.solana.com"  # Replace with your RPC URL
    MONITORED_ADDRESS = "MonitoredPublicAddress"  # Replace with the monitored wallet address
    USER_WALLET = "UserPublicAddress"  # Replace with the user's wallet address
    USER_PRIVATE_KEY = "UserPrivateKey"  # Replace with the user's private key in hex format

    copy_trade_bot = CopyTrade(RPC_URL, MONITORED_ADDRESS, USER_WALLET, USER_PRIVATE_KEY)
    copy_trade_bot.monitor_transactions()
