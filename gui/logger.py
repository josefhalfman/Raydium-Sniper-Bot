import tkinter as tk

class LoggerWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Logs")
        self.window.geometry("700x500")
        self._setup_ui()

    def _setup_ui(self):
        self.text_area = tk.Text(self.window, state="disabled")
        self.text_area.pack(expand=True, fill="both")
        self.load_logs()

    def load_logs(self):
        self.text_area.config(state="normal")
        self.text_area.insert("1.0", "Logs will be displayed here.")
        self.text_area.config(state="disabled")
