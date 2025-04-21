#!/bin/bash

if [[ $1 == "test" ]]
then
  psql="psql --username=postgres --dbname=e_library -t --no-align -c"
else
  psql="psql --username=postgres --dbname=e_library -t --no-align -c"
fi
# Do not change code above this line. Use the PSQL variable above to query your database.

# Clear existing data
echo "🧹 Truncating all tables..."
$psql "TRUNCATE users, addresses, libraries, categories, authors, books, book_categories, libraries_books, books_loans, books_holds RESTART IDENTITY CASCADE;"

# Insert data from users.csv
echo "Inserting data into users table..."
cat dummy_elibrary/users.csv | while IFS=',' read username password name gender birth_date birth_place email phone_number created_at is_deleted

do
  if [[ $username != "username" ]]
  then
    $psql "INSERT INTO users ( 
                                username, 
                                password, 
                                name, gender, 
                                birth_date, 
                                birth_place, 
                                email, 
                                phone_number, 
                                created_at, 
                                is_deleted
    ) 
            VALUES     (
                        '$username', 
                        '$password', 
                        '$name', 
                        '$gender', 
                        '$birth_date', 
                        '$birth_place', 
                        '$email', 
                        '$phone_number', 
                        '$created_at', 
                        '$is_deleted'
    );"
  fi
done

# Insert data from addresses.csv
echo "Inserting data into addresses table..."
cat dummy_elibrary/addresses.csv | while IFS=',' read user_id address_type street subdistrict city province postal_code created_at is_deleted
do
  if [[ $address_type != "address_type" ]]
  then
    $psql "INSERT INTO addresses (
                                user_id, 
                                address_type, 
                                street, 
                                subdistrict, 
                                city, 
                                province, 
                                postal_code, 
                                created_at, 
                                is_deleted
    ) 
            VALUES        (
                            '$user_id', 
                            '$address_type', 
                            '$street', 
                            '$subdistrict', 
                            '$city', 
                            '$province', 
                            '$postal_code', 
                            '$created_at', 
                            '$is_deleted'
    );"
  fi
done

# Insert data from libraries.csv
echo "Inserting data into libraries table..."
cat dummy_elibrary/libraries.csv | while IFS=',' read  library_name street subdistrict city province phone_number created_at
do
  if [[ $library_name != "library_name" ]]
  then
    $psql "INSERT INTO libraries ( 
                                    library_name, 
                                    street, 
                                    subdistrict, 
                                    city, 
                                    province, 
                                    phone_number, 
                                    created_at
    ) 
            VALUES     (
                        '$library_name', 
                        '$street', 
                        '$subdistrict', 
                        '$city', 
                        '$province', 
                        '$phone_number', 
                        '$created_at'
    );"
  fi
done

# Insert data from categories.csv
echo "Inserting data into categories table..."
cat dummy_elibrary/categories.csv | while IFS=',' read category_name created_at
do
  if [[ $category_name != "category_name" ]]
  then
    $psql "INSERT INTO categories ( 
                                    category_name, 
                                    created_at
    ) 
            VALUES ( 
                        '$category_name', 
                        '$created_at'
    );"
  fi
done

# Insert data from authors.csv
echo "Inserting data into authors table..."
cat dummy_elibrary/authors.csv | while IFS=',' read author_name created_at
do
  if [[ $author_name != "author_name" ]]
  then
    $psql "INSERT INTO authors (
                                author_name, 
                                created_at
    ) 
            VALUES (
                    '$author_name', 
                    '$created_at'
    );"
  fi
done

# Insert data from books.csv
echo "Inserting data into books table..."
cat dummy_elibrary/books.csv | while IFS=',' read title date_release author_id is_deleted
do
  if [[ $title != "title" ]]
  then
    $psql "INSERT INTO books (
                                title, 
                                date_release, 
                                author_id, 
                                is_deleted
    ) 
            VALUES (
                    '$title', 
                    '$date_release', 
                    '$author_id', 
                    '$is_deleted'
    );"
  fi
done

# Insert data from book_categories.csv
echo "Inserting data into book_categories table..."
cat dummy_elibrary/book_categories.csv | while IFS=',' read  book_id category_id 
do
  if [[ $book_id != "book_id" ]]
  then
    $psql "INSERT INTO book_categories (
                                        book_id, 
                                        category_id
    ) 
            VALUES (
                    '$book_id', 
                    '$category_id'
    );"
  fi
done

# Insert data from libraries_books.csv
echo "Inserting data into libraries_books table..."
cat dummy_elibrary/libraries_books.csv | while IFS=',' read  library_id book_id stock stock_out
do
  if [[ $library_id != "library_id" ]]
  then
    $psql "INSERT INTO libraries_books (
                                        library_id, 
                                        book_id, 
                                        stock, 
                                        stock_out
    ) 
            VALUES (
                    '$library_id', 
                    '$book_id', 
                    '$stock', 
                    '$stock_out'
    );"
  fi
done

# Insert data from books_loans.csv
echo "Inserting data into books_loans table..."
cat dummy_elibrary/books_loans.csv | while IFS=',' read user_id book_id library_id loan_date due_date return_date loan_quantity is_deleted
do
  if [[ $user_id != "user_id" ]]  
  then
    # Handle return_date as NULL if it's empty
    if [[ -z "$return_date" ]]; then
      return_date_value="NULL"  # if return_date is empity, set as NULL
    else
      return_date_value="'$return_date'"  # If there's a value, use the return_date
    fi

    # Run the INSERT statement, with return_date being NULL if it's empty
    $psql "INSERT INTO books_loans (
                                    user_id, 
                                    book_id, 
                                    library_id, 
                                    loan_date, 
                                    due_date, 
                                    return_date, 
                                    loan_quantity, 
                                    is_deleted
    ) 
            VALUES (
                    '$user_id', 
                    '$book_id', 
                    '$library_id', 
                    '$loan_date', 
                    '$due_date', 
                    $return_date_value, 
                    '$loan_quantity', 
                    '$is_deleted'
    );"
  fi
done


#insert data from books_holds.csv
echo "Inserting data into books_holds table..."
cat dummy_elibrary/books_holds.csv | while IFS=',' read user_id book_id library_id hold_date expire_date status queue_position is_deleted
do
  if [[ $user_id != "user_id" ]]
  then
    $psql "INSERT INTO books_holds (
                                    user_id, 
                                    book_id, 
                                    library_id, 
                                    hold_date, 
                                    expire_date, 
                                    status, 
                                    queue_position, 
                                    is_deleted
    ) 
            VALUES (
                    '$user_id', 
                    '$book_id', 
                    '$library_id', 
                    '$hold_date', 
                    '$expire_date', 
                    '$status', 
                    '$queue_position', 
                    '$is_deleted'
    );"
  fi
done

echo "Dummy data successfully inserted into e-library database!"
