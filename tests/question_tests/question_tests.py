#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions

from src.question_b.question_b import use_global, change_global

class Test_Config(unittest.TestCase):

    def test_question_c_config(self):
        self.assertEqual(change_global (10), 5)




