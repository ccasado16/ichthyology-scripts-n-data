def _split(row):
    splitted = (
        row.replace(" y ", " , ")
        .replace("&", " , ")
        .replace("/", " , ")
        .replace("-", " , ")
        # .replace(",", " , ") # for Usage or Usos table
        .split(" , ")
    )
    splitted = [x.strip() for x in splitted]

    return splitted
