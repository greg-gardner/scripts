#!/usr/bin/python

import sys  # Standard library.
import subprocess  # Run system commands

# Gather our code in a main() function
def main():
  print 'Hello there', sys.argv[1]
  subprocess.call(["notify-send", "-u", "critical", str(sys.argv[1]) ])

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
