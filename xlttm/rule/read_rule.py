import xlrd

def read_impediment_angle_rule():
    impediment_rule = []
    with xlrd.open_workbook('./rule/rule.xlsx') as book:
        sheet = book.sheet_by_index(0)

        distance = [x for x in sheet.col_values(1)]
        angle = [y for y in sheet.col_values(2)]

        for i in range(len(distance)):
            impediment_rule.append((distance[i].strip(), angle[i].strip()))
    return impediment_rule

def read_impediment_lamp_rule():
    impediment_rule = []
    with xlrd.open_workbook('./rule/rule_lamp.xlsx') as book:
        sheet = book.sheet_by_index(0)

        angle = [x for x in sheet.col_values(1)]
        lamp = [y for y in sheet.col_values(2)]
        distance = [z for z in sheet.col_values(3)]
        speed = [t for t in sheet.col_values(4)]

        for i in range(len(angle)):
            impediment_rule.append((angle[i].strip(), lamp[i].strip(), distance[i].strip(), speed[i].strip()))
    return impediment_rule

