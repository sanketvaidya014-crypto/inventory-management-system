from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret"

DB_PATH = os.path.join(os.path.dirname(__file__), "inventory.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL,
            supplier TEXT
        )
        """
    )
    conn.commit()
    conn.close()


@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    conn.close()
    return render_template("index.html", products=products)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    quantity = request.form['quantity']
    price = request.form['price']
    supplier = request.form['supplier']
    conn = get_db()
    conn.execute(
        "INSERT INTO products(product_name,category,quantity,price,supplier) VALUES(?,?,?,?,?)",
        (name, category, quantity, price, supplier),
    )
    conn.commit()
    conn.close()
    flash("Product Added")
    return redirect('/')


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
