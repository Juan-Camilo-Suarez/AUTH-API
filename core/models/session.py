from datetime import datetime


class Session:
    def __init__(self, expiration_time, creation_time, metadata):
        self.expiration_time = expiration_time
        self.creation_time = creation_time
        self.metadata = metadata

    def validate(self):
        return True
