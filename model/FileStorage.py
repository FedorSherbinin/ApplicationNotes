import json

class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_notes(self, notes):
        with open(self.file_path, 'w') as file:
            json.dump(notes, file, indent=2)

    def save(self, note):
        notes = self._load_notes()
        notes.append(note)
        self._save_notes(notes)

    def save_all(self, notes):
        self._save_notes(notes)

    def get_all(self):
        return self._load_notes()

    def filter_by_date(self, date):
        return [note for note in self._load_notes() if note['timestamp'].startswith(date)]