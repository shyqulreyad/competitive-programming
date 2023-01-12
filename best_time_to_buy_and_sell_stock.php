<?php
// $prices =[7,6,4,3,1];
$prices =[7,1,5,4];
// $sorted = $prices;
// sort($sorted);
// print_r($sorted);
// print_r($prices);
$len = count($prices);
$profit_arr = [0];
$profit = 0;
$break = max($prices) - min($prices);
for($i = 0; $i < $len; $i++){
        
    }
$result = max($profit_arr); //4
echo $result;
// $len = count($prices);
// $profit_arr = [0];
// $profit = 0;
// $break = max($prices) - min($prices);
// for($i = 0; $i < $len; $i++){
//         for($j= $i+1; $j< $len;$j++){
//             if($prices[$i] < $prices[$j]){
//                 $profit = $prices[$j] - $prices[$i];
//                 array_push($profit_arr,$profit);
//             }
//             if($profit == $break){
//                 break;
//             }
//         }
        
//     }
// $result = max($profit_arr); //4
// echo $result;