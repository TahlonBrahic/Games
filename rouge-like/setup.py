import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Rouge-Like", # Filler name to change later
    version="0.1", # Version name to change
    description="Work in progress",
    options={"build_exe": build_exe_options},
    executables=[Executable("rougelike.py", base=base)],
)