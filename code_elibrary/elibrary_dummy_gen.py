import os
import random
import pandas as pd
from faker import Faker
from datetime import timedelta

# Set global seed so Faker generates consistent data each run Faker.seed(0)
class Elibrary_dummy_generator:
    def __init__(self):
        """
        Initialize a new Elibrary_dummy_generator object.

        This function initializes a new Elibrary_dummy_generator object.
        It sets the self.fake attribute to a new Faker object.
        """
        self.fake = Faker()



    
    # Generate a random phone number
    def generate_phone_number(self):
        """
        Generate a random phone number.

        This function generates a random phone number.
        It uses Faker's unique.msisdn() and country_calling_code() functions to generate a random MSISDN and country code.
        It then combines the two and cuts it to a random length between 11 and 15 characters.

        Returns:
            str: a random phone number
        """
        msisdn = self.fake.unique.msisdn() 
        number = self.fake.country_calling_code()
        phone_number = f"({number}) {msisdn}"
        length = random.randint(13, 15)  
        return phone_number[:length] 




    # Generate user data
    def generate_users(self, n):
        """
        Generate a DataFrame of dummy user data.

        This function creates a DataFrame containing dummy user data for a specified number of users.
        Each user entry includes a unique username, a random password, name, gender, birth date,
        birth place, unique email, unique phone number, creation date, and a flag indicating if the user
        is deleted.

        Args:
            n (int): The number of user records to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the generated user data.
        """

        genders = ['male', 'female']
        return pd.DataFrame([{
            'username': self.fake.unique.user_name(),
            'password': self.fake.password(length=12),
            'name': self.fake.name(),
            'gender': random.choice(genders),
            'birth_date': self.fake.date_of_birth(minimum_age=18),
            'birth_place': self.fake.city(),
            'email': self.fake.unique.email(),
            'phone_number': self.generate_phone_number(),
            'created_at': self.fake.date_time_this_decade(),
            'is_deleted': False
        } for i in range(n)])




    # Generate address data for each user (KTP and domicile)
    def generate_addresses(self, n_users):
        """
        Generate a DataFrame of dummy address data for a specified number of users.

        This function creates a DataFrame containing dummy address data for a specified number of users.
        Each user entry includes a unique user_id, address_type (ktp or domisili), street, subdistrict, city,
        province, postal_code, creation date, and a flag indicating if the address is deleted.

        Args:
            n_users (int): The number of user records to generate addresses for.

        Returns:
            pd.DataFrame: A DataFrame containing the generated address data.
        """
        addresses = []
        for user_id in range(1, n_users + 1):
            # user must have a ktp as address_type
            addresses.append({
            'user_id': user_id,
            'address_type': 'ktp',
            'street': self.fake.street_address(),
            'subdistrict': self.fake.city_suffix(),
            'city': self.fake.city(),
            'province': self.fake.state(),
            'postal_code': self.fake.postcode(),
            'created_at': self.fake.date_time_this_decade(),
            'is_deleted': False
            })
            # randomly add 'domisili' address_type
            if random.choice([True, False]):
                addresses.append({
                    'user_id': user_id,
                    'address_type': 'domisili',
                    'street': self.fake.street_address(),
                    'subdistrict': self.fake.city_suffix(),
                    'city': self.fake.city(),
                    'province': self.fake.state(),
                    'postal_code': self.fake.postcode(),
                    'created_at': self.fake.date_time_this_decade(),
                    'is_deleted': False   
                })
                            
        return pd.DataFrame(addresses)




    # Generate library data
    def generate_libraries(self, n):
        """
        Generate a DataFrame of dummy library data.

        This function creates a DataFrame containing dummy library data for a specified number of libraries.
        Each library entry includes a library name, street address, subdistrict, city, province, phone number,
        and creation date.

        Args:
            n (int): The number of library records to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the generated library data.
        """

        
        return pd.DataFrame([{
            'library_name': f"{self.fake.last_name()} Library",
            'street': self.fake.street_address(),
            'subdistrict': self.fake.city_suffix(),
            'city': self.fake.city(),
            'province': self.fake.state(),
            'phone_number': self.generate_phone_number(),
            'created_at': self.fake.date_time_this_decade()
        } for _ in range(n)])
 
 
   
    
    # Generate category data for book
    def generate_categories(self, n):
        """
        Generate a DataFrame of dummy book categories.

        This function creates a DataFrame containing dummy book category data for a specified number of categories.
        Each category entry includes a category name and creation date.

        Args:
            n (int): The number of category records to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the generated category data.
        """
    
        return pd.DataFrame([{
            'category_name': self.fake.word().capitalize(),
            'created_at': self.fake.date_time_this_decade()
        } for _ in range(n)])

    # Generate author for book
    def generate_authors(self, n):
        """
        Generate a DataFrame of dummy book authors.

        This function creates a DataFrame containing dummy book author data for a specified number of authors.
        Each author entry includes an author name and creation date.

        Args:
            n (int): The number of author records to generate.

        Returns:
            pd.DataFrame: A DataFrame containing the generated author data.
        """
        return pd.DataFrame([{
            'author_name': self.fake.name(),
            'created_at': self.fake.date_time_this_decade()
        } for _ in range(n)])



            
    # Generate book data linked to authors
    def generate_books(self, n, author_count):
        """
        Generate a DataFrame of dummy book data.

        This function creates a DataFrame containing dummy book data for a specified number of books.
        Each book entry includes a title, release date, author_id, and a flag indicating if the book is deleted.

        Args:
            n (int): The number of book records to generate.
            author_count (int): The number of total authors available for the books.

        Returns:
            pd.DataFrame: A DataFrame containing the generated book data.
        """
        return pd.DataFrame([{
            'title': self.fake.sentence(nb_words=4).rstrip('.'),
            'date_release': self.fake.date_between(start_date='-10y', end_date='today'),
            'author_id': random.randint(1, author_count),
            'is_deleted': False
        } for _ in range(n)])




    # Generate many-to-many relationship between books and categories
    def generate_book_categories(self, n_books, n_categories):
        """
        Generate a DataFrame of dummy book to category many-to-many relationship.

        This function creates a DataFrame containing dummy many-to-many relationship between books and categories.
        Each book is assigned to two random categories.

        Args:
            n_books (int): The number of book records to generate relationships for.
            n_categories (int): The number of total categories available for the books.

        Returns:
            pd.DataFrame: A DataFrame containing the generated book to category relationships.
        """
        pairs = set()
        while len(pairs) < n_books * 2:
            pairs.add((
                random.randint(1, n_books),
                random.randint(1, n_categories)
            ))
        return pd.DataFrame(list(pairs), columns=['book_id', 'category_id'])

    # Generate book stock data per library
    def generate_libraries_books(self, n_books, n_libraries):
        """
        Generate a DataFrame of dummy library book stock data.

        This function creates a DataFrame containing dummy library book stock data for a specified number of books and libraries.
        Each book is assigned to a random number of libraries between 1 and 3, and each assignment includes the library_id, book_id, stock, and stock_out.

        Args:
            n_books (int): The number of book records to generate relationships for.
            n_libraries (int): The number of total libraries available for the books.

        Returns:
            pd.DataFrame: A DataFrame containing the generated library book stock data.
        """
        records = []
        for book_id in range(1, n_books + 1):
            for lib_id in random.sample(range(1, n_libraries + 1), k=min(random.randint(1, 3), n_libraries)):
                stock = random.randint(1, 20)
                stock_out = random.randint(0, stock)
                records.append({
                    'library_id': lib_id,
                    'book_id': book_id,
                    'stock': stock,
                    'stock_out': stock_out
                })
        return pd.DataFrame(records)




    # Generate book loan (borrowing) data
    def generate_books_loans(self, n, n_users, n_books, n_libraries):
        """
        Generate a DataFrame of dummy book loan data.

        This function creates a DataFrame containing dummy book loan data for a specified number of loans.
        Each loan entry includes a user_id, book_id, library_id, loan_date, due_date, return_date, loan_quantity, and a flag indicating if the loan is deleted.

        Args:
            n (int): The number of loan records to generate.
            n_users (int): The number of total users available for the loans.
            n_books (int): The number of total books available for the loans.
            n_libraries (int): The number of total libraries available for the loans.

        Returns:
            pd.DataFrame: A DataFrame containing the generated book loan data.
        """
        data = []
        for _ in range(n):
            loan_date = self.fake.date_between(start_date='-2y', end_date='today')
            due_date = loan_date + timedelta(days=14)
            return_date = random.choice(['Null', due_date + timedelta(days=random.randint(-3, 5))])
            data.append({
                'user_id': random.randint(1, n_users),
                'book_id': random.randint(1, n_books),
                'library_id': random.randint(1, n_libraries),
                'loan_date': loan_date,
                'due_date': due_date,
                'return_date': return_date,
                'loan_quantity': random.randint(1, 2),
                'is_deleted': False
            })
        return pd.DataFrame(data)




    # Generate book hold (booking) data
    def generate_books_holds(self, n, n_users, n_books, n_libraries):
        """
        Generate a DataFrame of dummy book hold data.

        This function creates a DataFrame containing dummy book hold data for a specified number of holds.
        Each hold entry includes a user_id, book_id, library_id, hold_date, expire_date, status, queue_position, and a flag indicating if the hold is deleted.

        Args:
            n (int): The number of hold records to generate.
            n_users (int): The number of total users available for the holds.
            n_books (int): The number of total books available for the holds.
            n_libraries (int): The number of total libraries available for the holds.

        Returns:
            pd.DataFrame: A DataFrame containing the generated book hold data.
        """
        statuses = ['waiting', 'fulfilled', 'expired']
        data = []
        for _ in range(n):
            hold_date = self.fake.date_between(start_date='-1y', end_date='today')
            expire_date = hold_date + timedelta(days=7)
            data.append({
                'user_id': random.randint(1, n_users),
                'book_id': random.randint(1, n_books),
                'library_id': random.randint(1, n_libraries),
                'hold_date': hold_date,
                'expire_date': expire_date,
                'status': random.choice(statuses),
                'queue_position': random.randint(1, 10),
                'is_deleted': False
            })
        return pd.DataFrame(data)




# prompt user for input and save generated data to CSV
def save_data_to_csv():
    """
    Generate and save dummy data for an e-library system to CSV files.

    This function prompts the user to input the number of records to generate for various e-library entities 
    such as users, libraries, categories, authors, books, book loans, and book holds. It then generates 
    the dummy data using the Elibrary_dummy_generator class and saves each dataset to a corresponding CSV file 
    in the "dummy_elibrary" directory.

    The CSV files saved include:
    - users.csv: Contains user data
    - addresses.csv: Contains addresses data associated with users
    - libraries.csv: Contains library data
    - categories.csv: Contains book category data
    - authors.csv: Contains author data
    - books.csv: Contains book data linked to authors
    - book_categories.csv: Contains many-to-many relationships between books and categories
    - libraries_books.csv: Contains library book stock data
    - books_loans.csv: Contains book loan data
    - books_holds.csv: Contains book hold data

    The function ensures that the output directory "dummy_elibrary" exists before saving the CSV files.
    """

    gen = Elibrary_dummy_generator()

    # Ask the user for the number of records to generate for each table
    print("Masukkan jumlah data yang ingin digenerate:")
    n_users = int(input("Jumlah Users: "))
    n_libraries = int(input("Jumlah Libraries: "))
    n_categories = int(input("Jumlah Categories: "))
    n_authors = int(input("Jumlah Authors: "))
    n_books = int(input("Jumlah Books: "))
    n_loans = int(input("Jumlah Book Loans: "))
    n_holds = int(input("Jumlah Book Holds: "))

    # Generate all datasets
    users_df = gen.generate_users(n_users)
    libraries_df = gen.generate_libraries(n_libraries)
    categories_df = gen.generate_categories(n_categories)
    authors_df = gen.generate_authors(n_authors)
    books_df = gen.generate_books(n_books, author_count=n_authors)
    book_categories_df = gen.generate_book_categories(n_books, n_categories)
    libraries_books_df = gen.generate_libraries_books(n_books, n_libraries)
    books_loans_df = gen.generate_books_loans(n_loans, n_users, n_books, n_libraries)
    books_holds_df = gen.generate_books_holds(n_holds, n_users, n_books, n_libraries)
    addresses_df = gen.generate_addresses(n_users)

    # Create output directory
    output_dir = "dummy_elibrary"
    os.makedirs(output_dir, exist_ok=True)

    # Save each dataset to a CSV file
    users_df.to_csv(f"{output_dir}/users.csv", index=False)
    addresses_df.to_csv(f"{output_dir}/addresses.csv", index=False)
    libraries_df.to_csv(f"{output_dir}/libraries.csv", index=False)
    categories_df.to_csv(f"{output_dir}/categories.csv", index=False)
    authors_df.to_csv(f"{output_dir}/authors.csv", index=False)
    books_df.to_csv(f"{output_dir}/books.csv", index=False)
    book_categories_df.to_csv(f"{output_dir}/book_categories.csv", index=False)
    libraries_books_df.to_csv(f"{output_dir}/libraries_books.csv", index=False)
    books_loans_df.to_csv(f"{output_dir}/books_loans.csv", index=False)
    books_holds_df.to_csv(f"{output_dir}/books_holds.csv", index=False)

    print(f"\nSemua file dummy berhasil disimpan di folder: {output_dir}/")



save_data_to_csv()