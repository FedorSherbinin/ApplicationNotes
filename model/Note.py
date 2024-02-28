from datetime import datetime

class Note:
    def __init__(self, title, message, timestamp=None):
        self.title = title
        self.message = message
        self.timestamp = timestamp or datetime.now().strftime('%Y-%m-%d %H:%M:%S')