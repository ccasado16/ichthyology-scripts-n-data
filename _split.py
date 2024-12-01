def _split(row):
    splitted = (
        row.replace(" y ", " , ")
        .replace("&", " , ")
        .replace("/", " , ")
        .replace("-", " , ")
        .replace(" - ", " , ")
        # .replace(",", " , ") # for Usage or Usos table
        .replace(", ", " , ")
        .split(" , ")
    )
    splitted = [x.strip() for x in splitted]

    return splitted
