from pathlib import Path


class FakePath(Path):

    def __init__(self, filepath : str, exists : bool = True):
        super().__init__(filepath)
        self._exists = exists

    def exists(self):
        return self._exists
