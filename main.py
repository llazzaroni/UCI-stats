import argparse

# Project-specific imports
from utils.import_dfs import process_tables
from utils.download import download_data
from utils.statistics import most_podiums, most_podiums_gt, most_podiums_monuments, most_podiums_monuments_wc, most_podiums_monuments_wc_gt, most_wins, most_wins_gt, most_wins_monuments, most_wins_monuments_wc, most_wins_monuments_wc_gt \


def main(args):
    if args.download_data:
        output_path = args.output
        download_data(output_path)
    if args.process_data:
        input_path = args.data
        output_path = args.output
        process_tables(input_path, output_path)
    if args.statistics:
        input_path = args.data
        podiums = most_podiums_monuments(input_path)
        print(podiums)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Build cycling winners dataset.")
    p.add_argument("--download-data", default=False)
    p.add_argument("--process-data", default=False)
    p.add_argument("--statistics", default=False)
    p.add_argument("--data")
    p.add_argument("--output")
    args = p.parse_args()
    main(args)

