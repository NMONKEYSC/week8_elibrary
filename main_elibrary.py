import subprocess
import sys
import os

# Path ke folder code_elibrary relatif terhadap lokasi main_elibrary.py
BASE_DIR = os.path.join(os.path.dirname(__file__), 'code_elibrary')

def run_sql_script(filename):
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\n📄 Running SQL script: {filepath}")
    try:
        subprocess.run(['psql', '-U', 'postgres', '-d', 'e_library', '-f', filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running SQL script: {e}")
        sys.exit(1)

def run_shell_script(filename):
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\n💻 Running shell script: {filepath}")
    try:
        subprocess.run(['bash', filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running shell script: {e}")
        sys.exit(1)

def run_python_script(filename):
    filepath = os.path.join(BASE_DIR, filename)
    print(f"\n🐍 Running Python script: {filepath}")
    try:
        subprocess.run([sys.executable, filepath], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Python script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_sql_script('e-library.sql')
    run_python_script('elibrary_dummy_gen.py')
    run_shell_script('insert_data_library.sh')

    print("\n✅ SEMUA BERHASIL DIJALANKAN!")
