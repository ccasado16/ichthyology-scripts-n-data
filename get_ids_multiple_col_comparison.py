import sys
import pandas as pd
from _normalize import _normalize

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Get the id of a column from a csv having the ids in another csv by comparing a list of columns provided by the user from both csvs and saving the id in the main csv"
    )

    parser.add_argument(
        "--main_csv",
        type=str,
        required=True,
        help="Main csv where there is the values you want to find their ids",
    )

    # columns from the main_csv that you want to compare with the ids_csv
    parser.add_argument(
        "--columns_to_compare_to_ids_csv",
        nargs="+",
        required=True,
        help="Columns from the main_csv that you want to compare with the ids_csv",
    )

    # column from the main_csv that you want the id
    parser.add_argument(
        "--column_to_search_id",
        type=str,
        required=True,
        help="Column from the main_csv that you want the id",
    )

    parser.add_argument("--ids_csv", type=str, help="Csv where there is the ids")

    # columns from the ids_csv that you want to compare with the main_csv columns
    parser.add_argument(
        "--columns_to_compare_to_main_csv",
        required=True,
        nargs="+",
        help="Columns from the ids_csv that you want to compare with the main_csv",
    )

    args = parser.parse_args()

    get_ids_multiple_col_comparison(
        pd.read_csv(args.main_csv, na_filter=False),
        args.columns_to_compare_to_ids_csv,
        args.column_to_search_id,
        pd.read_csv(args.ids_csv, na_filter=False),
        args.columns_to_compare_to_main_csv,
    )


def get_ids_multiple_col_comparison(
    main_csv: pd.DataFrame,
    columns_to_compare_to_ids_csv: list,
    column_to_search_id: str,
    ids_csv: pd.DataFrame,
    columns_to_compare_to_main_csv: list,
):
    print(f"columns_to_compare_to_ids_csv: {columns_to_compare_to_ids_csv}")

    print(f"column_to_search_id: {column_to_search_id}")

    print(f"columns_to_compare_to_main_csv: {columns_to_compare_to_main_csv}")

    # travese the main csv and take the values of the columns_to_compare_to_ids_csv
    for index, row in main_csv.iterrows():
        items = [_normalize(row[column]) for column in columns_to_compare_to_ids_csv]

        print(f"Items to compare: {items}")

        # traverse the ids csv and compare the items with the columns_to_compare_to_main_csv
        # if they are the same, take the id and save it in the main csv

        for j_index, j_row in ids_csv.iterrows():
            j_items = [
                _normalize(j_row[column]) for column in columns_to_compare_to_main_csv
            ]

            print(f"\tcomparing with {j_items}")

            if items == j_items:
                _id = j_row["id"]

                main_csv.at[index, f"{column_to_search_id}_id"] = _id

                print(f"\t[*] Match found: {_id} for {items}")

                break
        else:
            print("[!] No match found")

    main_csv.to_csv(
        f"ided-{column_to_search_id}_{sys.argv[2].split('/')[-1].split('.')[0]}.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
