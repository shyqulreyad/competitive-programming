<?php 
$nums = [1,3,5,6];
$target = 5;
$len = count($nums);
for($i=0;$i < $len; $i++){
    if($nums[$i] >= $target){
        echo $i;
    }
}
// echo $len;