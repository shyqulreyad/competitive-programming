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

// valid parentheses problem solution
// Path: test.php


$parentheses = '()()()()()()'; 

$parentheses = '()()()()(}';

function validParentheses($parentheses) {
    $parentheses = str_split($parentheses);
    $count = count($parentheses);
    $half = $count / 2;
    $open = array_fill(0, $half, '(');
    $close = array_fill(0, $half, ')');
    $valid = array_merge($open, $close);
    $diff = array_diff($valid, $parentheses);
    if (empty($diff)) {
        return true;
    } else {
        return false;
    }
}

var_dump(validParentheses($parentheses));