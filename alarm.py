#!/usr/bin/python

## alarm.py -- Start my music on time.

import sys
import time
import subprocess

def main():
  COMMAND = ["pithos"] # Command to be executed.

  # Prompt alarm time.
  print; print 'Start Pithos once at this time:'
  print 'Hour:'
  hour = int(raw_input())
  print 'Minute:'
  minute = int(raw_input())
  print

  # Main Loop: watch time.
  while(True):
    currentTime = time.localtime()
    if (hour == currentTime[3] and minute == currentTime[4]):
      subprocess.call( COMMAND)
      break  
    time.sleep(10)
# \main()       
  
# Boilerplate.
if __name__ == '__main__':
  main()
