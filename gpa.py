# 绩点计算公式
def calculate_gpa_from_grade(grade):
    grade_to_gpa = {
        "A+": 4.00, "A": 3.94, "A-": 3.85,
        "B+": 3.73, "B": 3.55, "B-": 3.32,
        "C+": 3.09, "C": 2.78, "C-": 2.42,
        "D+": 2.08, "D": 1.63, "D-": 1.15,
        "F": 0.00
    }
    return grade_to_gpa.get(grade.upper(), None)

# 主函数
def calculate_gpa(grades, credits):
    if len(grades) != len(credits):
        raise ValueError("等级和学分的列表长度必须一致！")

    total_points = 0  # 总绩点
    total_credits = 0  # 总学分

    for grade, credit in zip(grades, credits):
        gpa = calculate_gpa_from_grade(grade)
        if gpa is None:
            raise ValueError(f"无效的等级：{grade}")
        total_points += gpa * credit
        total_credits += credit

    if total_credits == 0:
        return 0.0  # 防止除以零

    return round(total_points / total_credits, 2)

# 示例数据
grades = ["B-", "B+", "A", "A", "A", "A-", "A-"]
credits = [1,   4,   2,   3,   4,    4,    4]
# 计算 GPA
try:
    gpa = calculate_gpa(grades, credits)
    print(f"总 GPA: {gpa}")
except ValueError as e:
    print(e)

