# 📘 Assignment: Database Integration with SQLite

## 🎯 Objective

Learn how to integrate SQLite databases into Python applications, including creating tables, performing CRUD operations, and handling data persistence.

## 📝 Tasks

### 🛠️ Set up database connection and schema

#### Description
Create a Python script that connects to an SQLite database and defines a table schema for storing data.

#### Requirements
Completed program should:

- Import the `sqlite3` module
- Create or connect to an SQLite database file
- Define a table with at least three columns (id, name, description)
- Handle database connection errors gracefully

### 🛠️ Implement CRUD operations

#### Description
Add functions to create, read, update, and delete records in the database.

#### Requirements
Completed program should:

- Include a function to insert new records
- Include a function to retrieve all records
- Include a function to update existing records by ID
- Include a function to delete records by ID
- Use parameterized queries to prevent SQL injection

### 🛠️ Add data validation and error handling

#### Description
Enhance the script with input validation and proper error handling for database operations.

#### Requirements
Completed program should:

- Validate input data before inserting/updating
- Handle cases where records don't exist (e.g., update/delete non-existent ID)
- Provide clear error messages for database failures
- Ensure the database connection is properly closed