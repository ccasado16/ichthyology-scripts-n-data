import sys
import pandas as pd
from _normalize import _normalize


def main():
    if len(sys.argv) > 1:
        csv = pd.read_csv(sys.argv[1], na_filter=False)
        column_name = sys.argv[2]
        clean(csv, column_name)
    else:
        print("Usage: python clean_repeated.py file-raw.csv column_name_to_sort")
        return


def clean(csv: pd.DataFrame, column_name: str):
    csv.dropna(inplace=True)
    raw_items_array = csv.values

    # raw items is a list of lists of strings, turn all the strings into lowercase and if the string is empty, replace it with "None"
    raw_items_array = [
        [_normalize(str(item)) if item != "" else "None" for item in row]
        for row in raw_items_array
    ]

    print(raw_items_array)

    # remove duplicates
    cleaned_items = []

    for row in raw_items_array:
        if row not in cleaned_items:
            cleaned_items.append(row)

    print(cleaned_items)

    # save the cleaned items into a new csv with the same headers as the original csv
    cleaned_csv = pd.DataFrame(cleaned_items, columns=csv.columns)

    # sort the cleaned csv by the column name
    cleaned_csv.sort_values(by=[column_name], inplace=True)

    cleaned_csv.to_csv(
        f"cleaned_{
        # remove the parent directory and the extension of the file to create the new file name
        sys.argv[1].split("/")[-1].split(".")[0]}.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
