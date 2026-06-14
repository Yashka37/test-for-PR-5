from config import BASE_DIR
from core import FileManager

HELP = """
Команды:
help                                  справка
where                                 текущая папка
list                                  список объектов
make-folder <name>                    создать папку
drop-folder <name>                    удалить пустую папку
into <name>                           перейти в папку
back                                  выйти на уровень выше
new-file <name>                       создать пустой файл
write-file <name> <text>              записать текст в файл
read-file <name>                      вывести содержимое файла
drop-file <name>                      удалить файл
copy-file <file> <folder>             скопировать файл в папку
move-file <file> <folder>             переместить файл в папку
name-file <old> <new>                 переименовать файл
quit                                  выход
""".strip()


def main():
    manager = FileManager(BASE_DIR)
    print("Simple File Manager")
    print("Рабочая папка:", manager.base)
    print("Введите help для просмотра команд")

    while True:
        try:
            line = input(f"fm:{manager.prompt_path()} > ").strip()
            if not line:
                continue

            parts = line.split(maxsplit=2)
            cmd = parts[0]

            if cmd == "help":
                print(HELP)
            elif cmd == "where":
                print(manager.prompt_path())
            elif cmd == "list":
                print(manager.list_items())
            elif cmd == "make-folder" and len(parts) >= 2:
                print(manager.make_folder(parts[1]))
            elif cmd == "drop-folder" and len(parts) >= 2:
                print(manager.drop_folder(parts[1]))
            elif cmd == "into" and len(parts) >= 2:
                print(manager.into(parts[1]))
            elif cmd == "back":
                print(manager.back())
            elif cmd == "new-file" and len(parts) >= 2:
                print(manager.new_file(parts[1]))
            elif cmd == "write-file" and len(parts) == 3:
                print(manager.write_file(parts[1], parts[2]))
            elif cmd == "read-file" and len(parts) >= 2:
                print(manager.read_file(parts[1]))
            elif cmd == "drop-file" and len(parts) >= 2:
                print(manager.drop_file(parts[1]))
            elif cmd == "copy-file" and len(parts) == 3:
                print(manager.copy_file(parts[1], parts[2]))
            elif cmd == "move-file" and len(parts) == 3:
                print(manager.move_file(parts[1], parts[2]))
            elif cmd == "name-file" and len(parts) == 3:
                print(manager.name_file(parts[1], parts[2]))
            elif cmd == "quit":
                break
            else:
                print("Команда не распознана")
        except Exception as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
