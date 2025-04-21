-- crate database for e_library
-- CREATE DATABASE e_library;

-- ENUM for address type
CREATE TYPE address_type_enum AS ENUM ('domisili', 'ktp');

-- ENUM for gender
CREATE TYPE gender_enum AS ENUM ('male', 'female');


-- ==========================
-- SECTION: CREATE TABLES
-- ==========================

-- data user
CREATE TABLE users (
    user_id         SERIAL PRIMARY KEY,
    username        VARCHAR(255) NOT NULL UNIQUE,
    password        VARCHAR(255) NOT NULL,
    name            VARCHAR(255) NOT NULL,
    gender          gender_enum NOT NULL,
    birth_date      DATE NOT NULL,
    birth_place     VARCHAR(255) NOT NULL,
    email           VARCHAR(255) NOT NULL UNIQUE,
    phone_number    VARCHAR(15) NOT NULL UNIQUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted       BOOLEAN DEFAULT FALSE
);

-- data address
CREATE TABLE addresses (
    address_id      SERIAL PRIMARY KEY,
    user_id         INT NOT NULL,
    address_type    address_type_enum NOT NULL,
    street          VARCHAR(255) ,
    subdistrict     VARCHAR(225) NOT NULL,
    city            VARCHAR(255) NOT NULL,
    province        VARCHAR(255) NOT NULL,
    postal_code     VARCHAR(255) NOT NULL ,   created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted       BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);

-- data libraries
CREATE TABLE libraries (
    library_id      SERIAL PRIMARY KEY,
    library_name    VARCHAR(255) NOT NULL,
    street          VARCHAR(255),
    subdistrict     VARCHAR(225) NOT NULL,
    city            VARCHAR(255) NOT NULL,
    province        VARCHAR(225) NOT NULL,
    phone_number    VARCHAR(15) NOT NULL UNIQUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- data category
CREATE TABLE categories (
    category_id     SERIAL PRIMARY KEY,
    category_name   VARCHAR(255) NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- data author
CREATE TABLE authors (
    author_id       SERIAL PRIMARY KEY,
    author_name     VARCHAR(255) NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- data books
CREATE TABLE books (
    book_id         SERIAL PRIMARY KEY,
    title           VARCHAR(255) NOT NULL,
    date_release    DATE NOT NULL,
    author_id       INT NOT NULL,
    is_deleted      BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE NO ACTION
);

-- data book_categories
CREATE TABLE book_categories (
    book_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- data libraries_books
CREATE TABLE libraries_books (
    library_id      INT NOT NULL,
    book_id         INT NOT NULL,
    stock           INT NOT NULL CHECK (stock >= 0),
    stock_out       INT NOT NULL CHECK (stock_out >= 0),
    PRIMARY KEY     (library_id, book_id),
    FOREIGN KEY     (library_id) REFERENCES libraries(library_id) ON DELETE CASCADE,
    FOREIGN KEY     (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);

-- data books loan
CREATE TABLE books_loans (
    loan_id         SERIAL PRIMARY KEY,
    user_id         INT NOT NULL,
    book_id         INT NOT NULL,
    library_id      INT NOT NULL,
    loan_date       DATE NOT NULL,
    due_date        DATE NOT NULL,
    return_date     DATE,
    loan_quantity   INT NOT NULL CHECK (loan_quantity >= 1 AND loan_quantity <= 2),
    is_deleted      BOOLEAN DEFAULT FALSE,
    FOREIGN KEY     (user_id) REFERENCES users(user_id) ON DELETE NO ACTION,
    FOREIGN KEY     (book_id) REFERENCES books(book_id) ON DELETE NO ACTION,
    FOREIGN KEY     (library_id) REFERENCES libraries(library_id) ON DELETE NO ACTION
);

-- data books hold
CREATE TABLE books_holds (
    hold_id         SERIAL PRIMARY KEY,
    user_id         INT NOT NULL,
    book_id         INT NOT NULL,
    library_id      INT NOT NULL,
    hold_date       DATE NOT NULL,
    expire_date     DATE NOT NULL,
    status          TEXT NOT NULL CHECK (status IN ('waiting', 'fulfilled', 'expired')),
    queue_position  INT NOT NULL,
    is_deleted      BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE NO ACTION,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE NO ACTION,
    FOREIGN KEY (library_id) REFERENCES libraries(library_id) ON DELETE NO ACTION
);


--View: Book Availability
CREATE VIEW     book_availability AS
SELECT          lb.library_id,
                lb.book_id,
                b.title,
                l.library_name,
                lb.stock,
                lb.stock_out,
                (lb.stock - lb.stock_out) AS available
FROM            libraries_books lb
JOIN            books b ON lb.book_id = b.book_id
JOIN            libraries l ON lb.library_id = l.library_id;
