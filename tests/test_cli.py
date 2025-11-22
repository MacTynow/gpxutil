import hashlib
import os
from typer.testing import CliRunner

from ..gpxutil.cli import app

runner = CliRunner()
test_data_path = os.getcwd() + "/tests/test_data/"


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.output.strip("\n") == "v0.2.0"
    assert result.exit_code == 0


def test_merge():    
    with open(test_data_path + "merged_good.sha256sum", 'r') as f:
      file_good_sha256sum = f.readline()

    result = runner.invoke(app, ["merge", test_data_path + "activity_1.gpx", test_data_path + "activity_2.gpx"])

    assert file_hash("./merged.gpx") == file_good_sha256sum
    assert result.exit_code == 0
    
def file_hash(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()