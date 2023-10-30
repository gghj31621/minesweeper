from cx_Freeze import setup, Executable

setup(
    name="menu",
    version="0.1",
    description="Menu App",
    executables=[Executable("menu.py")],
)
