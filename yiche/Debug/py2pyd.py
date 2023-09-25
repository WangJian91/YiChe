"""
@Author :guojie 
@Email: jie.guo@msxf.com
@createtime : 2022/9/19 17:10
"""
import os
import shutil
from distutils.core import setup
from Cython.Build import cythonize


class Py2Pyd:
    """
    Py2Pyd("dir_path")  文件夹
    Py2Pyd(["file","file"] 多个文件
    """
    def __init__(self, path, version="1.0.0", author="guojie"):
        self.c_path = "build\lib"
        self.pyd_path = "build\lib.win32-3.7"
        self.extend = "cp37-win32"
        self.path = path
        self.version = version
        self.author = author
        self.root = os.getcwd()
        self.remove_last()
        self.deal_py()
        self.py2pyd()

    @staticmethod
    def remove_last():
        shutil.rmtree("build", ignore_errors=True)

    def deal_py(self):
        print(self.path)
        if isinstance(self.path, list):
            self.path = self.path
        elif isinstance(self.path, str):
            temp_path = []
            print(os.path.exists(self.path))
            for root, dirs, files in os.walk(self.path):

                for file in files:
                    temp_path.append(os.path.join(root, file))
            self.path = temp_path
        print(self.path)

    def py2pyd(self):
        setup(
            version=self.version,
            author=self.author,
            ext_modules=cythonize(self.path, build_dir=self.c_path),
        )
