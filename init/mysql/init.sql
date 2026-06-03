-- Création de la base
CREATE DATABASE IF NOT EXISTS worldtrade_us;
USE worldtrade_us;

-- Tables
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    country VARCHAR(50),
    city VARCHAR(50),
    registration_date DATE DEFAULT (CURRENT_DATE)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price_usd DECIMAL(10,2),
    supplier_id INT
);

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100),
    country VARCHAR(50),
    contact_email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    unit_price_usd DECIMAL(10,2),
    total_amount_usd DECIMAL(10,2) GENERATED ALWAYS AS (quantity * unit_price_usd) STORED,
    currency VARCHAR(3) DEFAULT 'USD',
    status VARCHAR(20) DEFAULT 'completed',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE shipments (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT UNIQUE,
    shipment_date DATE,
    carrier VARCHAR(50),
    tracking_number VARCHAR(100),
    estimated_delivery DATE,
    status VARCHAR(20),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT UNIQUE,
    payment_date DATE,
    amount_usd DECIMAL(10,2),
    method VARCHAR(30),
    status VARCHAR(20),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insertions
INSERT INTO customers (first_name, last_name, email, country, city, registration_date) VALUES
('John', 'Smith', 'john.smith@email.com', 'USA', 'New York', '2023-01-10'),
('Emma', 'Johnson', 'emma.johnson@email.com', 'USA', 'Los Angeles', '2023-02-15'),
('Michael', 'Williams', 'michael.williams@email.com', 'USA', 'Chicago', '2023-03-20'),
('Sarah', 'Brown', 'sarah.brown@email.com', 'USA', 'Houston', '2023-04-25'),
('David', 'Jones', 'david.jones@email.com', 'USA', 'Phoenix', '2023-05-30'),
('Jessica', 'Garcia', 'jessica.garcia@email.com', 'USA', 'Philadelphia', '2023-06-05'),
('Daniel', 'Miller', 'daniel.miller@email.com', 'USA', 'San Antonio', '2023-07-12'),
('Laura', 'Davis', 'laura.davis@email.com', 'USA', 'San Diego', '2023-08-18'),
('James', 'Rodriguez', 'james.rodriguez@email.com', 'USA', 'Dallas', '2023-09-22'),
('Linda', 'Martinez', 'linda.martinez@email.com', 'USA', 'Austin', '2023-10-02'),
('Robert', 'Hernandez', 'robert.hernandez@email.com', 'USA', 'Jacksonville', '2023-11-11'),
('Patricia', 'Lopez', 'patricia.lopez@email.com', 'USA', 'Fort Worth', '2023-12-15'),
('Christopher', 'Gonzalez', 'chris.gonzalez@email.com', 'USA', 'Columbus', '2026-01-20'),
('Elizabeth', 'Wilson', 'elizabeth.wilson@email.com', 'USA', 'San Francisco', '2026-02-25'),
('Thomas', 'Anderson', 'thomas.anderson@email.com', 'USA', 'Charlotte', '2026-03-10'),
('Jennifer', 'Thomas', 'jennifer.thomas@email.com', 'USA', 'Detroit', '2026-04-15'),
('Charles', 'Taylor', 'charles.taylor@email.com', 'USA', 'El Paso', '2026-05-20'),
('Susan', 'Moore', 'susan.moore@email.com', 'USA', 'Memphis', '2026-06-25'),
('Matthew', 'Jackson', 'matthew.jackson@email.com', 'USA', 'Boston', '2026-07-30'),
('Ashley', 'Martin', 'ashley.martin@email.com', 'USA', 'Seattle', '2026-08-05');

INSERT INTO suppliers (supplier_name, country, contact_email) VALUES
('TechParts USA', 'USA', 'sales@techparts.com'),
('Midwest Foods', 'USA', 'info@midwestfoods.com'),
('California Wines', 'USA', 'wines@calwines.com'),
('Fashion Forward', 'USA', 'contact@fashionfwd.com'),
('AutoZone Supplies', 'USA', 'parts@autozone.com'),
('Green Grocery', 'USA', 'hello@greengrocery.com'),
('Pacific Seafood', 'USA', 'seafood@pacific.com'),
('Home Essentials', 'USA', 'support@homeessentials.com'),
('Sports Gear Inc', 'USA', 'gear@sportsinc.com'),
('BookWorld', 'USA', 'books@bookworld.com');

INSERT INTO products (product_name, category, unit_price_usd, supplier_id) VALUES
('Smartphone X', 'Electronics', 699.99, 1),
('Organic Coffee Beans', 'Grocery', 15.99, 2),
('Napa Valley Cabernet', 'Beverage', 28.50, 3),
('Leather Jacket', 'Apparel', 199.99, 4),
('Brake Pads Set', 'Auto', 45.00, 5),
('Avocado Box', 'Produce', 25.00, 6),
('Wild Salmon Fillet', 'Seafood', 18.99, 7),
('Memory Foam Pillow', 'Home', 39.99, 8),
('Basketball', 'Sports', 29.99, 9),
('Fiction Bestseller', 'Books', 14.99, 10),
('Wireless Earbuds', 'Electronics', 89.99, 1),
('Green Tea', 'Beverage', 12.50, 2),
('Chardonnay', 'Beverage', 22.00, 3),
('Sneakers', 'Apparel', 79.99, 4),
('Oil Filter', 'Auto', 12.50, 5),
('Strawberries', 'Produce', 6.99, 6),
('Shrimp Pack', 'Seafood', 24.99, 7),
('Bed Sheets Set', 'Home', 49.99, 8),
('Yoga Mat', 'Sports', 22.99, 9),
('Cookbook', 'Books', 19.99, 10);

INSERT INTO orders (customer_id, product_id, order_date, quantity, unit_price_usd, currency, status) VALUES
(1, 1, '2026-01-15', 1, 699.99, 'USD', 'completed'),
(2, 2, '2026-01-20', 2, 15.99, 'USD', 'completed'),
(3, 3, '2026-02-10', 1, 28.50, 'USD', 'completed'),
(4, 4, '2026-02-18', 1, 199.99, 'USD', 'completed'),
(5, 5, '2026-03-05', 2, 45.00, 'USD', 'completed'),
(6, 6, '2026-03-12', 5, 25.00, 'USD', 'completed'),
(7, 7, '2026-03-28', 3, 18.99, 'USD', 'completed'),
(8, 8, '2026-04-04', 2, 39.99, 'USD', 'completed'),
(9, 9, '2026-04-19', 1, 29.99, 'USD', 'completed'),
(10, 10, '2026-05-01', 4, 14.99, 'USD', 'completed'),
(11, 11, '2026-05-14', 1, 89.99, 'USD', 'completed'),
(12, 12, '2026-05-27', 3, 12.50, 'USD', 'completed'),
(13, 13, '2026-06-09', 2, 22.00, 'USD', 'shipped'),
(14, 14, '2026-06-18', 1, 79.99, 'USD', 'completed'),
(15, 15, '2026-07-02', 4, 12.50, 'USD', 'completed'),
(16, 16, '2026-07-15', 6, 6.99, 'USD', 'completed'),
(17, 17, '2026-07-28', 2, 24.99, 'USD', 'pending'),
(18, 18, '2026-08-10', 1, 49.99, 'USD', 'completed'),
(19, 19, '2026-08-22', 1, 22.99, 'USD', 'completed'),
(20, 20, '2026-09-01', 3, 19.99, 'USD', 'completed');

INSERT INTO shipments (order_id, shipment_date, carrier, tracking_number, estimated_delivery, status) VALUES
(1, '2026-01-16', 'UPS', '1Z999AA10123456784', '2026-01-19', 'delivered'),
(2, '2026-01-21', 'FedEx', '789456123012', '2026-01-24', 'delivered'),
(3, '2026-02-11', 'USPS', '9400112345678901234567', '2026-02-15', 'delivered'),
(4, '2026-02-19', 'DHL', '9876543210', '2026-02-23', 'delivered'),
(5, '2026-03-06', 'UPS', '1Z555AA10123456784', '2026-03-10', 'delivered'),
(6, '2026-03-13', 'FedEx', '123789456012', '2026-03-17', 'delivered'),
(7, '2026-03-29', 'USPS', '9400223456789012345678', '2026-04-02', 'delivered'),
(8, '2026-04-05', 'DHL', '4561237890', '2026-04-09', 'delivered'),
(9, '2026-04-20', 'UPS', '1Z777AA10123456784', '2026-04-24', 'delivered'),
(10, '2026-05-02', 'FedEx', '321654987012', '2026-05-06', 'delivered'),
(11, '2026-05-15', 'USPS', '94003345678901234567', '2026-05-19', 'delivered'),
(12, '2026-05-28', 'DHL', '1597534862', '2026-06-01', 'delivered'),
(13, '2026-06-10', 'UPS', '1Z888AA10123456784', '2026-06-14', 'in_transit'),
(14, '2026-06-19', 'FedEx', '753951486012', '2026-06-23', 'delivered'),
(15, '2026-07-03', 'USPS', '94004456789012345678', '2026-07-07', 'delivered'),
(16, '2026-07-16', 'DHL', '9517538520', '2026-07-20', 'delivered'),
(17, NULL, NULL, NULL, NULL, 'pending'),
(18, '2026-08-11', 'UPS', '1Z666AA10123456784', '2026-08-15', 'delivered'),
(19, '2026-08-23', 'FedEx', '852741963012', '2026-08-27', 'delivered'),
(20, '2026-09-02', 'USPS', '94005567890123456789', '2026-09-06', 'delivered');

INSERT INTO payments (order_id, payment_date, amount_usd, method, status) VALUES
(1, '2026-01-15', 699.99, 'Credit Card', 'completed'),
(2, '2026-01-20', 31.98, 'PayPal', 'completed'),
(3, '2026-02-10', 28.50, 'Bank Transfer', 'completed'),
(4, '2026-02-18', 199.99, 'Credit Card', 'completed'),
(5, '2026-03-05', 90.00, 'PayPal', 'completed'),
(6, '2026-03-12', 125.00, 'Debit Card', 'completed'),
(7, '2026-03-28', 56.97, 'Credit Card', 'completed'),
(8, '2026-04-04', 79.98, 'PayPal', 'completed'),
(9, '2026-04-19', 29.99, 'Credit Card', 'completed'),
(10, '2026-05-01', 59.96, 'Bank Transfer', 'completed'),
(11, '2026-05-14', 89.99, 'Credit Card', 'completed'),
(12, '2026-05-27', 37.50, 'PayPal', 'completed'),
(13, '2026-06-09', 44.00, 'Credit Card', 'completed'),
(14, '2026-06-18', 79.99, 'Debit Card', 'completed'),
(15, '2026-07-02', 50.00, 'PayPal', 'completed'),
(16, '2026-07-15', 41.94, 'Credit Card', 'completed'),
(17, '2026-07-28', 49.98, 'Bank Transfer', 'pending'),
(18, '2026-08-10', 49.99, 'Credit Card', 'completed'),
(19, '2026-08-22', 22.99, 'PayPal', 'completed'),
(20, '2026-09-01', 59.97, 'Credit Card', 'completed');