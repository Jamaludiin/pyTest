import pytest
#from pyTest.message_util import MessageUtil
from message_util import MessageUtil

class TestMessageUtil:
    def test_print_message(self):
            message = "Hello World"
            message_util = MessageUtil(message)
            assert message_util.print_message() == message
        
    def test_salutation_message(self):
        message = " Python"
        message_util = MessageUtil(message)
        assert message_util.salutation_message() == "Hi! Python"


# test_message_util.py