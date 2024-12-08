import time
import random

class TokenScanner:
    def __init__(self):
        self.scanned_tokens = []

    def scan_tokens(self, num_tokens=20):
        print(f"Starting advanced scanning for {num_tokens} tokens...")
        for i in range(num_tokens):
            token = {
                "name": f"Token_{i}",
                "price": round(random.uniform(0.1, 10.0), 2),
                "liquidity": random.randint(500, 5000),
            }
            self.scanned_tokens.append(token)
            print(f"Scanned: {token}")
            time.sleep(0.2)
        return self.scanned_tokens

    def filter_tokens(self, min_liquidity=1000):
        print(f"Filtering tokens with liquidity > {min_liquidity}...")
        filtered = [token for token in self.scanned_tokens if token["liquidity"] > min_liquidity]
        print(f"Filtered {len(filtered)} tokens out of {len(self.scanned_tokens)}.")
        return filtered

    def find_high_potential_tokens(self, price_range=(1.0, 5.0)):
        print(f"Finding tokens in price range {price_range}...")
        high_potential = [
            token for token in self.scanned_tokens
            if price_range[0] <= token["price"] <= price_range[1]
        ]
        print(f"Found {len(high_potential)} high-potential tokens.")
        return high_potential
