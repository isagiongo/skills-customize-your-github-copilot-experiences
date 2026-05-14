import sqlite3
from typing import List, Tuple, Optional

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn: sqlite3.Connection):
    """Create a table for storing items."""
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        );
        """
        conn.execute(sql)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_item(conn: sqlite3.Connection, item: Tuple[str, str]) -> int:
    """Insert a new item into the items table."""
    sql = "INSERT INTO items(name, description) VALUES(?, ?)"
    try:
        cur = conn.cursor()
        cur.execute(sql, item)
        conn.commit()
        print("Item inserted successfully")
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting item: {e}")
        return None

def get_all_items(conn: sqlite3.Connection) -> List[Tuple]:
    """Query all items from the items table."""
    sql = "SELECT * FROM items"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error retrieving items: {e}")
        return []

def update_item(conn: sqlite3.Connection, item_id: int, item: Tuple[str, str]):
    """Update an item by id."""
    sql = "UPDATE items SET name = ?, description = ? WHERE id = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (*item, item_id))
        conn.commit()
        if cur.rowcount > 0:
            print("Item updated successfully")
        else:
            print("No item found with that ID")
    except sqlite3.Error as e:
        print(f"Error updating item: {e}")

def delete_item(conn: sqlite3.Connection, item_id: int):
    """Delete an item by id."""
    sql = "DELETE FROM items WHERE id = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (item_id,))
        conn.commit()
        if cur.rowcount > 0:
            print("Item deleted successfully")
        else:
            print("No item found with that ID")
    except sqlite3.Error as e:
        print(f"Error deleting item: {e}")

if __name__ == "__main__":
    database = "items.db"
    conn = create_connection(database)
    if conn:
        create_table(conn)
        # Example usage
        insert_item(conn, ("Example Item", "This is a sample item"))
        items = get_all_items(conn)
        print("All items:", items)
        conn.close()