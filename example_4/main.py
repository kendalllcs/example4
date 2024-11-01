from flask import Flask, render_template
import util

# Create an application instance
app = Flask(__name__)

# Database configuration
username = 'postgres'  # Replace with your PostgreSQL username
password = 'password'  # Replace with your PostgreSQL password
host = '127.0.0.1'
port = '5432'
database = 'db01'  # Replace with your database name

@app.route('/')
@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    if cursor is None:
        return "Error connecting to the database."

    success, record = util.run_and_fetch_sql(cursor, "SELECT * FROM customer;")
    if not success:
        print('Something is wrong with the SQL command')
        log = []
        col_names = []
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', sql_table=log, table_title=col_names)


# Add this route to insert a new row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        sql_string = "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');"
        cursor.execute(sql_string)
        connection.commit()  # Commit the transaction
        message = "Success!"
    except Exception as e:
        connection.rollback()  # Rollback in case of error
        message = f"Error: {str(e)}"
    finally:
        util.disconnect_from_db(connection, cursor)
    return message

# Add this route to display unique fruits from both baskets
@app.route('/api/unique')
def unique():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        # Get unique fruits from basket_a
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a;")
        fruits_a = [row[0] for row in cursor.fetchall()]

        # Get unique fruits from basket_b
        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b;")
        fruits_b = [row[0] for row in cursor.fetchall()]
    except Exception as e:
        message = f"Error: {str(e)}"
        util.disconnect_from_db(connection, cursor)
        return message
    finally:
        util.disconnect_from_db(connection, cursor)
    return render_template('unique.html', fruits_a=fruits_a, fruits_b=fruits_b)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
