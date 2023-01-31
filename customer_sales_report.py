import csv


def main():
    infile = open("sales.csv", "r")
    outfile = open("salesreport.csv", "w")

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)

    myDict = {}
    for row in reader:
        if int(row[0]) not in myDict:
            myDict[int(row[0])] = float(row[3]) + float(row[4]) + float(row[5])
        else:
            myDict[int(row[0])] += float(row[3]) + float(row[4]) + float(row[5])

    header = ["Customer | Total"]
    writer.writerow(header)

    for k, v in myDict.items():
        custList = [k, "{:.2f}".format(v)]
        writer.writerow(custList)

    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
