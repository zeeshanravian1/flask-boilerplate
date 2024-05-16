#!/bin/bash

# Run the application
echo "***** Starting Flask app *****"
exec python app.py


# #!/bin/bash

# # Wait for PostgreSQL to be ready
# while ! nc -z postgres 5432; do
#   echo "Waiting for PostgreSQL..."
#   sleep 1
# done

# # Use the migration message from the environment variable or set a default value
# MIGRATION_MESSAGE=${MIGRATION_MESSAGE:-"Initial migration"}

# # Run migrations
# echo "Running migrations with message: $MIGRATION_MESSAGE"
# flask db migrate -m "$MIGRATION_MESSAGE"
# flask db upgrade

# # Run the application
# echo "Starting Flask app..."
# exec python app.py
