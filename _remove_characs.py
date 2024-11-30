def _remove_characs(string: str, list_to_remove: list) -> str:

    for remove in list_to_remove:
        string = string.replace(remove, "")

    return string.strip()
