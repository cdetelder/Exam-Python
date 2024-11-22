def calculate_bmi(height, weight):
# Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    if age <= 0:
        return "Invalid age"
    
    # Mifflin-St Jeor Equation for BMR
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid gender"

    # Round to 2 decimal places
    return round(bmr, 2)

