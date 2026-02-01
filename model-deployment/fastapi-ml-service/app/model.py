def predict_salary(years_experience: float) -> float:
    base_salary = 30000
    increment_per_year = 5000
    return base_salary + (years_experience * increment_per_year)
