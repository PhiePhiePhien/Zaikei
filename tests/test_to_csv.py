import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import json
from pathlib import Path
from project.src import to_csv


def test_to_csv(tmp_path: Path):
    raw_dir = tmp_path / 'raw'
    raw_dir.mkdir()
    data = [{'a':1,'b':2}]
    with (raw_dir / 'raw_20220101.json').open('w') as f:
        json.dump(data, f)
    to_csv.main(raw_dir, raw_dir)
    csv_files = list(raw_dir.glob('stock_data_*.csv'))
    assert csv_files
