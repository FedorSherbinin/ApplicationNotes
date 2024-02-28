from application.Application import Application
from controler.NoteController import NoteController
from model.FileStorage import FileStorage
from model.NoteService import NoteService
from view.NoteView import NoteView

if __name__ == "__main__":
    file_storage = FileStorage('notes.json')
    note_service = NoteService(file_storage)
    note_controller = NoteController(note_service)
    note_view = NoteView()

    app = Application(file_storage, note_service, note_controller, note_view)
    app.run()