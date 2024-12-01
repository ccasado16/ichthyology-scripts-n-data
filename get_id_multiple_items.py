from re import S
import sys
import pandas as pd
from _normalize import _normalize

import argparse
from _split import _split


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--main_csv",
        type=str,
        required=True,
        help="Main csv where there is the values you want to find their ids",
    )

    parser.add_argument(
        "--column_to_compare_to_ids_csv",
        required=True,
        type=str,
    )

    parser.add_argument(
        "--variant_replaces",
        type=str,
        help="Dictionary in key:value-key:value format to replace in the column_to_search_id before comparing",
    )

    parser.add_argument(
        "--ids_csv",
        type=str,
        help="Csv where there is the ids",
        required=True,
    )

    parser.add_argument(
        "--column_to_compare_to_main_csv",
        required=True,
    )

    args = parser.parse_args()

    get_ids_multiple_items(
        pd.read_csv(args.main_csv, na_filter=False),
        args.column_to_compare_to_ids_csv,
        args.variant_replaces,
        pd.read_csv(args.ids_csv, na_filter=False),
        args.column_to_compare_to_main_csv,
    )


def get_ids_multiple_items(
    main_csv: pd.DataFrame,
    column_to_compare_to_ids_csv: str,
    variant_replaces: str,
    ids_csv: pd.DataFrame,
    column_to_compare_to_main_csv: str,
):

    if variant_replaces:
        variant_replaces = dict(
            [tuple(x.split(":")) for x in variant_replaces.split("-")]
        )

    for tindex, row in main_csv.iterrows():
        items = _split(row[column_to_compare_to_ids_csv])

        print(f"items: {items}")

        if variant_replaces:
            for index, item in enumerate(items):
                if item in variant_replaces:
                    print(f"\t[!] Replacing {item} with {variant_replaces[item]}")
                    items[index] = variant_replaces[item]
                else:
                    print(f"\t[!] No replaces for {item}\n")

        print(f"\t[!] Items after replaces: {items} - type: {type(items)}")

        ids_list = []

        for item in items if type(items) == list else [items]:
            print(f"\t[!] Searching for {item}")

            for index, row in ids_csv.iterrows():
                normalized_id_csv_value = _normalize(row[column_to_compare_to_main_csv])
                normalized_item = _normalize(item)
                print(
                    f"\t\t[!] Comparing {_normalize(row[column_to_compare_to_main_csv])} with {_normalize(item)}"
                )
                if normalized_id_csv_value == normalized_item:
                    print(f"\t\t[!] Found {item} in ids_csv")
                    ids_list.append(str(row["id"]))
                    break
                continue

        print(f"\t[!] ids_list: {ids_list}")

        ids_str = ", ".join([str(x) for x in ids_list])

        print(f"[!] ids_str: {str(ids_str)} - type {type(str(ids_str))}")

        main_csv.at[tindex, f"{column_to_compare_to_ids_csv}_ids"] = str(ids_str)

    main_csv.to_csv(
        f"multiple-ided_{column_to_compare_to_ids_csv}_{sys.argv[2].split('/')[-1].split('.')[0]}.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
