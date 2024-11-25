import sqlite3
import time
import os

DB_FILE = 'jobs.db'


def main():
    print("Consumer uruchomiony.")

    while True:
        if os.path.isfile(DB_FILE):
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()

            # Fetch the first pending job
            c.execute('''
                SELECT id FROM jobs WHERE status = 'pending' ORDER BY id LIMIT 1
            ''')
            job = c.fetchone()

            if job:
                job_id = job[0]
                print(f"Znaleziono pracę {job_id}. Rozpoczynam wykonywanie.")

                # Update status to 'in_progress'
                c.execute('''
                    UPDATE jobs SET status = 'in_progress' WHERE id = ?
                ''', (job_id,))
                conn.commit()

                conn.close()

                time.sleep(30)  # Simulate processing time

                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()

                # Update status to 'done'
                c.execute('''
                    UPDATE jobs SET status = 'done' WHERE id = ?
                ''', (job_id,))
                conn.commit()
                conn.close()

                print(f"Praca {job_id} została ukończona.")
            else:
                print("Brak prac o statusie 'pending'.")
                conn.close()
        else:
            print("Plik bazy danych nie istnieje.")

        time.sleep(5)


if __name__ == '__main__':
    main()
