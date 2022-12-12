import pytest
import json
from logic.fixtures import *


@pytest.fixture(scope='class')
def config():
    with open('config.json', 'r') as file:
        config_json = json.load(file)
    return config_json
