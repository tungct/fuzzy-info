import xlrd

def read_impediment_rule():
    impediment_rule = []
    with xlrd.open_workbook('./rule/rule.xlsx') as book:
        sheet = book.sheet_by_index(0)

        distance = [x for x in sheet.col_values(1)]
        angle = [y for y in sheet.col_values(2)]

        for i in range(len(distance)):
            impediment_rule.append((distance[i].strip(), angle[i].strip()))
    return impediment_rule
