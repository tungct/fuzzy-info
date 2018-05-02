from xlttm.fuzzy import fuzzy_variable
from xlttm.rule import read_rule

def check_var_fuzzy_stone(distance, angle):
    var_fuzzy = []
    if fuzzy_variable.distance_near(distance) != 0.0:
        var_fuzzy.append("near")
    if fuzzy_variable.distance_normal(distance) != 0.0:
        var_fuzzy.append("medium")
    if fuzzy_variable.distance_far(distance) != 0.0:
        var_fuzzy.append("far")
    if fuzzy_variable.angle_more_right(angle) != 0.0:
        var_fuzzy.append("more_right")
    if fuzzy_variable.angle_right(angle) != 0.0:
        var_fuzzy.append("right")
    if fuzzy_variable.angle_normal(angle) != 0.0:
        var_fuzzy.append("normal")
    if fuzzy_variable.angle_left(angle) != 0.0:
        var_fuzzy.append("left")
    if fuzzy_variable.angle_more_left(angle) != 0.0:
        var_fuzzy.append("more_left")

    return var_fuzzy

def check_rule_fuzzy_stone(distance, angle):
    rule_use = []
    rule = read_rule.read_impediment_stone_rule()
    var_fuzzy = check_var_fuzzy_stone(distance, angle)

    for i in range(len(rule)):
        attr1, atrr2 = 0, 0
        for j in range(len(var_fuzzy)):
            if rule[i][0] == var_fuzzy[j]:
                attr1 = 1
            elif rule[i][1] == var_fuzzy[j]:
                atrr2 = 1
            if attr1 == 1 and atrr2 == 1:
                rule_use.append(rule[i])
                break
    return rule_use

def calc_speed_stone(distance, angle):
    rules = check_rule_fuzzy_stone(distance, angle)
    print(rules)
    speed = 0
    for i in range(len(rules)):
        if rules[i][1] == 'more_right':
            angle_var = fuzzy_variable.angle_more_right(angle)
        elif rules[i][1] == 'right':
            angle_var = fuzzy_variable.angle_right(angle)
        elif rules[i][1] == 'normal':
            angle_var = fuzzy_variable.angle_normal(angle)
        elif rules[i][1] == 'left':
            angle_var = fuzzy_variable.angle_left(angle)
        elif rules[i][1] == 'more_left':
            angle_var = fuzzy_variable.angle_more_left(angle)

        if rules[i][0] == 'near':
            distance_var = fuzzy_variable.distance_near(distance)
        elif rules[i][0] == 'medium':
            distance_var = fuzzy_variable.distance_normal(distance)
        elif rules[i][0] == 'far':
            distance_var = fuzzy_variable.distance_far(distance)

        if rules[i][2] == 'slow':
            speed_avg = 0.0
        elif rules[i][2] == 'normal':
            speed_avg = 30.0
        elif rules[i][2] == 'fast':
            speed_avg = 65.0
        # print(angle_var, lamp_var, distance_var, speed_avg)

        speed = speed + angle_var  * distance_var * speed_avg
    return speed

print(calc_speed_stone(15,55))







