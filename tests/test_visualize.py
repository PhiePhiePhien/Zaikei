import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import json
from pathlib import Path
from project.src import visualize


def test_visualize(tmp_path: Path):
    data = {'predictions':[1,2,3]}
    json_path = tmp_path / 'input.json'
    with json_path.open('w') as f:
        json.dump(data, f)
    out_dir = tmp_path / 'out'
    visualize.main(json_path, out_dir)
    assert (out_dir / 'prediction.csv').exists()
    assert (out_dir / 'prediction.png').exists()
