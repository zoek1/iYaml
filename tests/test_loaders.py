import unittest
import iyaml.loaders as l


class TestRawResources(unittest.TestCase):
    def test_if_one_directory_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile('.'))

    def test_if_non_existing_file_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile("random.yml"))
    
    def test_if_one_yaml_file_resource_is_a_valid_yaml_file(self):
        self.assertTrue(l.isyamlfile('examples/basic.yml'))


if __name__ == '__main__':
    unittest.main()
