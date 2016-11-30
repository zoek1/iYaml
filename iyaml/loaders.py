from yaml import load, dump
import re
import os

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper


YAML_EXTENSIONS = ['yml', 'yaml']

def isyamlfile(path):
    """Validate if the path refer to one yaml file"""
    base = '^.*\.({})$'
    extensions = '|'.join(YAML_EXTENSIONS)
    yml_re = re.compile(base.format(extensions))

    if os.path.isfile(os.path.abspath(path)) and yml_re.match(path):            return True

    return False


def seed():
    for root, dirs, files in os.walk(i18N_PATH):
        try:
            yaml_files = filter(lambda file: file, files)
        except FileNotFoundError as e:
            pass


def transform():
    pass
