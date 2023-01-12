<?php 
$nums = [3,3];
$target = 6;
$len = count($nums);
for($i = 0; $i<$len; $i++){
    for($j=$i+1; $j <$len; $j++){
        if($nums[$i]+$nums[$j] == $target){
            print_r($result = [$i,$j]);
        }
    }
}