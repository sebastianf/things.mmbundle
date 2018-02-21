#!/usr/bin/python

import os
import sys
import urllib
import subprocess

body = sys.stdin.read()

note = ("From: " + os.environ['MM_FROM'] + "\n"
  + "Subject: " + os.environ['MM_SUBJECT'] + "\n"
  + "Link: message://" + os.environ['MM_MESSAGE_ID'] + "\n"
  + "\n" + body[:200])

url = ("things:///add?when=today&title="
  + urllib.quote(os.environ['MM_SUBJECT'])
  + "&notes=" + urllib.quote(note))

subprocess.call(["open", url])
