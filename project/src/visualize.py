import argparse
import json
import logging
from pathlib import Path
import matplotlib; matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def main(input_json: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with input_json.open() as f:
        data = json.load(f)
    df = pd.DataFrame({"predicted_price": data["predictions"]})
    df["date"] = range(len(df))
    csv_path = out_dir / "prediction.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    plt.figure()
    plt.plot(df["date"], df["predicted_price"])
    plt.title("株価予想")
    plt.xlabel("日付")
    plt.ylabel("予想株価")
    plt.grid(True)
    png_path = out_dir / "prediction.png"
    plt.savefig(png_path)
    logging.info("results saved %s %s", csv_path, png_path)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    main(args.input_json, args.out_dir)


if __name__ == "__main__":
    cli()
