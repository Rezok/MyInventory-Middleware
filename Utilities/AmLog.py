import logging
class AmLog:
    def __init__(self):
        self.log_path = "%appdata%\\MyInventory Middleware\\"
        self.AmLoger = logging.getLogger("Amloger")