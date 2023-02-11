from contentscanner.exceptions.exceptions import *
from contentscanner.ContentScanner import ContentScanner
import os


def __current_path():
    return os.path.dirname(os.path.abspath(__file__))


def __wordlist_test_path():
    return os.path.join(__current_path(), '..', 'tests', 'wordlist_test.txt')


def __get_wordlist():
    with open(__wordlist_test_path(), "r") as file:
        return file.read().splitlines()


def test_wordlist():
    try:
        contentscanner = ContentScanner(
            'https://www.google.it', __wordlist_test_path()
        )
    except ExceptionGetWordlist:
        assert False
    else:
        assert True


def test_check_url():
    contentscanner = ContentScanner(
        'https://www.google.it', __wordlist_test_path()
    )
    try:
        contentscanner.scan()
    except ExceptionUrl:
        assert False
    else:
        assert True
