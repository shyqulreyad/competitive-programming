<?php
$x = 121;
// check if the number is palindrome
function isPalindrome($x) {
    $x = (string)$x;
    $len = strlen($x);
    $result = [];
    for($i = $len - 1; $i >= 0; $i--) {
        array_push($result, $x[$i]);
    }
    $result = implode($result);
    if($x == $result) {
        echo 'true';
    }else{
        echo 'false';
    }
}
isPalindrome($x);