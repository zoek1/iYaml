from yaml import load, dump
import re
import os

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper


YAML_EXTENSIONS = ['yml', 'yaml']


def isyamlfile(path):
    """Validate if the path refers to one yaml file"""

    base = '^.*\.({})$'
    extensions = '|'.join(YAML_EXTENSIONS)

    yml_re = re.compile(base.format(extensions))

    if os.path.isfile(os.path.abspath(path)) and yml_re.match(path):            return True

    return False


def collect_resources(yaml_dir='locales'):
    """Build a base dict with all valid yaml files"""
    roots = {}

    for root, dirs, files in os.walk(yaml_dir):
        try:
            yaml_files = [yf for yf in files
                          if isyamlfile(os.path.join(root, yf))]

            if len(yaml_files) > 0:
                roots[root] = yaml_files
        except FileNotFoundError as e:
            pass

    return roots


def transform(roots, storage_driver):
    pass
