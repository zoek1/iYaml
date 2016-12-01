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


def get_all_kv(yaml_file_loaders):
    """Inspect the instance and collect all kv that encounters"""
    return {}

def flat_hashes(kv):
    """FLat hashes to at 1 level of nested"""
    return kv

def normalize_keys(kv, parent=None):
    """Build a hash where each key part is seperated by one dot.
    If parent is provided change slashes by dots.
    """
    return kv

def build_keys(path):
    keys = {}
    resources = collect_resources(path)

    for path, files in yaml.items():
        for f in files:
            parent = "{}.{}".format(path, os.path.filename(f))
            stream = open(f, 'r')
            sf = load(stream)
            maps = flat_hashes(get_all_kv(sf))

            maps_normalized = normalize_keys(maps, parent=parent)

            keys += maps_normalized

    return keys



def bind(keys,  storage_driver_instance):
    """Takes array where each element correspond to one dict with lang, sections and value keys. One storage driver take this parameters and save it as entry that could be queried."""
    pass
