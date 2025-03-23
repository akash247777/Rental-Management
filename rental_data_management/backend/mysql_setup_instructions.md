# MySQL Setup Instructions

## 1. Install MySQL Server

1. Download MySQL Server from the [official website](https://dev.mysql.com/downloads/mysql/)
2. During installation:
   - Choose a root password (the default in the application is `2#06A9a`)
   - Make sure to install MySQL Server and MySQL Workbench
   - Configure MySQL to start automatically

## 2. Configure Environment Variables (Optional)

Create a `.env` file in the `backend` directory with the following variables:

```
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=RENT
DB_USER=root
DB_PASSWORD=your_password
```

## 3. Initialize the Database

1. Install the required Python packages:
   ```
   pip install -r backend/requirements.txt
   ```

2. Run the database initialization script:
   ```
   python backend/create_mysql_db.py
   ```

3. This script will:
   - Create the RENT database if it doesn't exist
   - Create the USERS table
   - Create an admin user with username `admin` and password `admin123`
   - Create the RENTDETAILS table with the correct schema

## 4. Run the Application

Start the application:
```
python backend/app.py
```

## 5. Migrate Data (If Needed)

If you have existing data in SQL Server that you want to migrate:

1. Export the data from SQL Server to CSV files
2. Use MySQL Workbench to import the CSV files into the corresponding tables
3. Or use the application's upload feature to upload Excel files with the data 