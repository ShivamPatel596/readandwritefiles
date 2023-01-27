import csv


def main():
    infile = open("sales.csv", "r")
    outfile = open("salesreport.csv", "w")

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        cust_list = [row[0], row[3]]
        writer.writerow(cust_list)


if __name__ == "__main__":
    main()
