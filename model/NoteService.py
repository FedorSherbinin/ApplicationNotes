class NoteService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, note):
        self.storage.save(note)

    def list(self):
        return self.storage.get_all()

    def get(self, note_id):
        return self.storage.get_by_id(note_id)

    def filter_by_date(self, date):
        return self.storage.filter_by_date(date)

    def edit(self, note_id, title, message):
        success = self.storage.update(note_id, title, message)
        if success:
            self.save_all()  # Добавлена автоматическая сохранение при редактировании
        return success

    def delete(self, note_id):
        success = self.storage.delete(note_id)
        if success:
            self.save_all()  # Добавлена автоматическая сохранение при удалении
        return success

    def save_all(self):
        self.storage.save_all()