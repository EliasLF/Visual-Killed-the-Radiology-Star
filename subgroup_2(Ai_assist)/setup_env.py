#!/usr/bin/env python3
"""Create a local .venv, install the requirements and register a Jupyter kernel.

Usage (from this folder):
    python setup_env.py            # create .venv + install + register kernel
    python setup_env.py --force    # ignore the Python-version check

Then start Jupyter with the venv's own interpreter:
    macOS/Linux:  .venv/bin/jupyter lab
    Windows:      .venv\\Scripts\\jupyter lab
and open biomedclip_demo.ipynb with the kernel "Python (.venv BiomedCLIP)".
"""
import platform
import subprocess
import sys
import venv
from pathlib import Path

HERE = Path(__file__).resolve().parent
VENV_DIR = HERE / ".venv"
KERNEL_NAME = "biomedclip-venv"
KERNEL_DISPLAY = "Python (.venv BiomedCLIP)"

# transformers==4.35.2 / tokenizers 0.15 have no wheels for Python 3.13+.
SUPPORTED = ((3, 9), (3, 12))


def venv_python() -> Path:
    sub = "Scripts/python.exe" if platform.system() == "Windows" else "bin/python"
    return VENV_DIR / sub


def run(*cmd) -> None:
    cmd = [str(c) for c in cmd]
    print("$", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def main() -> None:
    version = sys.version_info[:2]
    if not (SUPPORTED[0] <= version <= SUPPORTED[1]) and "--force" not in sys.argv:
        sys.exit(
            f"Python {version[0]}.{version[1]} is outside the tested range "
            f"{SUPPORTED[0][0]}.{SUPPORTED[0][1]}-{SUPPORTED[1][0]}.{SUPPORTED[1][1]} "
            "for the pinned packages.\n"
            "Run this script with Python 3.10-3.12 (e.g. `python3.11 setup_env.py`), "
            "or pass --force to try anyway."
        )

    if not venv_python().exists():
        print(f"Creating virtual environment in {VENV_DIR} ...")
        venv.EnvBuilder(with_pip=True, clear=False).create(VENV_DIR)
    else:
        print(f"Re-using existing virtual environment in {VENV_DIR}")

    py = venv_python()
    run(py, "-m", "pip", "install", "--upgrade", "pip")
    run(py, "-m", "pip", "install", "-r", HERE / "requirements.txt")
    run(
        py, "-m", "ipykernel", "install", "--user",
        "--name", KERNEL_NAME, "--display-name", KERNEL_DISPLAY,
    )

    jupyter = VENV_DIR / ("Scripts/jupyter.exe" if platform.system() == "Windows" else "bin/jupyter")
    print("\nDone. Start the notebook with:")
    print(f"  {jupyter} lab biomedclip_demo.ipynb")
    print(f"and select the kernel '{KERNEL_DISPLAY}'.")


if __name__ == "__main__":
    main()
