<?php

class CardDeck implements IteratorAggregate {
    private $suits = ['♠', '♥', '♦', '♣'];
    private $court = ['J', 'Q', 'K', 'A'];

    public function getIterator() {
        return new ArrayIterator($this->generateDeck());
    }

    private function generateDeck() {
        $deck = [];
        foreach ($this->suits as $suit) {
            for ($i = 2; $i <= 10; $i++) {
                $deck[] = $suit . $i;
            }
            foreach ($this->court as $courtCard) {
                $deck[] = $suit . $courtCard;
            }
        }
        return $deck;
    }
}

$cardDeck = new CardDeck();
print_r($cardDeck);

$num = [1,2,0,0];
$k = 34;
$sum = $k + implode($num);
print_r(str_split($sum));
// create a recursive function
function sum($num, $k) {
    $sum = $k + implode($num);
    $sum = str_split($sum);
    if (in_array(0, $sum)) {
        $sum = array_diff($sum, [0]);
        $sum = array_values($sum);
        return sum($sum, 0);
    } else {
        return $sum;
    }
}
print_r(sum($num, $k));
function sum2($num, $k) {
    $sum = $k + implode($num);
    $sum = str_split($sum);
    if (in_array(0, $sum)) {
        $sum = array_diff($sum, [0]);
        $sum = array_values($sum);
        return sum($sum, 0);
    } else {
        return $sum;
    }
}
print_r(sum2($num, $k));
