<?php
// Database connection
$servername = "localhost";
$username = "jjiavunp_Data";
$password = "KwbHTgYtvEZeXbYk4TSz";
$dbname = "jjiavunp_Data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the POST data is set and sanitize it
if (isset($_POST['value1']) && isset($_POST['value2'])) {
    // Ensure that the values are integers (1 or 0)
    $ledStatus1 = (int) $_POST['value1'];
    $ledStatus2 = (int) $_POST['value2'];

    // Prepare and bind SQL query
    $stmt = $conn->prepare("INSERT INTO log (value1, value2) VALUES (?, ?)");
    $stmt->bind_param("ii", $ledStatus1, $ledStatus2);  // "ii" for integer parameters

    // Execute the query
    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
} else {
    echo "Error: Missing data!";
}

// Close connection
$conn->close();
?>
