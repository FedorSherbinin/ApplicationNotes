from model.Note import Note


class NoteController:
    def __init__(self, note_service):
        self.note_service = note_service

    def add_note(self, title, message):
        self.note_service.add(Note(title, message))

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

    def save_notes(self):
        self.note_service.save_all()
