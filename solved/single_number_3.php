<?php
$nums = [1,1,2,2,3,4,4,5,5,9];
$single_number = [];
sort($nums);
$len = count($nums);
for($i = 0; $i < $len; $i+=2) {
    if($i < $len- 1) {
       $result = $nums[$i+1] - $nums[$i];
        if($result == 0){
            continue;
        }else{
            array_push($single_number, $nums[$i]);
            $i-=1;
        }
    }elseif($i === $len - 1) {
         array_push($single_number, $nums[$i]);
    }
}
return $single_number;