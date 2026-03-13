# calcu

A minimal installable calculator for Linux with both a Graphical User Interface and a robust Command-Line Interface.

## Features
- **GUI Mode**: A minimal interface using Tkinter, perfectly scaling to the user's display.
- **CLI Mode**: Fast and standard parsing for immediate calculations.
- **Desktop Integration**: Includes a `.desktop` file and SVG icon, meaning it is accessible via standard Desktop Application Menus.
- **Man Page**: Documentation accessible by running `man calcu`.
- **Error Logging**: Background errors evaluate to the system-specific local state path (`~/.local/state/calcu/calcu.log`).

## Installation

### Standard Linux Install (Recommended)

To install globally to your local user environment (`~/.local`), keeping the `.desktop` integration, icon, and man pages, use the included Makefile:

```bash
make install
```
*Note: This utilizes `pip install .` and copies necessary Linux desktop files to their standard `.local/share/` directories.*

You can uninstall anytime smoothly with:
```bash
make uninstall
```

### Pure Python Install

If you do not want manual pages and app icons, you can fall back to standard `pip`:

```bash
pip install .
# or for an editable install:
pip install -e .
```

## Usage

**1. Launch the Graphical Interface (GUI):**
```bash
calcu
```
*(Simply running the command with no arguments opens the calculator UI).*

**2. Command-Line Evaluation:**
```bash
calcu 5 '*' 5
calcu "math.pow(2, 3)"
```

**3. Interactive CLI Mode:**
```bash
calcu -i
calcu> 100 / 3
33.333333333333336
calcu> exit
```

**4. Piped Output:**
```bash
echo "12 * 12" | calcu
```
