#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    prog="MyDemo",
    description="Print's the name passed as a command line argument."
)

parser.add_argument("-n", "--name", default="Lewis",
                    help="The name to be printed out when running this script!")

args = parser.parse_args()

print(f"Hello {args.name}")
