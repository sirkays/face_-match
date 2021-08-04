<?php
$web_link = "http://localhost/python_api/evaluate_model.py?name=";
$web_data = file_get_contents($web_link);

echo "<br><br>".$web_data;
?>