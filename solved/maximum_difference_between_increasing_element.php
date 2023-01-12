<?php
$nums =[7,1,5,4];
$len = count($nums);
$profit_arr = [-1];
$profit = 0;
$break = max($nums) - min($nums);
for($i = 0; $i < $len; $i++){
        for($j= $i+1; $j< $len;$j++){
            if($nums[$i] < $nums[$j]){
                $profit = $nums[$j] - $nums[$i];
                array_push($profit_arr,$profit);
            }
            if($profit == $break){
                break;
            }
        }
        
    }
$result = max($profit_arr);
echo $result;
?>