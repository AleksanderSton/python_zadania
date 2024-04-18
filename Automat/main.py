def set_rule(rule):
    return {
        "***": '*' if rule[0] == '1' else '_',
        "**_": '*' if rule[1] == '1' else '_',
        "*_*": '*' if rule[2] == '1' else '_',
        "*__": '*' if rule[3] == '1' else '_',
        "_**": '*' if rule[4] == '1' else '_',
        "_*_": '*' if rule[5] == '1' else '_',
        "__*": '*' if rule[6] == '1' else '_',
        "___": '*' if rule[7] == '1' else '_'
    }


def triangle(n):
    return "_" * (n // 2) + "*" + "_" * (n // 2)


def new_automat(rule, n):
    rule_dict = set_rule(rule)
    return {pattern: rule_dict[pattern] for pattern in rule_dict}, triangle(n)


def run_automat(automat, k):
    cells = automat[1]
    for _ in range(k):
        print(cells)
        next_cells = ""
        for i in range(len(cells)):
            left = cells[i - 1]
            center = cells[i]
            right = cells[(i + 1) % len(cells)]
            pattern = left + center + right
            next_cells += automat[0].get(pattern, "_")
        cells = next_cells


rule = '01011010'
n = 78
k = 90

automat = new_automat(rule, n)
run_automat(automat, k)