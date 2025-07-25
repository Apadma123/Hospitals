#!/bin/bash

echo "✅ Creating PostgreSQL database 'hospitals'..."

# Create the database if it doesn't exist
createdb -U postgres hospitals 2>/dev/null

if [ $? -eq 0 ]; then
  echo "🎉 Database 'hospitals' created!"
else
  echo "⚠️  Database 'hospitals' may already exist or creation failed."
fi
