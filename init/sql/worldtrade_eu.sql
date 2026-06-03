-- Création de la base (à exécuter séparément si nécessaire)
-- CREATE DATABASE worldtrade_eu;

\c worldtrade_eu;

-- Tables
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(50) NOT NULL,
    city VARCHAR(50),
    registration_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    unit_price_usd DECIMAL(10,2),
    supplier_id INTEGER
);

CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    contact_email VARCHAR(100)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id INTEGER REFERENCES products(product_id),
    order_date DATE NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price_usd DECIMAL(10,2) NOT NULL,
    total_amount_usd DECIMAL(10,2) GENERATED ALWAYS AS (quantity * unit_price_usd) STORED,
    currency VARCHAR(3) DEFAULT 'EUR',
    status VARCHAR(20) DEFAULT 'completed'
);

CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    order_id INTEGER UNIQUE REFERENCES orders(order_id),
    shipment_date DATE NOT NULL,
    carrier VARCHAR(50),
    tracking_number VARCHAR(100),
    estimated_delivery DATE,
    status VARCHAR(20)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER UNIQUE REFERENCES orders(order_id),
    payment_date DATE NOT NULL,
    amount_usd DECIMAL(10,2),
    method VARCHAR(30),
    status VARCHAR(20)
);

-- Insertion des données
INSERT INTO customers (first_name, last_name, email, country, city, registration_date) VALUES
('Jean', 'Dupont', 'jean.dupont@email.fr', 'France', 'Paris', '2023-01-10'),
('Maria', 'Schmidt', 'maria.schmidt@email.de', 'Germany', 'Berlin', '2023-02-15'),
('Luca', 'Rossi', 'luca.rossi@email.it', 'Italy', 'Rome', '2023-03-20'),
('Elena', 'Garcia', 'elena.garcia@email.es', 'Spain', 'Madrid', '2023-04-25'),
('William', 'Jones', 'william.jones@email.uk', 'United Kingdom', 'London', '2023-05-30'),
('Sophie', 'Martin', 'sophie.martin@email.fr', 'France', 'Lyon', '2023-06-05'),
('Hans', 'Müller', 'hans.muller@email.de', 'Germany', 'Munich', '2023-07-12'),
('Giulia', 'Bianchi', 'giulia.bianchi@email.it', 'Italy', 'Milan', '2023-08-18'),
('Pablo', 'Lopez', 'pablo.lopez@email.es', 'Spain', 'Barcelona', '2023-09-22'),
('Emily', 'Brown', 'emily.brown@email.uk', 'United Kingdom', 'Manchester', '2023-10-02'),
('Claire', 'Dubois', 'claire.dubois@email.fr', 'France', 'Toulouse', '2023-11-11'),
('Thomas', 'Weber', 'thomas.weber@email.de', 'Germany', 'Hamburg', '2023-12-15'),
('Marco', 'Ferrari', 'marco.ferrari@email.it', 'Italy', 'Naples', '2026-01-20'),
('Ana', 'Martinez', 'ana.martinez@email.es', 'Spain', 'Valencia', '2026-02-25'),
('Oliver', 'Smith', 'oliver.smith@email.uk', 'United Kingdom', 'Birmingham', '2026-03-10'),
('Camille', 'Lefevre', 'camille.lefevre@email.fr', 'France', 'Nice', '2026-04-15'),
('Lukas', 'Schneider', 'lukas.schneider@email.de', 'Germany', 'Cologne', '2026-05-20'),
('Sofia', 'Ricci', 'sofia.ricci@email.it', 'Italy', 'Turin', '2026-06-25'),
('Javier', 'Gomez', 'javier.gomez@email.es', 'Spain', 'Seville', '2026-07-30'),
('Chloe', 'Wilson', 'chloe.wilson@email.uk', 'United Kingdom', 'Glasgow', '2026-08-05');

INSERT INTO suppliers (supplier_name, country, contact_email) VALUES
('Fromages de France', 'France', 'contact@fromages.fr'),
('Bayerische Brauerei', 'Germany', 'info@bayern-brau.de'),
('Pasta Italia SRL', 'Italy', 'sales@pastaitalia.it'),
('Iberico Ham Suppliers', 'Spain', 'ham@iberico.es'),
('Tea & Biscuits UK', 'United Kingdom', 'hello@teabiscuits.co.uk'),
('Vins de Bourgogne', 'France', 'vins@bourgogne.fr'),
('Automotive Parts GmbH', 'Germany', 'parts@gmbh.de'),
('Luxury Leather Firenze', 'Italy', 'leather@firenze.it'),
('Olive Oil Andalusia', 'Spain', 'oil@andalucia.es'),
('Scottish Salmon', 'United Kingdom', 'salmon@scotland.uk');

INSERT INTO products (product_name, category, unit_price_usd, supplier_id) VALUES
('Camembert', 'Dairy', 5.99, 1),
('Heineken Beer', 'Beverage', 2.50, 2),
('Spaghetti', 'Pasta', 1.80, 3),
('Jamón Ibérico', 'Meat', 45.00, 4),
('Earl Grey Tea', 'Beverage', 4.20, 5),
('Chardonnay', 'Wine', 12.00, 6),
('Brake Pads', 'Auto', 35.00, 7),
('Leather Wallet', 'Accessory', 29.99, 8),
('Olive Oil', 'Grocery', 15.00, 9),
('Smoked Salmon', 'Seafood', 22.50, 10),
('Brie', 'Dairy', 7.50, 1),
('Wheat Beer', 'Beverage', 2.80, 2),
('Penne', 'Pasta', 1.60, 3),
('Chorizo', 'Meat', 18.00, 4),
('English Breakfast Tea', 'Beverage', 3.90, 5),
('Merlot', 'Wine', 11.00, 6),
('Car Brake Disc', 'Auto', 48.00, 7),
('Leather Belt', 'Accessory', 19.99, 8),
('Balsamic Vinegar', 'Grocery', 9.00, 9),
('Herring Fillets', 'Seafood', 14.00, 10);

INSERT INTO orders (customer_id, product_id, order_date, quantity, unit_price_usd, currency, status) VALUES
(1, 1, '2026-01-15', 2, 5.99, 'EUR', 'completed'),
(2, 2, '2026-01-20', 6, 2.50, 'EUR', 'completed'),
(3, 3, '2026-02-10', 3, 1.80, 'EUR', 'completed'),
(4, 4, '2026-02-18', 1, 45.00, 'EUR', 'completed'),
(5, 5, '2026-03-05', 4, 4.20, 'EUR', 'completed'),
(6, 6, '2026-03-12', 2, 12.00, 'EUR', 'completed'),
(7, 7, '2026-03-28', 1, 35.00, 'EUR', 'completed'),
(8, 8, '2026-04-04', 3, 29.99, 'EUR', 'completed'),
(9, 9, '2026-04-19', 2, 15.00, 'EUR', 'completed'),
(10, 10, '2026-05-01', 5, 22.50, 'EUR', 'completed'),
(11, 11, '2026-05-14', 3, 7.50, 'EUR', 'completed'),
(12, 12, '2026-05-27', 8, 2.80, 'EUR', 'completed'),
(13, 13, '2026-06-09', 2, 1.60, 'EUR', 'shipped'),
(14, 14, '2026-06-18', 1, 18.00, 'EUR', 'completed'),
(15, 15, '2026-07-02', 4, 3.90, 'EUR', 'completed'),
(16, 16, '2026-07-15', 2, 11.00, 'EUR', 'completed'),
(17, 17, '2026-07-28', 1, 48.00, 'EUR', 'pending'),
(18, 18, '2026-08-10', 3, 19.99, 'EUR', 'completed'),
(19, 19, '2026-08-22', 2, 9.00, 'EUR', 'completed'),
(20, 20, '2026-09-01', 4, 14.00, 'EUR', 'completed');

INSERT INTO shipments (order_id, shipment_date, carrier, tracking_number, estimated_delivery, status) VALUES
(1, '2026-01-16', 'DHL', 'EU123456789', '2026-01-20', 'delivered'),
(2, '2026-01-21', 'UPS', 'EU987654321', '2026-01-25', 'delivered'),
(3, '2026-02-11', 'FedEx', 'EU456123789', '2026-02-15', 'delivered'),
(4, '2026-02-19', 'DHL', 'EU321654987', '2026-02-23', 'delivered'),
(5, '2026-03-06', 'DPD', 'EU741852963', '2026-03-10', 'delivered'),
(6, '2026-03-13', 'UPS', 'EU852963741', '2026-03-17', 'delivered'),
(7, '2026-03-29', 'FedEx', 'EU963741852', '2026-04-02', 'delivered'),
(8, '2026-04-05', 'DHL', 'EU159753486', '2026-04-09', 'delivered'),
(9, '2026-04-20', 'DPD', 'EU357951862', '2026-04-24', 'delivered'),
(10, '2026-05-02', 'UPS', 'EU486215793', '2026-05-06', 'delivered'),
(11, '2026-05-15', 'DHL', 'EU789123456', '2026-05-19', 'delivered'),
(12, '2026-05-28', 'FedEx', 'EU321789654', '2026-06-01', 'delivered'),
(13, '2026-06-10', 'DPD', 'EU654987321', '2026-06-14', 'in_transit'),
(14, '2026-06-19', 'UPS', 'EU987123654', '2026-06-23', 'delivered'),
(15, '2026-07-03', 'DHL', 'EU159753852', '2026-07-07', 'delivered'),
(16, '2026-07-16', 'FedEx', 'EU753951486', '2026-07-20', 'delivered'),
(17, NULL, NULL, NULL, NULL, 'pending'),
(18, '2026-08-11', 'DPD', 'EU951753852', '2026-08-15', 'delivered'),
(19, '2026-08-23', 'UPS', 'EU852741963', '2026-08-27', 'delivered'),
(20, '2026-09-02', 'DHL', 'EU357159486', '2026-09-06', 'delivered');

INSERT INTO payments (order_id, payment_date, amount_usd, method, status) VALUES
(1, '2026-01-15', 11.98, 'Credit Card', 'completed'),
(2, '2026-01-20', 15.00, 'PayPal', 'completed'),
(3, '2026-02-10', 5.40, 'Bank Transfer', 'completed'),
(4, '2026-02-18', 45.00, 'Credit Card', 'completed'),
(5, '2026-03-05', 16.80, 'PayPal', 'completed'),
(6, '2026-03-12', 24.00, 'Credit Card', 'completed'),
(7, '2026-03-28', 35.00, 'Debit Card', 'completed'),
(8, '2026-04-04', 89.97, 'PayPal', 'completed'),
(9, '2026-04-19', 30.00, 'Credit Card', 'completed'),
(10, '2026-05-01', 112.50, 'Bank Transfer', 'completed'),
(11, '2026-05-14', 22.50, 'Credit Card', 'completed'),
(12, '2026-05-27', 22.40, 'PayPal', 'completed'),
(13, '2026-06-09', 3.20, 'Credit Card', 'completed'),
(14, '2026-06-18', 18.00, 'Debit Card', 'completed'),
(15, '2026-07-02', 15.60, 'PayPal', 'completed'),
(16, '2026-07-15', 22.00, 'Credit Card', 'completed'),
(17, '2026-07-28', 48.00, 'Bank Transfer', 'pending'),
(18, '2026-08-10', 59.97, 'Credit Card', 'completed'),
(19, '2026-08-22', 18.00, 'PayPal', 'completed'),
(20, '2026-09-01', 56.00, 'Credit Card', 'completed');