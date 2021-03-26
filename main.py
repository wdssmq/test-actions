import os

_file_changes = ""

try:
    if(os.environ["_file_changes"]):
        _file_changes = os.environ["_file_changes"]
except:
    print(_file_changes)
print(_file_changes)