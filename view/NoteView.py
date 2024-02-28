class NoteView:
    def list_notes(self, notes):
        for note in notes:
            print(f"{note['id']}. {note['title']} - {note['timestamp']}")

    def view_note_by_id(self, note):
        if note:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТело: {note['message']}\nДата/время: {note['timestamp']}")
        else:
            print("Заметка не найдена")

    def success_message(self, message):
        print(message)
