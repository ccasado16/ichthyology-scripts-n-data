def _split(row):
    splitted = (
        row.replace(" y ", " , ")
        .replace("&", " , ")
        .replace("/", " , ")
        .replace("-", " , ")
        .split(" , ")
    )
    splitted = [x.strip() for x in splitted]

    return splitted
