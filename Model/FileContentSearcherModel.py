from Utilities.AmConfig import AmConfig
import ast
"""
    CURRENT_VERSION: 1.0
    AUTHOR: Jakub Pankiewicz
    DESCRIPTION: This is model of FileContentSearcher module.

    **CHANGELOG**
    12.07.2024 |1.0| - Create FileContentSearcher model.
"""


class FileContentSearcherModel:
    def __init__(self):
        self.amconfig = AmConfig()
        self.servers = self.amconfig.config["App Config"]["servers"]
        self._files = []

    def get_servers(self):
        self.servers = ast.literal_eval(self.servers)
        return self.servers

    def get_files_list(self):
        return self._files

    def add_files_to_list(self, file):
        self._files.append(file)
