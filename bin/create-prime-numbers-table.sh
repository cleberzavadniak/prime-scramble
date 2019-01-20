#!/bin/sh

URL='http://www.svobodat.com/primes/PRIMES1C.TXT?attredirects=0&d=1'
LIMIT=$(( 125 - 33 ))

wget "$URL" -O - | sed 's: :\n:g' | head -$LIMIT > assets/prime-numbers.txt
