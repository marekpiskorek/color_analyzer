#!/usr/bin/env python
import subprocess


def test_empty_dir():
    result = subprocess.check_output(['python', 'analyzer.py'])
    assert result == '>>> There are no image files!\n'


def test_two_images():
    result = subprocess.check_output(['python', 'analyzer.py', 'data/'])
    assert result.split('\n') == [
        '>>> data/magical.png:', '> red', '> black', '> white',
        '>>> data/all-the-sweaters.jpg:', '> white', '> black', '> red', ''
    ]
