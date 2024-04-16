"""
install_script.py

Simple script to install device_overflow.py to FL Studio
"""
from pathlib import Path
from shutil import copy


our_path = Path(__file__).parent

target_path = \
    Path.home() \
    / Path(
        "Documents",
        "Image-Line",
        "FL Studio",
        "Settings",
        "Hardware",
        "Overflow test",
    )


target_path.mkdir(exist_ok=True)

copy(our_path.joinpath("device_overflow.py"), target_path)
