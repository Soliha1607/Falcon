ALTER TABLE shop_images ADD COLUMN my_order INT DEFAULT 0;

CREATE TABLE shop_customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone VARCHAR(15),
    billing_address TEXT,
    joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(255)
);



