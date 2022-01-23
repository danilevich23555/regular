from function import regular_text, union, mergeDict, remove_recurrence
import os
import csv

if __name__ == '__main__':
    path1 = os.path.join(os.getcwd(), 'out.csv')
    with open("IN.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    a = regular_text(contacts_list)
    b = union(a)
    c = remove_recurrence(b)
    with open(path1, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'))
        for i in range(len(c)):
            writer.writerow((c[i]['lastname'], c[i]['firstname'], c[i]['surname'],
                             c[i]['organization'], c[i]['position'], c[i]['phone'],
                             c[i]['email']))