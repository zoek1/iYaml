import unittest
import iyaml.loaders as l


class TestRawResources(unittest.TestCase):
    def test_if_one_directory_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile('.'))

    def test_if_non_existing_file_is_a_valid_yaml_file(self):
        self.assertFalse(l.isyamlfile("random.yml"))

    def test_if_one_yaml_file_resource_is_a_valid_yaml_file(self):
        self.assertTrue(l.isyamlfile('examples/basic.yml'))



class TestFileCollector(unittest.TestCase):
    def test_if_directory_no_collect_yaml_files(self):
        self.assertEqual(l.collect_resources('test'), {})

        self.assertEqual(l.collect_resources('/tmp'), {})


    def test_if_directory_collect_yaml_files(self):
        self.assertEqual(len(l.collect_resources('examples').keys()), 1)
        self.assertEqual(len(l.collect_resources('examples').values()), 1)


if __name__ == '__main__':
    unittest.main()
