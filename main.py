#!/usr/bin/.venv python3

# main.py

"""
Description: This script performs ....
Author: Author Name
Date Created: 2024-10-01 16:24:21
Date Modified: 2024-10-01 16:24:21
Version: 1.0
Python Version: 3.12.0
Dependencies: shlex, sys 
License: MIT License
"""

import shlex
import sys

def echo(phrase: str) -> None:
    """A dummy wrapper around print."""
    # for demonstration purposes, you can imagine that there is some
    # valuable and reusable logic inside this function
    print(phrase)

def main() -> int:
    """ Main entry point of the app """
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    """App starts executing here"""
    sys.exit(main())  # next section explains the use of sys.exit
    
    