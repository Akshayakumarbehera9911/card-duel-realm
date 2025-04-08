#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Run seed script to initialize the database
python seed_db.py

# Start the application
gunicorn app:app