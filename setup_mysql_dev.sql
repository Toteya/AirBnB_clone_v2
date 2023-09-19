-- create a mysql database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all priveleges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
