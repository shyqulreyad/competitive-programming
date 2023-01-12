<?php
// $colors =[9,9,9,18,9,9,9,9,9,18];
$colors =[1,8,3,8,3];
$len = count($colors);
$color_arr = [1];
for($i=0; $i <$len; $i++){
    $counter = 0;
    $main = 0;
    for($j=$i+1;$j < $len; $j++){
        $counter++;
        if($colors[$i] != $colors[$j]){
            $main = $counter;
        }
    }
    array_push($color_arr,$main);
}
$result = max($color_arr);
echo $result;