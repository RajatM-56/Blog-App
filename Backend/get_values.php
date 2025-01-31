<?php
// MySQL database connection details
$servername = "localhost";
$username = "jjiavunp_Data";
$password = "KwbHTgYtvEZeXbYk4TSz";
$dbname = "jjiavunp_Data";

// Create connection to MySQL
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Define default values
$value1 = 0;
$value2 = 0;

// Query to fetch value1 and value2
$sql = "SELECT value1, value2 FROM log ORDER BY id DESC LIMIT 1";  // Replace 'log' with your actual table name
$result = $conn->query($sql);

// Check if any row is returned
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $value1 = $row["value1"];
    $value2 = $row["value2"];
}

// Set content type to JSON
header('Content-Type: application/json');

$current_time = microtime(true);
file_put_contents("last_request.csv", "1,$current_time");

// Return the values as JSON
echo json_encode(array("value1" => $value1, "value2" => $value2));

// Close the connection
$conn->close();
?>
