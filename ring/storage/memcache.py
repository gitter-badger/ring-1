
from __future__ import absolute_import

from .base import BaseStorage


class MemcacheStorage(BaseStorage):

    def __init__(self, storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get(key)

    def update(self, key, value, expire=None):
        return self.storage.update(value, time=expire)
