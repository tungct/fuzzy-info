from xlttm.fuzzy import fuzzy_variable
from xlttm.rule import read_rule

def check_var_fuzzy_lamp(angle, time, distance):
    var_fuzzy = []
    if fuzzy_variable.distance_near(distance) != 0.0:
        var_fuzzy.append("near")
    if fuzzy_variable.distance_normal(distance) != 0.0:
        var_fuzzy.append("medium")
    if fuzzy_variable.distance_far(distance) != 0.0:
        var_fuzzy.append("far")
    if fuzzy_variable.lamp_more_red(time) != 0.0:
        var_fuzzy.append("more_red")
    if fuzzy_variable.lamp_red(time) != 0.0:
        var_fuzzy.append("red")
    if fuzzy_variable.lamp_yellow(time) != 0.0:
        var_fuzzy.append("yellow")
    if fuzzy_variable.lamp_green(time) != 0.0:
        var_fuzzy.append("green")
    if fuzzy_variable.lamp_more_green(time) != 0.0:
        var_fuzzy.append("more_green")
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

def check_rule_fuzzy_lamp(angle, time, distance):
    rule_use = []
    rule = read_rule.read_impediment_lamp_rule()
    var_fuzzy = check_var_fuzzy_lamp(angle, time, distance)

    for i in range(len(rule)):
        attr1, atrr2, attr3 = 0, 0, 0
        for j in range(len(var_fuzzy)):
            if rule[i][0] == var_fuzzy[j]:
                attr1 = 1
            elif rule[i][1] == var_fuzzy[j]:
                atrr2 = 1
            elif rule[i][2] == var_fuzzy[j]:
                attr3 = 1
            if attr1 == 1 and atrr2 == 1 and attr3 == 1:
                rule_use.append(rule[i])
                break
    return rule_use

def calc_speed_lamp(angle, time, distance):
    rules = check_rule_fuzzy_lamp(angle, time, distance)
    print(rules)
    speed = 0
    # print(rules)
    for i in range(len(rules)):
        if rules[i][0] == 'more_right':
            angle_var = fuzzy_variable.angle_more_right(angle)
        elif rules[i][0] == 'right':
            angle_var = fuzzy_variable.angle_right(angle)
        elif rules[i][0] == 'normal':
            angle_var = fuzzy_variable.angle_normal(angle)
        elif rules[i][0] == 'left':
            angle_var = fuzzy_variable.angle_left(angle)
        elif rules[i][0] == 'more_left':
            angle_var = fuzzy_variable.angle_more_left(angle)

        if rules[i][1] == 'more_red':
            lamp_var = fuzzy_variable.lamp_more_red(time)
        elif rules[i][1] == 'red':
            lamp_var = fuzzy_variable.lamp_red(time)
        elif rules[i][1] == 'yellow':
            lamp_var = fuzzy_variable.lamp_yellow(time)
        elif rules[i][1] == 'green':
            lamp_var = fuzzy_variable.lamp_green(time)
        elif rules[i][1] == 'more_green':
            lamp_var = fuzzy_variable.lamp_more_green(time)

        if rules[i][2] == 'near':
            distance_var = fuzzy_variable.distance_near(distance)
        elif rules[i][2] == 'medium':
            distance_var = fuzzy_variable.distance_normal(distance)
        elif rules[i][2] == 'far':
            distance_var = fuzzy_variable.distance_far(distance)

        if rules[i][3] == 'slow':
            speed_avg = 0.0
        elif rules[i][3] == 'normal':
            speed_avg = 30.0
        elif rules[i][3] == 'fast':
            speed_avg = 65.0
        # print(angle_var, lamp_var, distance_var, speed_avg)

        speed = speed + angle_var * lamp_var * distance_var * speed_avg
    return speed

print(calc_speed_lamp(19,2,20))







