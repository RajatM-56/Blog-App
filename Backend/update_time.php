<?php
$csvFile = "last_request.csv";
$current_time = microtime(true);

// Check if the CSV file exists
if (file_exists($csvFile) && filesize($csvFile) > 0) {
    $data = file_get_contents($csvFile);
    $parts = explode(",", trim($data));

    if (count($parts) == 2) {
        $online_status = (int) trim($parts[0]);
        $last_time = (float) trim($parts[1]);
    } else {
        $online_status = 0;
        $last_time = 0;
    }
} else {
    $online_status = 0;
    $last_time = 0;
}

// Check if ESP is offline
if ($last_time > 0) {
    $elapsed_time = $current_time - $last_time;
    if ($elapsed_time > 3.0) {
        $online_status = 0;
        file_put_contents($csvFile, "$online_status,0");
    }
}

// Write back to CSV only if offline status needs updating
file_put_contents("log.txt", "$elapsed_time");

// Output for debugging
echo "Updated online status: $online_status";
?>
