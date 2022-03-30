# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from .BoilerPlate import TestTypes

# ----------------------------------------------------------------------------------------------------------------------
# - Support Decorators for testing OPAQUE COLORS-
# ----------------------------------------------------------------------------------------------------------------------
# RGB tests
def testRGB(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=int,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"RGB values {arguments=} did not consist of integer values")
        return fnc(*args,**kwargs)
    return wrapper

# HEX tests
def testHEX(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=str,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HEX values {arguments=} did not consist of a string value")
        return fnc(*args,**kwargs)
    return wrapper

# HSV tests
def testHSV(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HSV values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

# HSL tests
def testHSL(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HSL values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

# CMYK tests
def testCMYK(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=(int,float),
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"CMYK values {arguments=} did not consist of integer or float values")
        return fnc(*args,**kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Support Decorators for testing TRANSPARENT COLORS-
# ----------------------------------------------------------------------------------------------------------------------
# RGB tests
def testRGBA(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=int,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"RGBA values {arguments=} did not consist of integer values")
        return fnc(*args,**kwargs)
    return wrapper

# HEX tests
def testHEXA(fnc):
    """
    Decorator which runs TestTypes on the function's arguments.
    Raises a ValueError when not all off the arguments can be matched to the given type
    """
    def wrapper(*args,**kwargs):
        if not TestTypes(
                types=str,
                objects=(arguments:= args if not kwargs else (*args,*kwargs.values()))
        ):
            raise ValueError(f"HEXA values {arguments=} did not consist of a string value")
        return fnc(*args,**kwargs)
    return wrapper