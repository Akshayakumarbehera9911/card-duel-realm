#!/bin/bash
# Exit on error
set -o errexit

# Fix for werkzeug.urls issue
pip install -r requirements.txt
pip install werkzeug==2.0.3

# Run seed script to initialize the database
python seed_db.py