class NoteView:
    def list_notes(self, notes):
        if not notes:
            print("Список заметок пуст.")
            return

        for note in notes:
            print(f"{note.get('id')}. {note.get('title')} - {note.get('timestamp')}")

    def view_note_by_id(self, note):
        if note:
            print(f"Заголовок: {note.get('title')}\nТело: {note.get('message')}\nДата/время: {note.get('timestamp')}")
        else:
            print("Заметка не найдена")

    def success_message(self, message):
        print(message)