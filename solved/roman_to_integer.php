<?php
 $s = "MCMXCIV";
    $num = 0;
    $a = str_split($s);
    $len = count($a);
    for($i = 0; $i < $len; $i++){
        if($a[$i] == 'I'){
            if($a[$i].$a[$i+1] == 'IX'){
                $num += 9;
                $i++;
            }elseif($a[$i].$a[$i+1] == 'IV'){
                $num += 4;
                $i++;
            }else{
                $num += 1;
            }
        }elseif($a[$i] == 'V'){
            $num += 5;
        }elseif($a[$i] == 'X'){
            if($a[$i].$a[$i+1] == 'XC'){
                $num += 90;
                $i++;
            }elseif($a[$i].$a[$i+1] == 'XL'){
                $num += 40;
                $i++;
            }else{
                $num += 10;
            }
        }elseif($a[$i] == 'L'){
            $num += 50;
        }elseif($a[$i] == 'C'){
            if($a[$i].$a[$i+1] == 'CM'){
                $num += 900;
                $i++;
            }elseif($a[$i].$a[$i+1] == 'CD'){
                $num += 400;
                $i++;
            }else{
                $num += 100;
            }
        }elseif($a[$i] == 'D'){
            $num += 500;
        }elseif($a[$i] == 'M'){
            $num += 1000;
        }
    }
     echo $num;
?>