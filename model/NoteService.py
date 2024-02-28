from datetime import datetime


class NoteService:
    def __init__(self, storage):
        self.storage = storage
        self.notes = self.storage.get_all()
        self.current_id = 1 if not self.notes else max(note.get('id', 0) for note in self.notes) + 1

    def add(self, note):
        note['id'] = self.current_id
        self.current_id += 1
        self.notes.append(note)
        self.storage.save(note)

    def list(self):
        return self.notes

    def get(self, note_id):
        return next((note for note in self.notes if note.get('id') == note_id), None)

    def filter_by_date(self, date):
        return [note for note in self.notes if note['timestamp'].startswith(date)]

    def edit(self, note_id, title, message):
        for note in self.notes:
            if note.get('id') == note_id:
                note['title'] = title
                note['message'] = message
                note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.storage.save_all(self.notes)
                return True
        return False

    def delete(self, note_id):
        filtered_notes = [note for note in self.notes if note.get('id') != note_id]
        if len(filtered_notes) < len(self.notes):
            self.storage.save_all(filtered_notes)
            self.notes = filtered_notes
            return True
        return False