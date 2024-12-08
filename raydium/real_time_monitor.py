import time
import random

class MarketMonitor:
    def __init__(self, duration=10):
        self.duration = duration
        self.activities = []

    def start_monitoring(self):
        print(f"Starting market monitoring for {self.duration} seconds...")
        for _ in range(self.duration):
            activity = {
                "token": f"Token_{random.randint(1, 10)}",
                "action": random.choice(["buy", "sell"]),
                "volume": random.randint(50, 500),
                "price": round(random.uniform(0.5, 5.0), 2),
            }
            self.activities.append(activity)
            print(f"Logged: {activity}")
            time.sleep(1)

    def summarize_activity(self):
        print("Summarizing market activities...")
        buy_volume = sum(act["volume"] for act in self.activities if act["action"] == "buy")
        sell_volume = sum(act["volume"] for act in self.activities if act["action"] == "sell")
        print(f"Buy volume: {buy_volume}, Sell volume: {sell_volume}")
        return {"buy_volume": buy_volume, "sell_volume": sell_volume}
