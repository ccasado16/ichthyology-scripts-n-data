import sys
import pandas as pd
from _normalize import _normalize


def main():
    if len(sys.argv) > 1:
        # csv containing ids
        ids_csv = pd.read_csv(sys.argv[1], na_filter=False)

        # csv to compare with ids
        cleaned_csv = pd.read_csv(sys.argv[2], na_filter=False)

        # column of the cleaned_csv with the values you want to find their ids in ids_csv
        column_to_search_id = sys.argv[3]

        # column of the ids_csv with the values you want to compare
        # with the cleaned_csv (normally 'name')
        column_to_compare_item = sys.argv[4]

        get_ids(ids_csv, cleaned_csv, column_to_search_id, column_to_compare_item)
    else:
        print(
            "Usage: python get_ids.py ids_file.csv cleaned_file.csv column_to_search_id column_to_compare_item (normally 'name')"
        )


def get_ids(
    ids_csv: pd.DataFrame,
    cleaned_csv: pd.DataFrame,
    column_to_search_id: str,
    column_to_compare_item: str,
):
    # traverse the cleaned csv and take the value of the column_to_search_id
    for index, row in cleaned_csv.iterrows():
        item = row[column_to_search_id]
        print(_normalize(item))

        # if not name:
        #     cleaned_csv.at[index, column_to_search_id] = "None"
        #     continue

        # traverse the ids csv and compare the item with the column_to_compare_item
        # if they are the same, take the id and save it in the cleaned csv
        for j_index, j_row in ids_csv.iterrows():
            if _normalize(j_row[column_to_compare_item]) == _normalize(item):
                _id = j_row["id"]

                cleaned_csv.at[index, f"{column_to_search_id}_id"] = _id

                break

    # cleaned_csv.to_csv("ided_" + sys.argv[2], index=False)
    cleaned_csv.to_csv(
        f"ided_{
            sys.argv[3]
        }_{sys.argv[2].split('/')[-1].split('.')[0]}.csv", index=False
    )


if __name__ == "__main__":
    main()
