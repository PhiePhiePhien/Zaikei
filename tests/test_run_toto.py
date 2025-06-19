import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import torch
from pathlib import Path
from project.src import run_toto


def test_dummy_predict(tmp_path: Path):
    tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    pt = tmp_path / 'data.pt'
    torch.save(tensor, pt)
    out = tmp_path / 'res.json'
    run_toto.main(pt, out)
    assert out.exists()
