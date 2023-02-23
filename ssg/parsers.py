from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []
    def valid_extension(self, extension):
        return extension in self.extensions
    def parse(path: Path, source: Path, dest: Path):
        raise NotImplementedError()
    def read(path):
        with open(path) as file:
            return file
    def write(path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext)