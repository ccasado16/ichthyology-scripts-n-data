from _normalize import _normalize


def _switch_habitats(habitat):
    if "tipishca" in _normalize(habitat):
        habitat = "cocha"

    elif "rio" in _normalize(habitat):
        habitat = "rio"

    elif "orilla" in _normalize(habitat):
        habitat = "rio"

    elif "lago" in _normalize(habitat):
        habitat = "cocha"

    elif "quebrada" in _normalize(habitat):
        habitat = "quebrada"

    elif "ucayali" in _normalize(habitat):
        habitat = "rio"

    elif "cochas" in _normalize(habitat):
        habitat = "cocha"

    elif "cocha" in _normalize(habitat):
        habitat = "cocha"

    elif "tipischca" in _normalize(habitat):
        habitat = "cocha"

    elif "tipischa" in _normalize(habitat):
        habitat = "cocha"

    else:
        habitat = "otros"

    return habitat
