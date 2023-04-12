<?php
$num = [1,2,0,0];
$k = 34;
$sum = $k + implode($num);
print_r(str_split($sum));
// create a recursive function
function sum($num, $k) {
    $sum = $k + implode($num);
    $sum = str_split($sum);
    if (in_array(0, $sum)) {
        $sum = array_diff($sum, [0]);
        $sum = array_values($sum);
        return sum($sum, 0);
    } else {
        return $sum;
    }
}
print_r(sum($num, $k));

// create recursive funtion using dp (dynamic programming)
function sum_dp($num, $k) {
    $sum = $k + implode($num);
    $sum = str_split($sum);
    if (in_array(0, $sum)) {
        $sum = array_diff($sum, [0]);
        $sum = array_values($sum);
        return sum_dp($sum, 0);
    } else {
        return $sum;
    }
}
print_r(sum_dp($num, $k));