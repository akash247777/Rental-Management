import pymysql
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '3306'))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '2#06A9a')

def create_database():
    try:
        # Connect to MySQL server
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        print("Creating database RENT if it doesn't exist...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS RENT")
        
        # Switch to the RENT database
        cursor.execute("USE RENT")
        
        # Create USERS table
        print("Creating USERS table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(80) UNIQUE NOT NULL,
                password VARCHAR(120) NOT NULL,
                role VARCHAR(20) NOT NULL DEFAULT 'user'
            )
        """)
        
        # Check if admin user exists
        cursor.execute("SELECT COUNT(*) FROM USERS WHERE username = 'admin'")
        admin_exists = cursor.fetchone()[0]
        
        # Create admin user if not exists
        if not admin_exists:
            print("Creating admin user...")
            hashed = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt())
            cursor.execute(
                "INSERT INTO USERS (username, password, role) VALUES (%s, %s, %s)",
                ('admin', hashed.decode('utf-8'), 'admin')
            )
        
        # Create RENTDETAILS table
        print("Creating RENTDETAILS table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS RENTDETAILS (
                ENTRY_NO INT AUTO_INCREMENT PRIMARY KEY,
                SITE VARCHAR(10) UNIQUE NOT NULL,
                `STORE NAME` VARCHAR(100) NOT NULL,
                REGION VARCHAR(50) NOT NULL,
                DIV VARCHAR(10) NOT NULL,
                MANAGER VARCHAR(100) NOT NULL,
                `ASST.MANAGER` VARCHAR(100) NOT NULL,
                EXECUTIVE VARCHAR(100) NOT NULL,
                `D.O.O` DATE NOT NULL,
                `SQ.FT` INT NOT NULL,
                `AGREEMENT DATE` DATE NOT NULL,
                `RENT POSITION DATE` DATE NOT NULL,
                `RENT EFFECTIVE DATE` DATE NOT NULL,
                `AGREEMENT VALID UPTO` DATE NULL,
                `CURRENT DATE` DATE NULL,
                `LEASE PERIOD` INT NOT NULL,
                RENT_FREE_PERIOD_DAYS INT NOT NULL,
                `RENT EFFECTIVE AMOUNT` FLOAT NOT NULL,
                `PRESENT RENT` FLOAT NOT NULL,
                `HIKE %` FLOAT NOT NULL,
                `HIKE YEAR` INT NOT NULL,
                `RENT DEPOSIT` FLOAT NOT NULL,
                `OWNER NAME-1` VARCHAR(100) NOT NULL,
                `OWNER NAME-2` VARCHAR(100) NULL,
                `OWNER NAME-3` VARCHAR(100) NULL,
                `OWNER NAME-4` VARCHAR(100) NULL,
                `OWNER NAME-5` VARCHAR(100) NULL,
                `OWNER NAME-6` VARCHAR(100) NULL,
                `OWNER MOBILE NUMBER` VARCHAR(20) NULL,
                `CURRENT DATE 1` VARCHAR(50) NULL,
                `VALIDITY DATE` VARCHAR(50) NULL,
                GST_NUMBER VARCHAR(20) NOT NULL,
                PAN_NUMBER VARCHAR(20) NOT NULL,
                TDS_PERCENTAGE FLOAT NOT NULL,
                MATURE VARCHAR(3) NOT NULL,
                STATUS VARCHAR(10) NOT NULL,
                REMARKS TEXT NULL
            )
        """)
        
        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        
        print("Database initialization completed successfully.")
        
    except Exception as e:
        print(f"Error creating database: {str(e)}")

if __name__ == "__main__":
    create_database() 