#!/bin/sh

if [ "$SERVICE" = "web" ]; then
  watchmedo auto-restart --directory=./src --pattern="*.py" --recursive -- \
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
else
  echo "Unknown or missing SERVICE. Only 'web' is supported currently."
  exit 1
fi
