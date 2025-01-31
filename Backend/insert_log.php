<?php
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

// Check if 'value1' and 'value2' are set in POST request
if (isset($_POST['value1']) && isset($_POST['value2'])) {
    $value1 = intval($_POST['value1']); // Ensure value1 is an integer
    $value2 = intval($_POST['value2']); // Ensure value2 is an integer

    // Insert into the table
    $sql = "INSERT INTO log (value1, value2) VALUES ('$value1', '$value2')";

    if ($conn->query($sql) === TRUE) {
        echo "Data inserted successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    echo "Values not provided in POST request";
}

$conn->close();
?>
