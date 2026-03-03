#!/usr/bin/env python3

import sys
import os
import argparse
from simple_calculator.calculator import Calculator
from simple_calculator.ui import CalculatorUI
from importlib.metadata import version


from simple_calculator.post_install import install_desktop_files



def get_version():
    return version("simple-calculator")


def main():
    install_desktop_files()

    parser=argparse.ArgumentParser(description="Simple Calculator application")
    
    parser.add_argument(
    "--version",
    action="store_true",
    help="Show application version"
    )
    
    parser.add_argument(
    "--gui",
    action="store_true",
    help="Lauch gui calculator"
    
    )
    
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    # Subtract
    sub_parser = subparsers.add_parser("sub", help="Subtract two numbers")
    sub_parser.add_argument("a", type=float)
    sub_parser.add_argument("b", type=float)

    # Multiply
    mul_parser = subparsers.add_parser("mul", help="Multiply two numbers")
    mul_parser.add_argument("a", type=float)
    mul_parser.add_argument("b", type=float)

    # Divide
    div_parser = subparsers.add_parser("div", help="Divide two numbers")
    div_parser.add_argument("a", type=float)
    div_parser.add_argument("b", type=float)
    
    args = parser.parse_args()
    calculator = Calculator()
    if args.version:
        print(get_version())
        sys.exit(0)
    if args.gui:
        app = CalculatorUI(calculator)
        app.run()
        sys.exit(0)
    if args.command == "add":
        print(calculator.add(args.a, args.b))
    elif args.command == "sub":
        print(calculator.subtract(args.a, args.b))
    elif args.command == "mul":
        print(calculator.multiply(args.a, args.b))
    elif args.command == "div":
        print(calculator.divide(args.a, args.b))
    else:
        parser.print_help()

    calculator = Calculator()
    app= CalculatorUI(calculator)
    app.run()

if __name__ == "__main__":
    main()
