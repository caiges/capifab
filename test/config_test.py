from unittest import TestCase

from os import path
import sys

sys.path.append(path.join(path.abspath(path.dirname(__file__)), '..'))

from capifab.config import FabConfig
from fixtures import config

class ConfigParserTest(TestCase):
    
    def setup(self):
        self.capifab_config = file.open(path.join('fixtures', 'config.py'), 'r').read()
    
    def test_valid_config(self):
        print(self.capifab_config)