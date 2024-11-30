import sys
import pandas as pd
from _normalize import _normalize
import argparse


def main():
    parser = argparse.ArgumentParser(description="Get ids from a csv")

    parser.add_argument("--ids_csv", type=str, help="csv containing ids", required=True)

    parser.add_argument(
        "--cleaned_csv", type=str, help="csv to compare with ids", required=True
    )

    parser.add_argument(
        "--column_to_search_id",
        type=str,
        help="column of the cleaned_csv with the values you want to find their ids in ids_csv",
        required=True,
    )

    parser.add_argument(
        "--column_to_compare_item",
        type=str,
        help="column of the ids_csv with the values you want to compare with the cleaned_csv (normally 'name')",
        required=True,
    )

    parser.add_argument(
        "--variant_replaces",
        type=str,
        help="Dictionary in key:value,key:value format to replace in the column_to_search_id before comparing",
    )

    args = parser.parse_args()

    print(args.variant_replaces, type(args.variant_replaces))

    get_ids(
        pd.read_csv(args.ids_csv, na_filter=False),
        pd.read_csv(args.cleaned_csv, na_filter=False),
        args.column_to_search_id,
        args.column_to_compare_item,
        args.variant_replaces,
    )


def get_ids(
    ids_csv: pd.DataFrame,
    cleaned_csv: pd.DataFrame,
    column_to_search_id: str,
    column_to_compare_item: str,
    variant_replaces: str,
):
    if variant_replaces:
        variant_replaces = dict(
            [tuple(x.split(":")) for x in variant_replaces.split(",")]
        )

    # traverse the cleaned csv and take the value of the column_to_search_id
    for index, row in cleaned_csv.iterrows():
        item = row[column_to_search_id]
        print(_normalize(item))

        # if not name:
        #     cleaned_csv.at[index, column_to_search_id] = "None"
        #     continue

        if variant_replaces:
            if item in variant_replaces:
                print(f"\t[!] Replacing {item} with {variant_replaces[item]}")
                item = variant_replaces[item]
            else:
                print(f"\t[!] No replacements for {item}")

        # traverse the ids csv and compare the item with the column_to_compare_item
        # if they are the same, take the id and save it in the cleaned csv
        for j_index, j_row in ids_csv.iterrows():
            if _normalize(j_row[column_to_compare_item]) == _normalize(item):
                _id = j_row["id"]

                cleaned_csv.at[index, f"{column_to_search_id}_id"] = _id

                break

    cleaned_csv.to_csv(
        # name of the column to search id + name of the cleaned csv file
        f"ided_{column_to_search_id}_{
            sys.argv[4].split('/')[-1].split('.')[0]
        }.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
