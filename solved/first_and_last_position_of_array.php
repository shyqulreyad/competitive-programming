<?php
// $nums = [1];
$nums = [3,3,3];
$target = 3;
$len = count($nums);
$result = [];
for($i=0;$i < $len; $i++){
    if($nums[$i] == $target){
        array_push($result,$i);
    }
}
$res_len =count($result);
if($res_len < 1){
    $result=[-1,-1];
}elseif($res_len == 1){
    $result=[$result[0],$result[0]];
}elseif($res_len > 2){
    $result =[$result[0],$result[$res_len-1]];
}
print_r($result);