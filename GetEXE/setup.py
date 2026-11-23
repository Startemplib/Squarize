from cx_Freeze import setup, Executable

setup(
    name="Squarize",
    version="0.1",
    description="Squarize Application",
    executables=[Executable("Squarize.py", base="Win32GUI", icon="Squarize.ico")],
)
