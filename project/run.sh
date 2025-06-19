#!/usr/bin/env bash
set -euo pipefail

echo "=== 環境構築とパッケージインストール ==="
bash ./setup_env.sh

echo "=== パイプライン実行 ==="
bash ./run_pipeline.sh

echo "=== 完了 ==="
echo "出力ファイルは project/data/output にあります"
