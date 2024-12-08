import random

class TransactionSimulator:
    def __init__(self, token, num_transactions=10):
        self.token = token
        self.num_transactions = num_transactions
        self.transactions = []

    def simulate(self):
        print(f"Simulating {self.num_transactions} transactions for {self.token}...")
        for _ in range(self.num_transactions):
            transaction = {
                "token": self.token,
                "type": random.choice(["buy", "sell"]),
                "amount": random.randint(5, 50),
                "price": round(random.uniform(0.2, 2.0), 2),
            }
            self.transactions.append(transaction)
            print(f"Transaction simulated: {transaction}")
        return self.transactions

    def analyze_transactions(self):
        print("Analyzing transactions...")
        total_buys = sum(tx["amount"] * tx["price"] for tx in self.transactions if tx["type"] == "buy")
        total_sells = sum(tx["amount"] * tx["price"] for tx in self.transactions if tx["type"] == "sell")
        net = total_sells - total_buys
        print(f"Total buys: {total_buys}, Total sells: {total_sells}, Net: {net}")
        return {"total_buys": total_buys, "total_sells": total_sells, "net": net}
