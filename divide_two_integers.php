<?php
$dividend = -2147483648;
$divisor = -1;
 $change = false;
                if($divisor < 0 && $dividend < 0){
                    $divisor = abs($divisor); 
                    $dividend = abs($dividend);
                    $change = false;
                }elseif($divisor < 0){
                    $divisor = abs($divisor); 
                    $change = true;
                }elseif($dividend < 0){
                    $dividend = abs($dividend);
                    $change = true;
                }
                   $counter =0;
                    if($dividend == 0){
                        $counter = 0;
                        echo $counter;
                    }
                    if($divisor == 1){
                        $counter = $dividend;
                        echo $counter;
                    }
                for($i=1; $i >=1; $i++){
                
                    if($dividend >= $divisor){
                        $counter+=1;
                        $dividend -= $divisor;
                    }else{
                        break;
                    }
                }

                if($change){
                    $result = -$counter;
                    echo $result;
                }else{
                    echo $counter;
                }