<?php
$servername = "localhost";
$username = "jjiavunp_Data";
$password = "KwbHTgYtvEZeXbYk4TSz";
$dbname = "jjiavunp_Data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die(json_encode(["success" => false, "error" => "Connection failed"]));
}

// Query to fetch the latest values for value1 and value2
$sql = "SELECT value1, value2 FROM log ORDER BY id DESC LIMIT 1"; // Modify table name if needed
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo json_encode(["success" => true, "value1" => $row["value1"], "value2" => $row["value2"]]);
} else {
    echo json_encode(["success" => false, "error" => "No data found"]);
}

$conn->close();
?>
