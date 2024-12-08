import time

class PerformanceTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.records = []

    def start(self):
        print("Starting performance tracking...")
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        self.records.append(duration)
        print(f"Performance tracking stopped. Duration: {duration:.2f} seconds.")

    def get_average_time(self):
        if not self.records:
            print("No performance data available.")
            return 0
        average = sum(self.records) / len(self.records)
        print(f"Average execution time: {average:.2f} seconds.")
        return average
