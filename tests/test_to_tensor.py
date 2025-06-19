import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pathlib import Path
import pandas as pd
from project.src import to_tensor

def test_tensor_creation(tmp_path: Path):
    df = pd.DataFrame({'a':[1,2],'b':[3,4]})
    csv = tmp_path / 'stock_data_20220101_week01.csv'
    df.to_csv(csv, index=False)
    tensor_dir = tmp_path / 'out'
    to_tensor.main(tmp_path, tensor_dir)
    assert (tensor_dir / 'data_tensor.pt').exists()
