#!/usr/bin/python3
"""
    create a unique 'FileStorage' instance for the application
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

create_instance = { 'BaseModel': BaseModel }

storage = FileStorage()
storage.reload()
