#!/usr/bin/env bash
set -euo pipefail

source ./setup_env.sh

python src/fetch_data.py --url "https://www.rakuten-sec.co.jp/web/market/data/topx.html" --weeks 10 --out-dir "data/raw"
python src/to_csv.py --input-dir "data/raw" --out-dir "data/raw"
python src/to_tensor.py --input-dir "data/raw" --out-dir "data/output"
python src/run_toto.py --input "data/output/data_tensor.pt" --out-json "data/output/result.json"
python src/visualize.py --input-json "data/output/result.json" --out-dir "data/output"
