<?php
    function intToRoman($num) {
        $roman = "";
$roman_number = array(
  "M" => 1000,
    "CM" => 900,
    "D" => 500,
    "CD" => 400,
    "C" => 100,
    "XC" => 90,
    "L" => 50,
    "XL" => 40,
    "X" => 10,
    "IX" => 9,
    "V" => 5,
    "IV" => 4,
    "I" => 1
);
foreach($roman_number as $key => $value){
    $matches = intval($num / $value);
    $roman .= str_repeat($key, $matches);
    $num = $num % $value;
}


return $roman;
}
?>