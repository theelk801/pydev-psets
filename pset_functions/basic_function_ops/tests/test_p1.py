"""
Function Basics I - No Input
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch

from p1 import *
from random import randint

@pytest.mark.describe('it returns ')
def test_rand_list():
	assert rand_list() == randint() * 5