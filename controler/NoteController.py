from datetime import datetime

class NoteController:
    def __init__(self, note_service):
        self.note_service = note_service

    def add_note(self, title, message):
        note = {'title': title, 'message': message, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.note_service.add(note)

    def list_notes(self):
        return self.note_service.list()

    def view_note_by_id(self, note_id):
        return self.note_service.get(note_id)

    def filter_notes_by_date(self, date):
        return self.note_service.filter_by_date(date)

    def edit_note_by_id(self, note_id, title, message):
        return self.note_service.edit(note_id, title, message)

    def delete_note_by_id(self, note_id):
        return self.note_service.delete(note_id)
