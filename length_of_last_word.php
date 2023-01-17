<?php
$s =  "   fly me   to   the moon  ";
   $s = trim($s);
   $s = explode(" ", $s);
   $s = end($s);
   $s = strlen($s);
   echo $s;