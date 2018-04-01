import json
import csv


def main():
    input_data_path = 'data/resale-flat-prices-based-on-approval-date-1990-1999.csv'
    output_data_path = 'data/addr-age4.csv'
    title_new = ["addr", "lease_commence_date"]
    with open(input_data_path) as input_csv_file:
        reader = csv.DictReader(input_csv_file)
        with open(output_data_path, 'w') as output_csv_file:
            writer = csv.writer(output_csv_file)
            writer.writerow(title_new)
            seen = set()
            for row in reader:
                if row['street_name'] in seen:
                    continue
                seen.add(row['street_name'])
                row_new = [
                    row['street_name'],
                    row['lease_commence_date']
                ]
                writer.writerow(row_new)


if __name__ == '__main__':
    main()