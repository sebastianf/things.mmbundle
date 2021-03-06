#!/usr/bin/python

import os
import sys
import urllib
import subprocess

body = sys.stdin.read()

note = (
    "Link: message://" + os.environ['MM_MESSAGE_ID'] + "\n\n"
  + os.environ['MM_SUBJECT'] + "\n"
  + "\n" + body[:1000])

url = ("things:///add?show-quick-entry=true&title="
  + urllib.quote(os.environ['MM_SUBJECT'])
  + "&notes=" + urllib.quote(note))

subprocess.call(["open", url])
