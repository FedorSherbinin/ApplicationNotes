class Application:
    def __init__(self, file_storage, note_service, note_controller, note_view):
        self.file_storage = file_storage
        self.note_service = note_service
        self.note_controller = note_controller
        self.note_view = note_view

    def run(self):
        while True:
            print("\n1. Добавить заметку")
            print("2. Просмотреть список заметок")
            print("3. Просмотреть заметку по ID")
            print("4. Фильтр по дате")
            print("5. Редактировать заметку по ID")
            print("6. Удалить заметку по ID")
            print("7. Выйти")

            choice = input("Введите номер команды: ")

            if choice == '1':
                title = input("Введите заголовок заметки: ")
                message = input("Введите тело заметки: ")
                self.note_controller.add_note(title, message)
                self.note_view.success_message('Заметка успешно сохранена')
            elif choice == '2':
                notes = self.note_controller.list_notes()
                self.note_view.list_notes(notes)
            elif choice == '3':
                note_id = int(input("Введите ID заметки: "))
                note = self.note_controller.view_note_by_id(note_id)
                self.note_view.view_note_by_id(note)
            elif choice == '4':
                date = input("Введите дату для фильтрации (в формате YYYY-MM-DD): ")
                notes = self.note_controller.filter_notes_by_date(date)
                self.note_view.list_notes(notes)
            elif choice == '5':
                note_id = int(input("Введите ID заметки для редактирования: "))
                title = input("Введите новый заголовок заметки: ")
                message = input("Введите новое тело заметки: ")
                success = self.note_controller.edit_note_by_id(note_id, title, message)
                if success:
                    self.note_view.success_message('Заметка успешно отредактирована')
                else:
                    self.note_view.success_message('Заметка не найдена')
            elif choice == '6':
                note_id = int(input("Введите ID заметки для удаления: "))
                success = self.note_controller.delete_note_by_id(note_id)
                if success:
                    self.note_view.success_message('Заметка успешно удалена')
                else:
                    self.note_view.success_message('Заметка не найдена')
            elif choice == '7':
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите существующую команду.")
