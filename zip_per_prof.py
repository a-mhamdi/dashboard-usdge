#!/home/mhamdi/work/dashboard/.venv/bin/python3

import sys

import json
import zipfile

from students_per_jury import find_documents_by_data

# Call the function
stage = sys.argv[1] # "perf"
date = sys.argv[2]  # "07-02-2025"  # Submission date (format: dd-mm-yyyy)
nature = "initiation" if stage == "init" else "perfectionnement"
subject = "Rapports de stage" + ' [' + nature.upper() + ']'

with open('/home/mhamdi/work/dashboard/dept-ge.teachers.json', 'r') as file:
    enseignants = json.load(file)
    for person in enseignants:
        enseignant = person["name"]
        email = person["email"]
        print(f"Processing {enseignant} ({email})...")

        try:
            rapports = find_documents_by_data(stage, date, enseignant)
            print(f"Found {len(rapports)} documents for {enseignant}")

            if not rapports:
                print(f"No documents found for {enseignant}")
                continue

            with zipfile.ZipFile("/home/mhamdi/Desktop/RAPPORTS/" + enseignant + ".zip", "w", zipfile.ZIP_DEFLATED) as zip_ref:
                for rapport in rapports:
                    pdf_name = rapport + ".pdf"
                    path_to_pdf = "/var/isetbz/uploads/" + \
                        nature + "/" + pdf_name
                    zip_ref.write(path_to_pdf, arcname=pdf_name)

        except Exception as e:
            print(e)
