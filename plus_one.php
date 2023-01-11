<?php
    $digits =[7,2,8,5,0,9,1,2,9,5,4,9,4,7,0,1,1,1,7,4,0,0,6];
    $length = count($digits);
    $number = implode($digits);
    $final =$number+1;
    $final_ans = str_split($final);
    print_r($number);
