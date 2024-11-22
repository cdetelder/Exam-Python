// Function to calculate BMI when the form is submitted
function calculateBMI() {
    // Get the height and weight values from the input fields
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);

    // Check if the inputs are valid
    if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
        alert("Please enter valid height and weight values.");
        return;
    }

    // Prepare data to send to the Flask server
    const data = {
        height: height,
        weight: weight
    };

    // Make a POST request to the Flask API for BMI calculation
    fetch('http://localhost:5000/bmi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the BMI result
        document.getElementById('bmi-result').textContent = `BMI: ${data.bmi}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while calculating BMI.");
    });
}

// Function to calculate BMR when the form is submitted
function calculateBMR() {
    // Get the values from the input fields
    const height = parseFloat(document.getElementById('height-bmr').value);
    const weight = parseFloat(document.getElementById('weight-bmr').value);
    const age = parseInt(document.getElementById('age').value);
    const gender = document.getElementById('gender').value;

    // Check if the inputs are valid
    if (isNaN(height) || isNaN(weight) || isNaN(age) || height <= 0 || weight <= 0 || age <= 0 || (gender !== 'male' && gender !== 'female')) {
        alert("Please enter valid height, weight, age, and gender.");
        return;
    }

    // Prepare data to send to the Flask server
    const data = {
        height: height,
        weight: weight,
        age: age,
        gender: gender
    };

    // Make a POST request to the Flask API for BMR calculation
    fetch('http://localhost:5000/bmr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the BMR result
        document.getElementById('bmr-result').textContent = `BMR: ${data.bmr}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while calculating BMR.");
    });
}

// Add event listeners to the forms
document.getElementById('bmi-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calculateBMI();
});

document.getElementById('bmr-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calculateBMR();
});

// Function to calculate BMI when the form is submitted
function calculateBMI() {
    // Get the height and weight values from the input fields
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);

    // Check if the inputs are valid
    if (isNaN(height) || isNaN(weight) || height <= 0 || weight <= 0) {
        alert("Please enter valid height and weight values.");
        return;
    }

    // Prepare data to send to the Flask server
    const data = {
        height: height,
        weight: weight
    };

    // Make a POST request to the Flask API for BMI calculation
    fetch('http://localhost:5000/bmi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the BMI result
        document.getElementById('bmi-result').textContent = `BMI: ${data.bmi}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while calculating BMI.");
    });
}

// Function to calculate BMR when the form is submitted
function calculateBMR() {
    // Get the values from the input fields
    const height = parseFloat(document.getElementById('height-bmr').value);
    const weight = parseFloat(document.getElementById('weight-bmr').value);
    const age = parseInt(document.getElementById('age').value);
    const gender = document.getElementById('gender').value;

    // Check if the inputs are valid
    if (isNaN(height) || isNaN(weight) || isNaN(age) || height <= 0 || weight <= 0 || age <= 0 || (gender !== 'male' && gender !== 'female')) {
        alert("Please enter valid height, weight, age, and gender.");
        return;
    }

    // Prepare data to send to the Flask server
    const data = {
        height: height,
        weight: weight,
        age: age,
        gender: gender
    };

    // Make a POST request to the Flask API for BMR calculation
    fetch('http://localhost:5000/bmr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the BMR result
        document.getElementById('bmr-result').textContent = `BMR: ${data.bmr}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while calculating BMR.");
    });
}

// Add event listeners to the forms
document.getElementById('bmi-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calculateBMI();
});

document.getElementById('bmr-form').addEventListener('submit', function(event) {
    event.preventDefault();
    calculateBMR();
});

