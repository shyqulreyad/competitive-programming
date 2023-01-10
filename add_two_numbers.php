<?php
function custom_reverse($arr) {
    $len = count($arr);
    $result = [];
    for($i = $len - 1; $i >= 0; $i--) {
        array_push($result, $arr[$i]);
    }
    return $result;
}
$l1 = [9,9,9,9,9,9,9];
$l2 = [9,9,9,9];
$l1 = custom_reverse($l1);
$l2 = array_reverse($l2);
$num_one =implode($l1);
$num_two =implode($l2);
$result = $num_one + $num_two;
$result = str_split($result);
$result = array_reverse($result);
print_r($result);

?>