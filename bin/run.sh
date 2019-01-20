#!/bin/sh

set -e  # Quit on any error

EMAIL='cqil}##$E3.79>AuKEXMMXW_mt8{u'
SUBJECT='ohhvy$&t.!/->13>?COV'
export PYTHONPATH=.

if [[ ! -f assets/prime-numbers.txt ]];then
    [[ -d assets ]] || mkdir assets
    echo "Downloading prime numbers table." >&2
    bin/create-prime-numbers-table.sh > /dev/null 2>&1
    echo "Done" >&2
    echo >&2
fi

echo -n "E-mail: $EMAIL -> "
python3 -m mercafacil.prime_scramble "$EMAIL"

echo -n "Subject: $SUBJECT -> "
python3 -m mercafacil.prime_scramble "$SUBJECT"
