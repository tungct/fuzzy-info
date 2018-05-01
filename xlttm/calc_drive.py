from xlttm.fuzzy import fuzzy_variable
from xlttm.rule import read_rule

def check_var_fuzzy(angle):
    var_fuzzy = []

    if fuzzy_variable.angle_left(angle) != 0.0:
        var_fuzzy.append("left")
    if fuzzy_variable.angle_more_left(angle) != 0.0:
        var_fuzzy.append("more_left")
    if fuzzy_variable.angle_normal(angle) != 0.0:
        var_fuzzy.append("normal")
    if fuzzy_variable.angle_right(angle) != 0.0:
        var_fuzzy.append("right")
    if fuzzy_variable.angle_more_right(angle) != 0.0:
        var_fuzzy.append("more_right")

    return var_fuzzy

def check_rule_fuzzy(angle):
    rule_use = []
    rule = read_rule.read_impediment_angle_rule()
    var_fuzzy = check_var_fuzzy(angle)
    for i in range(len(var_fuzzy)):
        for j in range(len(rule)):
            if var_fuzzy[i] == rule[j][0]:
                rule_use.append(rule[j])
    return rule_use

def calc_drive(angle):
    rules = check_rule_fuzzy(angle)
    drive = 0
    for i in range(len(rules)):
        if rules[i][0] == "left":
            temp = fuzzy_variable.angle_left(angle)
            angle_avg = -22.5
            drive = drive + temp * angle_avg
        elif rules[i][0] == "right":
            temp = fuzzy_variable.angle_right(angle)
            angle_avg = 22.5
            drive = drive + temp * angle_avg
        elif rules[i][0] == "more_left":
            temp = fuzzy_variable.angle_more_left(angle)
            angle_avg = -45
            drive = drive + temp * angle_avg
        elif rules[i][0] == "more_right":
            temp = fuzzy_variable.angle_more_right(angle)
            angle_avg = 45
            drive = drive + temp * angle_avg
        elif rules[i][0] == "normal":
            temp = fuzzy_variable.angle_normal(angle)
            angle_avg = 0
            drive = drive + temp * angle_avg
    return drive










