import csv
import time
import os

JOB_FILE = 'jobs.csv'


def main():
    print("Consumer uruchomiony.")
    while True:
        if os.path.isfile(JOB_FILE):
            with open(JOB_FILE, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

            header = rows[0]
            data_rows = rows[1:]

            pending_jobs = [row for row in data_rows if row[1] == 'pending']

            if pending_jobs:
                job = pending_jobs[0]
                job_id = job[0]
                print(f"Znaleziono pracę {job_id}. Rozpoczynam wykonywanie.")

                for row in data_rows:
                    if row[0] == job_id:
                        row[1] = 'in_progress'
                        break

                with open(JOB_FILE, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(header)
                    writer.writerows(data_rows)

                time.sleep(30)

                with open(JOB_FILE, 'r', newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    rows = list(reader)

                header = rows[0]
                data_rows = rows[1:]

                for row in data_rows:
                    if row[0] == job_id:
                        row[1] = 'done'
                        break

                with open(JOB_FILE, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(header)
                    writer.writerows(data_rows)

                print(f"Praca {job_id} została ukończona.")
            else:
                print("Brak prac o statusie 'pending'.")
        else:
            print("Plik z pracami nie istnieje.")

        time.sleep(5)


if __name__ == '__main__':
    main()
