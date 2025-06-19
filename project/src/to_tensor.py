import argparse
import logging
from pathlib import Path
import pandas as pd
import torch
from sklearn.preprocessing import StandardScaler

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def main(input_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_files = sorted(input_dir.glob("stock_data_*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV files found")
    frames = [pd.read_csv(fp) for fp in csv_files]
    df = pd.concat(frames, ignore_index=True)
    df.fillna(method="ffill", inplace=True)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df.select_dtypes(include=[float, int]))
    tensor = torch.tensor(scaled, dtype=torch.float32)
    out_path = out_dir / "data_tensor.pt"
    torch.save(tensor, out_path)
    logging.info("tensor saved %s", out_path)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    main(args.input_dir, args.out_dir)


if __name__ == "__main__":
    cli()
