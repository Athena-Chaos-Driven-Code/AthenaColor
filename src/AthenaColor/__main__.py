# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects.ColorSystems.Opaque import (
    RGB,
    HSV,
    HSL,
    HEX,
    CMYK
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    rgb = RGB(165,42,42)
    hex_ = HEX("#A52A2A")
    print(repr(rgb))
    print(repr(hex_))

    print(RGB(189,183,107)==HEX("#BDB76D"))