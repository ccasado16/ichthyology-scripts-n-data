import sys
import pandas as pd
import argparse

from _normalize import _normalize
from _remove_characs import _remove_characs


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--main_csv",
        type=str,
        required=True,
        help="Main csv where there is the values you want to find their counter value in the data_csv",
    )

    parser.add_argument(
        "--column_to_compare_with_data_csv", type=str, required=True, help=""
    )

    parser.add_argument(
        "--data_csv",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--column_to_be_compared_with_main_csv",
        type=str,
        required=True,
    )

    parser.add_argument(
        "--column_to_get_data_from",
        type=str,
        required=True,
    )

    parser.add_argument("--value_is_data_empty", type=str)

    parser.add_argument(
        "--characs_to_remove_from_data",
        nargs="+",
        help="List of characters to remove from the data",
    )

    parser.add_argument(
        "--name_for_data_column_in_main_csv",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    get_data(
        pd.read_csv(args.main_csv, na_filter=False),
        args.column_to_compare_with_data_csv,
        pd.read_csv(args.data_csv, na_filter=False),
        args.column_to_be_compared_with_main_csv,
        args.column_to_get_data_from,
        args.value_is_data_empty,
        args.name_for_data_column_in_main_csv,
        args.characs_to_remove_from_data,
    )


def get_data(
    main_csv: pd.DataFrame,
    column_to_compare_with_data_csv: str,
    data_csv: pd.DataFrame,
    column_to_be_compared_with_main_csv: str,
    column_to_get_data_from: str,
    value_is_data_empty: str,
    name_for_data_column_in_main_csv: str,
    characs_to_remove_from_data: list,
):
    for index, row in main_csv.iterrows():
        item = row[column_to_compare_with_data_csv]

        print(item)

        for j_index, j_row in data_csv.iterrows():
            comparison_item = j_row[column_to_be_compared_with_main_csv]
            print(f"\tComparing with: {comparison_item}")

            if _normalize(comparison_item) == _normalize(item):
                data = (
                    j_row[column_to_get_data_from]
                    if j_row[column_to_get_data_from]
                    else value_is_data_empty
                )

                if characs_to_remove_from_data:
                    print(
                        f"\t[!] Removing characters from data: {characs_to_remove_from_data}"
                    )

                    data = _remove_characs(data, characs_to_remove_from_data)

                print(f"\t[*] Match Found: {item} : {comparison_item} -> {data}")

                main_csv.at[index, name_for_data_column_in_main_csv] = data

                break

        else:
            print("\t[!] No match found")

    main_csv.to_csv(
        f"with_data_{column_to_get_data_from}_{
            sys.argv[2].split('/')[-1].split('.')[0]
        }.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
