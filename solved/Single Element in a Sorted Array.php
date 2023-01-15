<?php
$nums = [1,1,2,3,3,4,4,8,8];
$len = count($nums);
for($i = 0; $i < $len; $i+=2) {
    if($i < $len- 1) {
    $result = $nums[$i+1] - $nums[$i];
        if($result == 0){
            continue;
        }else{
            return $nums[$i];
        }
    }elseif($i === $len - 1) {
        return $nums[$i];
    }
}