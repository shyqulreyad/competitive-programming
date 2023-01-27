<?php
$s = "the   sky is   blue";
$s = explode(" ", $s);
$length = count($s);
$result = "";
$j = 1;
for($i=$length-1; $i >= 0; $i--){

    if($s[$i] != ""){
        if ($j == 1){
            $result .= $s[$i];
            $j++;
        }else{
            $result .= " ".$s[$i];
        }
    }
}
print_r($result);