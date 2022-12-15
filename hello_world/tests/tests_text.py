from django.test import TestCase

from hello_world.utils.textUtils import (
# festi.utils.text import (
    ##extract_ip_addr_from_string, slugify,
    split_name
    ##strict_camelize,
    ##strip_prefix,
)

# Create your tests here.
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)

    # def test_split_name(self):
    # self.assert split_name("  Agi  Pain  ") == ("Agi", "Pain")
    # assert split_name(" Agi  ") == ("Agi", "")
    # assert split_name("Agi Pain in my ass") == ("Agi", "Pain in my ass")


# from django.test import TestCase

# from hello_world.utils.textUtils import (
# # festi.utils.text import (
#     ##extract_ip_addr_from_string, slugify,
#     split_name
#     ##strict_camelize,
#     ##strip_prefix,
# )

# class YourTestClass(TestCase):
#         def setUp(self):
#         # Setup run before every test method.
#         pass

#     def tearDown(self):
#         # Clean up run after every test method.
#         pass
# def test_split_name():
#     assert split_name("  Agi  Pain  ") == ("Agi", "Pain")
#     assert split_name(" Agi  ") == ("Agi", "")
#     assert split_name("Agi Pain in my ass") == ("Agi", "Pain in my ass")