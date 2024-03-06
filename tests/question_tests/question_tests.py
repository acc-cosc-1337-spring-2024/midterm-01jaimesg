#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions

from src.question_d.question_d import get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_question_c_config(self):
        self.assertEqual(get_miles_per_hour (32), 19.883872)




