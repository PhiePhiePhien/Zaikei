import argparse
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def fetch_html(url: str) -> str:
    for _ in range(3):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        logging.warning("Request failed with status %s", resp.status_code)
    resp.raise_for_status()


def parse_table(html: str):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    data = []
    if table:
        headers = [th.text.strip() for th in table.find_all("th")]
        for row in table.find_all("tr"):
            cols = [td.text.strip() for td in row.find_all("td")]
            if len(cols) == len(headers):
                data.append(dict(zip(headers, cols)))
    return data


def main(url: str, weeks: int, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for w in range(weeks):
        date = datetime.now() - timedelta(weeks=w)
        html = fetch_html(url)
        records = parse_table(html)
        out_file = out_dir / f"raw_{date.strftime('%Y%m%d')}.json"
        with out_file.open("w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False)
        logging.info("saved %s", out_file)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--weeks", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, default=Path("data/raw"))
    args = parser.parse_args()
    main(args.url, args.weeks, args.out_dir)


if __name__ == "__main__":
    cli()
