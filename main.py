import argparse

# Project-specific imports
from utils.import_dfs import process_tables
from utils.download import download_data
from utils.statistics import most_podiums, most_podiums_gt, most_podiums_monuments, most_podiums_monuments_wc, most_podiums_monuments_wc_gt, most_wins, most_wins_gt, most_wins_monuments, most_wins_monuments_wc, most_wins_monuments_wc_gt
from utils.write_outputs import write_outputs


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
        output_path = args.output
        write_outputs(input_path, output_path, args.include, int(args.number_cyclists))



if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Build cycling winners dataset.")
    p.add_argument("--download-data", default=False)
    p.add_argument("--process-data", default=False)
    p.add_argument("--statistics", default=False)
    p.add_argument("--data")
    p.add_argument("--output")
    p.add_argument(
        "--include",
        nargs="+",
        default=["most_podiums", "most_podiums_gt", "most_podiums_monuments", "most_podiums_monuments_wc",
                 "most_podiums_monuments_wc_gt", "most_wins", "most_wins_gt", "most_wins_monuments", "most_wins_monuments_wc",
                 "most_wins_monuments_wc_gt"],
        help="List of scene names to process"
    )
    p.add_argument("--number-cyclists", default=8)
    args = p.parse_args()
    main(args)