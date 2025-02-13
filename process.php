<?php
    $a = escapeshellarg($_POST['a']);
    $b = escapeshellarg($_POST['b']);
    $command = escapeshellcmd("python3 process.py $a $b");
    $output = shell_exec($command);

    echo "<h1>Assignment 5:</h1>";
    echo "<h2>Python Script Result</h2>";
    echo "<div>$output</div>";
?>