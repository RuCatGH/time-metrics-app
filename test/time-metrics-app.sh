#!/bin/bash
ANSW=$(curl http://127.0.0.1:5000/time)
if [ "$ANSW" == "0" ]; then
  echo "Test failed"
  exit 1
else
  echo "Time route test passed"
fi
