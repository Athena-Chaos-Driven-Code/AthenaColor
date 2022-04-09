# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .RgbControlled import RgbControlled

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Fore","Back", "Underline"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
Fore = RgbControlled(
    param_code= f"38;2;",
)

Back = RgbControlled(
    param_code= f"48;2;",
)

Underline = RgbControlled(
    param_code= f"58;2;",
)