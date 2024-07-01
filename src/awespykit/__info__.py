# coding: utf-8

try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata

APP_NAME = "PyTools"
PRE_VER = "1.0.0"
try:
    VERSION = metadata.version(APP_NAME)
except:
    VERSION = PRE_VER
AUTHOR = "hrp/hrpzcf"

__all__ = ["APP_NAME", "AUTHOR", "PRE_VER", "VERSION"]
