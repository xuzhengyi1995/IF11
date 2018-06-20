import os
import sys
import json
import warnings
import argparse

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.recognize import MicrophoneRecognizer

DEFAULT_CONFIG_FILE = "./main/dejavu.cnf"


class musicProcessor:
    def __init__(self):
        with open(DEFAULT_CONFIG_FILE) as f:
            config = json.load(f)
        # create a Dejavu instance
        self.processor = Dejavu(config)

    def fp_file(self, _filepath, _songname):
        self.processor.fingerprint_file(filepath=_filepath, song_name=_songname)
        return True

    def reg_file(self, _filepath):
        return self.processor.recognize(FileRecognizer, _filepath)
