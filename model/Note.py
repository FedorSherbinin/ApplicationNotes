from datetime import datetime

class Note:
    current_id = None  # Нам не нужен текущий счетчик здесь

    def __init__(self, title, message):
        self.id = None  # Мы устанавливаем id позже
        self.title = title
        self.message = message
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
