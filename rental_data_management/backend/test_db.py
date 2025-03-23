import pymysql

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 3306
DB_DATABASE = "RENT"
DB_USER = "root"
DB_PASSWORD = "2#06A9a"

def test_connection():
    try:
        # Connect to the database
        print(f"Attempting to connect to {DB_HOST}/{DB_DATABASE} as {DB_USER}...")
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        # Check if connection is successful
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        row = cursor.fetchone()
        
        print(f"Connection successful!")
        print(f"Server version: {row[0]}")
        
        # List all tables in the database
        print("\nTables in the database:")
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
            ORDER BY TABLE_NAME
        """)
        tables = cursor.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        # Try to find tables related to sites or rental data
        print("\nAttempting to examine potential site tables...")
        for table_name in [t[0] for t in tables]:
            try:
                cursor.execute(f"SELECT * FROM `{table_name}` LIMIT 1")
                columns = [column[0] for column in cursor.description]
                print(f"\nTable: {table_name}")
                print(f"Columns: {', '.join(columns)}")
                
                # If we find site_id or similar columns, show some sample data
                potential_id_columns = [col for col in columns if 'id' in col.lower() or 'site' in col.lower() or 'store' in col.lower()]
                if potential_id_columns:
                    id_col = potential_id_columns[0]
                    cursor.execute(f"SELECT {id_col} FROM `{table_name}` LIMIT 5")
                    sample_ids = cursor.fetchall()
                    if sample_ids:
                        print(f"Sample {id_col} values: {', '.join([str(row[0]) for row in sample_ids])}")
            except Exception as e:
                print(f"Error examining table {table_name}: {str(e)}")
        
        # Close the connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Connection failed: {str(e)}")

if __name__ == "__main__":
    test_connection() 