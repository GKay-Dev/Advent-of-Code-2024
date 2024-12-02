with open("input.txt", "r") as f:
    reports = [list(map(int, l.split())) for l in f]

def is_order_safe(l: list) -> bool:
    return sorted(l) == l or sorted(l, reverse=True) == l

def is_diff_safe(l: list) -> bool:
    return all(1 <= abs(i - j) <= 3 for i, j in zip(l, l[1:]))

def is_report_safe(l: list) -> bool:
    return is_order_safe(l) and is_diff_safe(l)

safe_reports = 0
modified_safe_reports = 0

for r in reports:
    # Part One
    if is_report_safe(r):
        safe_reports += 1
    
    # Part Two
    else:
        for i in range(len(r)):
            new_r = r[:i] + r[i+1:]
            if is_report_safe(new_r):
                modified_safe_reports += 1
                break

print('No of Safe Reports:', safe_reports)
print('No of Safe Reports using Problem Dampener:', safe_reports + modified_safe_reports)
