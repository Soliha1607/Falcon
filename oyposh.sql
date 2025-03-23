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


CREATE TABLE shop_attribute (
    id SERIAL PRIMARY KEY,
    attribute_key VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE shop_attributevalue (
    id SERIAL PRIMARY KEY,
    attribute_value VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE shop_productattribute (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    attribute_key_id INTEGER NOT NULL,
    attribute_value_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES shop_product (id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_key_id) REFERENCES shop_attribute (id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_value_id) REFERENCES shop_attributevalue (id) ON DELETE CASCADE
);


ALTER TABLE shop_category ADD COLUMN slug VARCHAR(200) UNIQUE;

