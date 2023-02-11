<?php
$s = "bcabc";
// explode the string into an array
$s = str_split($s);
$s = array_unique($s);
print_r($s);