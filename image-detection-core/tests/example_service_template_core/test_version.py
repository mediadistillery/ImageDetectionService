import pathlib

import toml

from image_detection_core.version import __version__


def test_versions_are_in_sync():
    path = pathlib.Path(__file__).resolve().parents[2] / 'pyproject.toml'
    with open(str(path)) as f:
        pyproject = toml.loads(f.read())
    pyproject_version = pyproject['tool']['poetry']['version']
    assert __version__ == pyproject_version
