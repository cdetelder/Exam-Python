def calculate_bmi(height, weight):
# Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    if age < 0:
        return "Invalid age"
    
    if gender.lower() == 'male':
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
    elif gender.lower() == 'female':
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
    else:
        return "Invalid gender"

