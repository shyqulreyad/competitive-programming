<?php
$haystack = "butsadsad";
$needle = "sad";
$ans = strpos($haystack, $needle);
if($ans){
    echo $ans;
} else{
    echo -1;
}