import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from project.src import fetch_data

def test_parse_table_empty():
    html = "<html></html>"
    assert fetch_data.parse_table(html) == []
