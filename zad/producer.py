import sqlite3
import uuid

DB_FILE = 'jobs.db'


def main():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            status TEXT
        )
    ''')

    job_id = str(uuid.uuid4())
    job_status = 'pending'

    # Insert new job
    c.execute('''
        INSERT INTO jobs (id, status) VALUES (?, ?)
    ''', (job_id, job_status))

    conn.commit()
    conn.close()

    print(f"Dodano pracę {job_id} ze statusem '{job_status}'.")


if __name__ == '__main__':
    main()
