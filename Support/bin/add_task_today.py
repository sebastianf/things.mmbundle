#!/usr/bin/python

import os
import sys
import urllib
import subprocess

body = sys.stdin.read()

note = (
    "Link: message://" + os.environ['MM_MESSAGE_ID'] + "\n\n"
  + os.environ['MM_SUBJECT'] + "\n"
  + "\n" + body[:9900])

url = ("things:///add?when=today&title="
  + urllib.quote(os.environ['MM_SUBJECT'])
  + "&notes=" + urllib.quote(note))

subprocess.call(["open", url])
