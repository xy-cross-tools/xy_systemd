# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'ModuleData'
'''
  * @File    :   ModuleData.py
  * @Time    :   2023/06/03 10:36:13
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
'''

from importlib_resources import files
from .BaseModuleData import BaseModuleData
import xy_systemd

class ModuleData(BaseModuleData):

    def __init__(self):
        self.data_path = files(xy_systemd.__name__).joinpath("data")  # type: ignore