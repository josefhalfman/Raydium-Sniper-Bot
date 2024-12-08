import tkinter as tk
from gui.settings import SettingsWindow
from gui.logger import LoggerWindow

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Raydium Sniper Bot")
        self.root.geometry("900x700")
        self._setup_ui()

    def _setup_ui(self):
        tk.Button(self.root, text="Settings", command=self.open_settings).pack(pady=10)
        tk.Button(self.root, text="Logs", command=self.open_logs).pack(pady=10)
        tk.Button(self.root, text="Start Sniping", command=self.start_sniping).pack(pady=10)
        tk.Button(self.root, text="Stop Sniping", command=self.stop_sniping).pack(pady=10)

    def open_settings(self):
        SettingsWindow()

    def open_logs(self):
        LoggerWindow()

    def start_sniping(self):
        print("Sniping started")

    def stop_sniping(self):
        print("Sniping stopped")

    def run(self):
        self.root.mainloop()
