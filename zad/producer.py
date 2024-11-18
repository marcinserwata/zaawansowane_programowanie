import csv
import uuid
import os

JOB_FILE = 'jobs.csv'


def main():
    job_id = str(uuid.uuid4())

    job_data = [job_id, 'pending']

    file_exists = os.path.isfile(JOB_FILE)

    with open(JOB_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['id', 'status'])
        writer.writerow(job_data)

    print(f"Dodano pracę {job_id} ze statusem 'pending'.")


if __name__ == '__main__':
    main()
