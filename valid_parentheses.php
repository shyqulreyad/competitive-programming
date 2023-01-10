<?php
$s = "({[]})";
// $s = "([)]";
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
        for($i=0;$i < $half_len; $i++){
            for($j = $len-1; $j > $half_len ; $j--){
                print('first'.$s[$i]);
                print('second'.$s[$j]);
            }
         
        }
}else{
    $result = false;
    return $result;
}

// print_r($result);

