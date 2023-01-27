<?php
$s = "bcabc";
// explode the string into an array
$s = str_split($s);
$s = array_unique($s);
sort($s);
$s = implode($s);
print_r($s);
// implode 