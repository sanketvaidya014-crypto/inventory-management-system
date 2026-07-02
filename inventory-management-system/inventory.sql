-- SQLite schema for the Inventory Management System.
-- The app (app.py) creates this table automatically on startup via init_db(),
-- so you normally do NOT need to run this file by hand. It is kept for reference
-- or if you want to inspect / seed the database with a SQLite client.

CREATE TABLE IF NOT EXISTS products (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category     TEXT,
    quantity     INTEGER,
    price        REAL,
    supplier     TEXT
);

-- Optional sample data (uncomment to seed):
-- INSERT INTO products (product_name, category, quantity, price, supplier) VALUES
--   ('Wireless Mouse', 'Electronics', 25, 19.99, 'Acme Co.'),
--   ('Notebook',       'Stationery',  3,  2.50,  'PaperWorks'),
--   ('USB-C Cable',    'Electronics', 40, 8.75,  'CablePro');
