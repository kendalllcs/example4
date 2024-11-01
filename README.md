# PostgreSQL and Flask Integration Project

This project demonstrates how to connect PostgreSQL with Flask to perform database operations and display SQL SELECT results in an HTML table. It includes functionality to insert data into a PostgreSQL database and retrieve unique records, showcasing dynamic web application development with Python, Flask, and PostgreSQL.

## Team Members

- [Your Name]

## Project Overview

The application connects to a PostgreSQL database containing two tables, `basket_a` and `basket_b`. It provides the following functionalities:

1. **Insert a new row into `basket_a`:**
   - **Route:** `/api/update_basket_a`
   - **Functionality:** Inserts a new fruit, 'Cherry', into `basket_a`.
   - **Output:** Displays "Success!" upon successful insertion or an error message if it fails.

2. **Display unique fruits from both baskets:**
   - **Route:** `/api/unique`
   - **Functionality:** Retrieves unique fruits from `basket_a` and `basket_b` and displays them in an HTML table.
   - **Output:** An HTML table listing unique fruits from both baskets side by side.

## Prerequisites

- **Python 3.x**
- **PostgreSQL**
- **pgAdmin 4** (for database management)
- **pip** (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository/example_4
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv python_venv
```

Activate the virtual environment:

- On macOS and Linux:

  ```bash
  source python_venv/bin/activate
  ```

- On Windows:

  ```bash
  python_venv\Scripts\activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```
Flask==2.0.3
Jinja2==3.1.1
MarkupSafe==2.0.1
psycopg2
```

### 4. Database Setup Using pgAdmin 4

#### **a. Launch pgAdmin 4**

- Open pgAdmin 4 from your applications.

#### **b. Connect to Your PostgreSQL Server**

- Enter your PostgreSQL password if prompted.

#### **c. Create a New Database (If Not Already Created)**

1. Right-click on **Databases** in the Browser panel.
2. Select **Create** > **Database...**
3. Enter `db01` as the database name.
4. Click **Save**.

#### **d. Create the Required Tables and Insert Data**

1. Expand **Servers** > **Your Server** > **Databases** > **db01** > **Schemas** > **public**.
2. Right-click on **Tables** and select **Query Tool**.
3. In the SQL editor, paste the following SQL commands:

   ```sql
   CREATE TABLE basket_a (
       a INT PRIMARY KEY,
       fruit_a VARCHAR (100) NOT NULL
   );

   CREATE TABLE basket_b (
       b INT PRIMARY KEY,
       fruit_b VARCHAR (100) NOT NULL
   );

   INSERT INTO basket_a (a, fruit_a)
   VALUES
       (1, 'Apple'),
       (2, 'Orange'),
       (3, 'Banana'),
       (4, 'Cucumber');

   INSERT INTO basket_b (b, fruit_b)
   VALUES
       (1, 'Orange'),
       (2, 'Apple'),
       (3, 'Watermelon'),
       (4, 'Pear');
   ```

4. Click the **Execute/Refresh** button (lightning bolt icon) or press **F5**.

#### **e. Create the `customer` Table and Insert Data**

1. In the same SQL editor, execute the following commands:

   ```sql
   CREATE TABLE customer (
       customer_id SERIAL PRIMARY KEY,
       first_name VARCHAR(50),
       last_name VARCHAR(50),
       email VARCHAR(100)
   );

   INSERT INTO customer (first_name, last_name, email) VALUES
   ('John', 'Doe', 'john.doe@example.com'),
   ('Jane', 'Smith', 'jane.smith@example.com'),
   ('Alice', 'Johnson', 'alice.johnson@example.com'),
   ('Bob', 'Brown', 'bob.brown@example.com'),
   ('Charlie', 'Davis', 'charlie.davis@example.com');
   ```

5. Execute the commands.

### 5. Update Database Credentials

Open `main.py` and `util.py`, and update the database connection parameters with your PostgreSQL credentials:

#### **In `main.py`:**

```python
# Database configuration
username = 'your_postgres_username'  # Replace with your PostgreSQL username
password = 'your_postgres_password'  # Replace with your PostgreSQL password
host = '127.0.0.1'
port = '5432'
database = 'db01'  # Replace with your database name if different
```

#### **In `util.py`:**

```python
def connect_to_db(username='your_postgres_username', password='your_postgres_password', host='127.0.0.1', port='5432', database='db01'):
    # Existing code...
```

### 6. Verify File Structure

Ensure your project directory contains the following files:

- `main.py`
- `util.py`
- `requirements.txt`
- `README.md`
- A folder named `templates` containing:
  - `index.html`
  - `unique.html`

### 7. Run the Application

Start the Flask application by running:

```bash
python3 main.py
```

**Note:** If you're using Windows, you may need to use `python` instead of `python3`.

### 8. Access the Application

#### **a. View the Index Page**

- Open your web browser and navigate to:

  ```
  http://127.0.0.1:5000/
  ```

- You should see:

  - A static HTML table with university data.
  - A dynamic table displaying the first five entries from the `customer` table.

#### **b. Insert into `basket_a`**

- Navigate to:

  ```
  http://127.0.0.1:5000/api/update_basket_a
  ```

- Expected Output:

  - **Success!** if the insertion was successful.
  - An error message if there was a problem (e.g., duplicate primary key).

- **Verify the Insertion:**

  - In pgAdmin 4, run:

    ```sql
    SELECT * FROM basket_a;
    ```

  - You should see the new row `(5, 'Cherry')`.

#### **c. View Unique Fruits**

- Navigate to:

  ```
  http://127.0.0.1:5000/api/unique
  ```

- You should see an HTML table displaying unique fruits from both `basket_a` and `basket_b`.

## Project Structure

```
example_4/
│
├── main.py             # The main Flask application
├── util.py             # Utility functions for database operations
├── requirements.txt    # Python package dependencies
├── README.md           # Project documentation
└── templates/          # HTML templates
    ├── index.html      # Template for the index route
    └── unique.html     # Template for displaying unique fruits
```

## Detailed Code Explanation

### `main.py`

- **Imports:**

  ```python
  from flask import Flask, render_template
  import util
  ```

- **Application Instance:**

  ```python
  app = Flask(__name__)
  ```

- **Database Configuration:**

  ```python
  username = 'your_postgres_username'
  password = 'your_postgres_password'
  host = '127.0.0.1'
  port = '5432'
  database = 'db01'
  ```

- **Index Route `/`:**

  - Connects to the database.
  - Retrieves data from the `customer` table.
  - Renders `index.html` with the data.

- **Route `/api/update_basket_a`:**

  - Inserts a new fruit into `basket_a`.
  - Handles success and error messages.

- **Route `/api/unique`:**

  - Retrieves unique fruits from both baskets.
  - Renders `unique.html` with the data.

- **Running the Application:**

  ```python
  if __name__ == '__main__':
      app.debug = True
      ip = '127.0.0.1'
      app.run(host=ip)
  ```

### `util.py`

- **Functions:**

  - `connect_to_db()`: Establishes a connection to the database.
  - `disconnect_from_db()`: Closes the database connection.
  - `run_sql()`: Executes an SQL command without fetching results.
  - `run_and_fetch_sql()`: Executes an SQL command and fetches results.

### `index.html`

- Displays a static HTML table.
- Dynamically generates a table based on SQL results passed from `main.py`.

### `unique.html`

- Displays unique fruits from `basket_a` and `basket_b` in a side-by-side table.

## Troubleshooting

- **Database Connection Errors:**

  - Ensure PostgreSQL is running.
  - Verify your database credentials in `main.py` and `util.py`.
  - Check if the database `db01` exists and contains the necessary tables.

- **Module Import Errors:**

  - Ensure `util.py` is in the same directory as `main.py`.
  - Restart the Flask application after making changes.

- **Template Rendering Issues:**

  - Verify that templates are located in the `templates` directory.
  - Ensure the template file names match those used in `render_template()`.

- **Insertion Errors in `/api/update_basket_a`:**

  - If you receive a duplicate key error, modify the primary key in the insertion statement or delete existing entries with the same key.

## Additional Notes

- **Environment Variables (Optional):**

  - For security, consider using environment variables to store database credentials instead of hardcoding them.

- **Virtual Environment:**

  - Always activate your virtual environment before running the application to ensure you're using the correct dependencies.

- **Requirements File:**

  - Update `requirements.txt` if you install additional packages:

    ```bash
    pip freeze > requirements.txt
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PostgreSQL documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Psycopg2 documentation: [https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)
