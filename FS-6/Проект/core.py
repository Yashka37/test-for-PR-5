from pathlib import Path
import shutil


class FileManager:
    def __init__(self, base_dir):
        self.base = Path(base_dir).expanduser().resolve()
        self.base.mkdir(parents=True, exist_ok=True)
        self.current = self.base

    def _path(self, value=""):
        target = (self.current / value).resolve()
        try:
            target.relative_to(self.base)
        except ValueError:
            raise ValueError("Выход за пределы рабочей папки запрещен")
        return target

    def prompt_path(self):
        rel = self.current.relative_to(self.base)
        return "/" if str(rel) == "." else "/" + str(rel).replace("\\", "/")

    def list_items(self):
        items = sorted(self.current.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        if not items:
            return "Папка пустая"
        return "\n".join(("[D] " if p.is_dir() else "[F] ") + p.name for p in items)

    def make_folder(self, name):
        self._path(name).mkdir(exist_ok=True)
        return "Папка создана"

    def drop_folder(self, name):
        self._path(name).rmdir()
        return "Папка удалена"

    def into(self, name):
        target = self._path(name)
        if not target.is_dir():
            raise ValueError("Папка не найдена")
        self.current = target
        return self.prompt_path()

    def back(self):
        if self.current != self.base:
            self.current = self.current.parent
        return self.prompt_path()

    def new_file(self, name):
        self._path(name).touch(exist_ok=True)
        return "Файл создан"

    def write_file(self, name, text):
        self._path(name).write_text(text, encoding="utf-8")
        return "Текст записан"

    def read_file(self, name):
        return self._path(name).read_text(encoding="utf-8")

    def drop_file(self, name):
        self._path(name).unlink()
        return "Файл удален"

    def copy_file(self, src, folder):
        source = self._path(src)
        target_dir = self._path(folder)
        if not source.is_file():
            raise ValueError("Исходный файл не найден")
        if not target_dir.is_dir():
            raise ValueError("Папка назначения не найдена")
        shutil.copy2(source, target_dir / source.name)
        return "Файл скопирован"

    def move_file(self, src, folder):
        source = self._path(src)
        target_dir = self._path(folder)
        if not source.is_file():
            raise ValueError("Исходный файл не найден")
        if not target_dir.is_dir():
            raise ValueError("Папка назначения не найдена")
        shutil.move(str(source), str(target_dir / source.name))
        return "Файл перемещен"

    def name_file(self, old, new):
        self._path(old).rename(self._path(new))
        return "Файл переименован"
