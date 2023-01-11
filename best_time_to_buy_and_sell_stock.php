<?php
$prices =[7,6,4,3,1];
// $prices =[7,1,5,3,6,4];
$len = count($prices);
$profit_arr = [0];
for($i = 0; $i < $len; $i++){
        for($j= $i+1; $j< $len;$j++){
            if($prices[$i] < $prices[$j]){
                $profit = $prices[$j] - $prices[$i];
                array_push($profit_arr,$profit);
            }
        
        }
        
    }
$result = max($profit_arr);
echo $result;