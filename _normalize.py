def _normalize(string):
    word = (
        (
            string.replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )
        .lower()
        .strip()
    )

    return word
