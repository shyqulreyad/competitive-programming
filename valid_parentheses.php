<?php
// $s = "({[]})";
$s = "([)]";
// $s = "(){}[]";
$s = str_split($s);
$len = count($s);  //4
$result = true;
if($s[0] ==')' || $s[0] == '}' || $s[0] == ']'){
    $result = false;
    return $result;
}
if($s[$len - 1] == '(' || $s[$len -1] == '[' || $s[$len -1] == '{'){
    $result = false;
    return $result;
}
if($len % 2 == 0){
    $half_len = $len / 2;
        $j = $len-1;
        $array_one = [];
        $array_two = [];
        $array_three = [];
        for($i = 0; $i < $len; $i++){
            if($s[$i] == '(' || $s[$i] == ')'){
                array_push($array_one,$i);
            }
            if($s[$i] == '{' || $s[$i] == '}'){
                array_push($array_two,$i);
            }
            if($s[$i] == '[' || $s[$i] == ']'){
                array_push($array_three,$i);
            }
        }
        print_r($array_one);
        print_r($array_two);
        print_r($array_three);
        // for($i=0;$i < $half_len; $i++){
        //         $ascii = ord($s[$i]);
        //         $ascii2 = ord($s[$j]);
        //         echo $ascii . ' ' . $ascii2 . '';
        //         if($ascii != $ascii2 - 1 && $ascii != $ascii2 - 2){
        //                 $result = 'false';
        //                 echo $result;
        //             }
        //         $j--;     
        // }
}else{
    $result = false;
    return $result;
}
return $result;


