def predict_salary(years_experience: float) -> float:
    base_salary = 30000
    increment = years_experience * 5000
    return base_salary + increment
