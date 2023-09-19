-- create a mysql database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all priveleges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
