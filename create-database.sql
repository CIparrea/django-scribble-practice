-- Create the database
CREATE DATABASE scribble;

-- Create an admin user for our app to use
CREATE USER scribble_admin WITH PASSWORD 'password';

-- Give that user permissins to manage the database:
GRANT ALL PRIVILEGES ON DATABASE scribble TO scribble_admin;