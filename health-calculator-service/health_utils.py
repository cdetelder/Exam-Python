def calculate_bmi(height, weight):
# Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    return weight / (height ** 2)
def calculate_bmr(height, weight, age, gender):
    """
    Calculate BMR using the updated equations.
    Args:
        height (float): Height in cm.
        weight (float): Weight in kg.
        age (int): Age in years.
        gender (str): Gender ('male' or 'female').

    Returns:
        float: BMR rounded to 2 decimal places.
    """
    if age <= 0:
        return "Invalid age"
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
    else:
        return "Invalid gender"

    return round(bmr, 2)



