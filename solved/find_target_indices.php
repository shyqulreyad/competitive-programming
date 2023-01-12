<?php
$nums = [1,2,5,2,3];
sort($nums);
print_r($nums);
$target = 3;
$len = count($nums);
$result = [];
for($i=0;$i < $len; $i++){
    if($nums[$i] == $target){
        array_push($result,$i);
    }
}
print_r($result);