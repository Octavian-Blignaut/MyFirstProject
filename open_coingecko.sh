#!/bin/bash

# This script opens coingecko.com in Google Chrome.

# Check if Google Chrome is installed.
if ! command -v google-chrome &> /dev/null
then
  echo "Google Chrome is not installed. Please install it and try again."
  exit 1
fi

google-chrome "https://www.coingecko.com"

echo "Opening coingecko.com in Google Chrome..."
