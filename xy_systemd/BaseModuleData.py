# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'BaseModuleData'
'''
  * @File    :   BaseModuleData.py
  * @Time    :   2023/06/06 20:21:48
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
'''

from importlib.abc import Traversable
from pathlib import Path
from .utils import is_empty_string


class BaseModuleData:
    template_suffix = ".template"
    data_path: Path | Traversable | None = None
    root_path = Path.cwd()

    def __init__(self):
        pass

    def make_data_template(self, name: str) -> Path | Traversable | None:
        return self.make_data_path(
            name,
            suffix=self.template_suffix,
        )

    def make_data_path(self, name: str, suffix: str) -> Path | Traversable | None:
        return self.make_path(name, suffix, self.data_path)

    def make_path(
        self, name: str, suffix: str, root_path: Path | Traversable | None
    ) -> Path | Traversable | None:
        if isinstance(root_path, Path) or isinstance(root_path, Traversable):
            return root_path.joinpath(f"{name}{suffix}")
        return None

    def src_path(self, module_name: str | None):
        if (
            self.root_path
            and not is_empty_string(module_name)
            and isinstance(module_name, str)
        ):
            return self.root_path.joinpath(module_name)
        return None

    def make_src_path(self, module_name: str | None, file_name: str):
        src_path = self.src_path(module_name)
        if src_path and not is_empty_string(file_name) and isinstance(file_name, str):
            return src_path.joinpath(file_name)
        return None

    def write(self, filepath: Path | None, content: str | None):
        if filepath and not filepath.exists():
            if not filepath.parent.exists():
                filepath.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )
            filepath.touch()
            if filepath and filepath.exists():
                filepath.write_text(str(content), encoding="utf-8")
