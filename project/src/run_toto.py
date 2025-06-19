import argparse
import json
import logging
from pathlib import Path
import torch

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def dummy_predict(tensor: torch.Tensor):
    return tensor.mean(dim=1).tolist()


def main(input_path: Path, out_json: Path):
    tensor = torch.load(input_path)
    predictions = dummy_predict(tensor)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w") as f:
        json.dump({"predictions": predictions}, f)
    logging.info("predictions saved %s", out_json)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    args = parser.parse_args()
    main(args.input, args.out_json)


if __name__ == "__main__":
    cli()
