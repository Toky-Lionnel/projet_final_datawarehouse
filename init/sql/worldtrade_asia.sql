-- CREATE DATABASE worldtrade_asia;
\c worldtrade_asia;

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
    currency VARCHAR(3) DEFAULT 'JPY',
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

INSERT INTO customers (first_name, last_name, email, country, city, registration_date) VALUES
('Takashi', 'Yamamoto', 'takashi.yamamoto@email.jp', 'Japan', 'Tokyo', '2023-01-10'),
('Wei', 'Chen', 'wei.chen@email.cn', 'China', 'Shanghai', '2023-02-15'),
('Priya', 'Patel', 'priya.patel@email.in', 'India', 'Mumbai', '2023-03-20'),
('Min-jun', 'Kim', 'minjun.kim@email.kr', 'South Korea', 'Seoul', '2023-04-25'),
('Anh', 'Nguyen', 'anh.nguyen@email.vn', 'Vietnam', 'Ho Chi Minh City', '2023-05-30'),
('Siti', 'Rahman', 'siti.rahman@email.my', 'Malaysia', 'Kuala Lumpur', '2023-06-05'),
('Yuki', 'Tanaka', 'yuki.tanaka@email.jp', 'Japan', 'Osaka', '2023-07-12'),
('Ling', 'Wang', 'ling.wang@email.cn', 'China', 'Beijing', '2023-08-18'),
('Raj', 'Kumar', 'raj.kumar@email.in', 'India', 'Delhi', '2023-09-22'),
('Ji-hoon', 'Park', 'jihoon.park@email.kr', 'South Korea', 'Busan', '2023-10-02'),
('Minh', 'Tran', 'minh.tran@email.vn', 'Vietnam', 'Hanoi', '2023-11-11'),
('Nur', 'Hassan', 'nur.hassan@email.my', 'Malaysia', 'Penang', '2023-12-15'),
('Haruki', 'Nakamura', 'haruki.nakamura@email.jp', 'Japan', 'Yokohama', '2026-01-20'),
('Xiao', 'Li', 'xiao.li@email.cn', 'China', 'Guangzhou', '2026-02-25'),
('Deepa', 'Singh', 'deepa.singh@email.in', 'India', 'Bangalore', '2026-03-10'),
('Soo-jin', 'Lee', 'soojin.lee@email.kr', 'South Korea', 'Incheon', '2026-04-15'),
('Quang', 'Pham', 'quang.pham@email.vn', 'Vietnam', 'Da Nang', '2026-05-20'),
('Aisha', 'Abdullah', 'aisha.abdullah@email.my', 'Malaysia', 'Johor Bahru', '2026-06-25'),
('Kenji', 'Suzuki', 'kenji.suzuki@email.jp', 'Japan', 'Nagoya', '2026-07-30'),
('Hong', 'Zhang', 'hong.zhang@email.cn', 'China', 'Shenzhen', '2026-08-05');

INSERT INTO suppliers (supplier_name, country, contact_email) VALUES
('Sony Electronics', 'Japan', 'supply@sony.co.jp'),
('Alibaba Group', 'China', 'sourcing@alibaba.com'),
('Tata Industries', 'India', 'procurement@tata.in'),
('Samsung Global', 'South Korea', 'partner@samsung.com'),
('VinGroup', 'Vietnam', 'supply@vingroup.vn'),
('Petronas Chemicals', 'Malaysia', 'trade@petronas.com.my'),
('Toyota Auto Parts', 'Japan', 'parts@toyota.jp'),
('Huawei Tech', 'China', 'buy@huawei.com'),
('Infosys Services', 'India', 'services@infosys.com'),
('LG Electronics', 'South Korea', 'supply@lg.com');

INSERT INTO products (product_name, category, unit_price_usd, supplier_id) VALUES
('4K TV 55"', 'Electronics', 599.99, 1),
('Smart Speaker', 'Electronics', 49.99, 2),
('Cotton T-Shirt', 'Apparel', 12.99, 3),
('SSD 1TB', 'Computer', 89.99, 4),
('Rice Cooker', 'Home', 45.00, 5),
('Palm Oil', 'Commodity', 35.00, 6),
('Car Battery', 'Auto', 120.00, 7),
('Smartphone', 'Electronics', 399.99, 8),
('Software License', 'IT', 299.99, 9),
('Refrigerator', 'Home', 799.99, 10),
('Headphones', 'Electronics', 79.99, 1),
('Tea Set', 'Home', 34.99, 2),
('Silk Scarf', 'Apparel', 45.00, 3),
('Laptop Stand', 'Computer', 29.99, 4),
('Air Fryer', 'Home', 89.99, 5),
('Rubber Gloves', 'Industrial', 5.00, 6),
('Motor Oil', 'Auto', 25.00, 7),
('Tablet', 'Electronics', 249.99, 8),
('Cloud Storage', 'IT', 99.99, 9),
('Vacuum Cleaner', 'Home', 149.99, 10);

INSERT INTO orders (customer_id, product_id, order_date, quantity, unit_price_usd, currency, status) VALUES
(1, 1, '2026-01-15', 1, 599.99, 'JPY', 'completed'),
(2, 2, '2026-01-20', 3, 49.99, 'CNY', 'completed'),
(3, 3, '2026-02-10', 5, 12.99, 'INR', 'completed'),
(4, 4, '2026-02-18', 2, 89.99, 'KRW', 'completed'),
(5, 5, '2026-03-05', 1, 45.00, 'VND', 'completed'),
(6, 6, '2026-03-12', 4, 35.00, 'MYR', 'completed'),
(7, 7, '2026-03-28', 1, 120.00, 'JPY', 'completed'),
(8, 8, '2026-04-04', 2, 399.99, 'CNY', 'completed'),
(9, 9, '2026-04-19', 1, 299.99, 'INR', 'completed'),
(10, 10, '2026-05-01', 1, 799.99, 'KRW', 'completed'),
(11, 11, '2026-05-14', 2, 79.99, 'VND', 'completed'),
(12, 12, '2026-05-27', 3, 34.99, 'MYR', 'completed'),
(13, 13, '2026-06-09', 1, 45.00, 'JPY', 'shipped'),
(14, 14, '2026-06-18', 4, 29.99, 'CNY', 'completed'),
(15, 15, '2026-07-02', 1, 89.99, 'INR', 'completed'),
(16, 16, '2026-07-15', 10, 5.00, 'KRW', 'completed'),
(17, 17, '2026-07-28', 2, 25.00, 'VND', 'pending'),
(18, 18, '2026-08-10', 1, 249.99, 'MYR', 'completed'),
(19, 19, '2026-08-22', 3, 99.99, 'JPY', 'completed'),
(20, 20, '2026-09-01', 1, 149.99, 'CNY', 'completed');

INSERT INTO shipments (order_id, shipment_date, carrier, tracking_number, estimated_delivery, status) VALUES
(1, '2026-01-16', 'Yamato', 'JP1234567890', '2026-01-20', 'delivered'),
(2, '2026-01-21', 'SF Express', 'CN9876543210', '2026-01-25', 'delivered'),
(3, '2026-02-11', 'DTDC', 'IN4561237890', '2026-02-15', 'delivered'),
(4, '2026-02-19', 'CJ Logistics', 'KR3216549870', '2026-02-23', 'delivered'),
(5, '2026-03-06', 'Viettel Post', 'VN7418529630', '2026-03-10', 'delivered'),
(6, '2026-03-13', 'Pos Malaysia', 'MY8529637410', '2026-03-17', 'delivered'),
(7, '2026-03-29', 'Yamato', 'JP9637418520', '2026-04-02', 'delivered'),
(8, '2026-04-05', 'SF Express', 'CN1597534860', '2026-04-09', 'delivered'),
(9, '2026-04-20', 'DTDC', 'IN3579518620', '2026-04-24', 'delivered'),
(10, '2026-05-02', 'CJ Logistics', 'KR4862157930', '2026-05-06', 'delivered'),
(11, '2026-05-15', 'Viettel Post', 'VN7891234560', '2026-05-19', 'delivered'),
(12, '2026-05-28', 'Pos Malaysia', 'MY3217896540', '2026-06-01', 'delivered'),
(13, '2026-06-10', 'Yamato', 'JP6549873210', '2026-06-14', 'in_transit'),
(14, '2026-06-19', 'SF Express', 'CN9871236540', '2026-06-23', 'delivered'),
(15, '2026-07-03', 'DTDC', 'IN1597538520', '2026-07-07', 'delivered'),
(16, '2026-07-16', 'CJ Logistics', 'KR7539514860', '2026-07-20', 'delivered'),
(17, NULL, NULL, NULL, NULL, 'pending'),
(18, '2026-08-11', 'Viettel Post', 'VN9517538520', '2026-08-15', 'delivered'),
(19, '2026-08-23', 'Pos Malaysia', 'MY8527419630', '2026-08-27', 'delivered'),
(20, '2026-09-02', 'Yamato', 'JP3571594860', '2026-09-06', 'delivered');

INSERT INTO payments (order_id, payment_date, amount_usd, method, status) VALUES
(1, '2026-01-15', 599.99, 'Credit Card', 'completed'),
(2, '2026-01-20', 149.97, 'Alipay', 'completed'),
(3, '2026-02-10', 64.95, 'Paytm', 'completed'),
(4, '2026-02-18', 179.98, 'KakaoPay', 'completed'),
(5, '2026-03-05', 45.00, 'Bank Transfer', 'completed'),
(6, '2026-03-12', 140.00, 'Touch n Go', 'completed'),
(7, '2026-03-28', 120.00, 'Credit Card', 'completed'),
(8, '2026-04-04', 799.98, 'WeChat Pay', 'completed'),
(9, '2026-04-19', 299.99, 'Paytm', 'completed'),
(10, '2026-05-01', 799.99, 'KakaoPay', 'completed'),
(11, '2026-05-14', 159.98, 'Credit Card', 'completed'),
(12, '2026-05-27', 104.97, 'Touch n Go', 'completed'),
(13, '2026-06-09', 45.00, 'Alipay', 'completed'),
(14, '2026-06-18', 119.96, 'WeChat Pay', 'completed'),
(15, '2026-07-02', 89.99, 'Paytm', 'completed'),
(16, '2026-07-15', 50.00, 'KakaoPay', 'completed'),
(17, '2026-07-28', 50.00, 'Bank Transfer', 'pending'),
(18, '2026-08-10', 249.99, 'Credit Card', 'completed'),
(19, '2026-08-22', 299.97, 'Alipay', 'completed'),
(20, '2026-09-01', 149.99, 'WeChat Pay', 'completed');