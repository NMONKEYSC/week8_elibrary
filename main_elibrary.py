import subprocess
import sys
import os

# Path to the code_elibrary folder, relative to the main_elibrary.py
BASE_DIR = os.path.join(os.path.dirname(__file__), 'code_elibrary')

def run_sql_script(filename):
    """
    Run an SQL script against the e_library database.

    :param filename: Path to a .sql file, relative to the code_elibrary folder.
    :raises: subprocess.CalledProcessError if the SQL script fails to run.
    """
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\nRunning SQL script: {filepath}")
    try:
        subprocess.run(['psql', '-U', 'postgres', '-d', 'e_library', '-f', filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running SQL script: {e}")
        sys.exit(1)

def run_shell_script(filename):
    """
    Run a shell script.

    :param filename: Path to a .sh file, relative to the code_elibrary folder.
    :raises: subprocess.CalledProcessError if the shell script fails to run.
    """
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\n💻 Running shell script: {filepath}")
    try:
        subprocess.run(['bash', filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running shell script: {e}")
        sys.exit(1)

def run_python_script(filename):
    """
    Run a Python script.

    :param filename: Path to a .py file, relative to the code_elibrary folder.
    :raises: subprocess.CalledProcessError if the Python script fails to run.
    """
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\n🐍 Running Python script: {filepath}")
    try:
        subprocess.run([sys.executable, filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_sql_script('e-library.sql')
    run_python_script('elibrary_dummy_gen.py')
    run_shell_script('insert_data_library.sh')

    print("\nALL DONE!")
