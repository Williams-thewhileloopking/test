import csv
import sys
def main():
    try:
        reorder()
    except FileNotFoundError as e:
        sys.exit(f"File could not be found: {e}")
def reorder():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as csv_file, open(output_file, 'w') as new_csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=['first_name', 'last_name', 'house'])
        csv_writer.writeheader()
        next(csv_reader)
        for row in csv_reader:
            name_parts = row[0].split(", ")
            first_name, last_name, house = name_parts[1], name_parts[0], row[-1]
            output_row = {
                'first_name': first_name,
                'last_name': last_name,
                'house': house
            }
            csv_writer.writerow(output_row)
if __name__ == "__main__":
    main()
