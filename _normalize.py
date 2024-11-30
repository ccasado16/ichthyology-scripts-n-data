def _normalize(string: str, additional_removes: list = None) -> str:
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

    if additional_removes:
        for remove in additional_removes:
            word = word.replace(remove, "")

    return word
