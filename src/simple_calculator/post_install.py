import os
import shutil
from importlib.resources import files


def install_desktop_files():
    home = os.path.expanduser("~")

    applications_dir = os.path.join(home, ".local/share/applications")
    icons_dir = os.path.join(home, ".local/share/icons/hicolor/256x256/apps")

    os.makedirs(applications_dir, exist_ok=True)
    os.makedirs(icons_dir, exist_ok=True)

    assets = files("simple_calculator.assets")

    desktop_src = assets / "simple-calculator.desktop"
    icon_src = assets / "simple-calculator.png"

    shutil.copy(desktop_src, applications_dir)
    shutil.copy(icon_src, icons_dir)

    print("Desktop integration complete.")
