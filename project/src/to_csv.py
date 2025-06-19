import argparse
import json
import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def main(input_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for fp in input_dir.glob("raw_*.json"):
        with fp.open() as f:
            data = json.load(f)
        if not data:
            logging.warning("no data in %s", fp)
            continue
        df = pd.DataFrame(data)
        date = fp.stem.split("_")[1]
        out_file = out_dir / f"stock_data_{date}_week{date[-2:]}.csv"
        df.to_csv(out_file, index=False, encoding="utf-8-sig")
        logging.info("csv saved %s", out_file)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    main(args.input_dir, args.out_dir)


if __name__ == "__main__":
    cli()
