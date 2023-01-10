<?php
$s = "{[]}";
// sort($s);
// $s = "([)]";
$s = str_split($s);
$len = count($s);
$result = true;
for($i=0;$i < $len; $i+=2){
    if($s[$i] == '(' && $s[$i+1] != ')'){
        if($s[$i+2] !== ')'){
            $result = false;
        }
        if($s[$i+3] != ')'){
            $result = false;
        }
        $result = false;
    }elseif($s[$i] == ')'){
        $result = false;
    }elseif($s[$i] == '{' && $s[$i+1] != '}'){
        if($s[$i+2] !== '}'){
            $result = false;
        }
        if($s[$i+3] != '}'){
            $result = false;
        }
        $result = false;
    }elseif($s[$i] == '}'){
        $result = false;
    }elseif($s[$i] == '[' && $s[$i+1] != ']'){
        if($s[$i+2] !== ']'){
            $result = false;
        }
        if($s[$i+3] != ']'){
            $result = false;
        }
        $result = false;
    }elseif($s[$i] == ']'){
        $result = false;
    }
}
print_r($result);