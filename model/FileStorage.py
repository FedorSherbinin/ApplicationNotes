import json
from datetime import datetime


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.current_id = self._load_current_id()  # Загружаем текущий id при инициализации

    def _load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_notes(self, notes):
        with open(self.file_path, 'w') as file:
            json.dump(notes, file, indent=2)

    def _load_current_id(self):
        try:
            with open('current_id.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 1

    def _save_current_id(self, current_id):
        with open('current_id.txt', 'w') as file:
            file.write(str(current_id))

    def save(self, note):
        notes = self._load_notes()
        note_data = {
            'id': self.current_id,
            'title': note.title,
            'message': note.message,
            'timestamp': note.timestamp
        }
        notes.append(note_data)
        self._save_notes(notes)
        self.current_id += 1
        self._save_current_id(self.current_id)

    def save_all(self):
        notes = self._load_notes()
        self._save_notes(notes)

    def get_all(self):
        return self._load_notes()

    def get_by_id(self, note_id):
        for note in self._load_notes():
            if note['id'] == note_id:
                return note
        return None

    def filter_by_date(self, date):
        return [note for note in self._load_notes() if note['timestamp'].startswith(date)]

    def update(self, note_id, title, message):
        notes = self._load_notes()
        for note in notes:
            if note['id'] == note_id:
                note['title'] = title
                note['message'] = message
                note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self._save_notes(notes)
                return True
        return False

    def delete(self, note_id):
        notes = self._load_notes()
        filtered_notes = [note for note in notes if note['id'] != note_id]
        if len(filtered_notes) < len(notes):
            self._save_notes(filtered_notes)
            return True
        return False
