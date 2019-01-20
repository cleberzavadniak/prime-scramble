# Mercafácil Challenge: Prime-Scramble

## The challenge

```
 Desafio de criptografia:

Desenvolver um algoritmo em qualquer linguagem de programação que tome como input uma string criptografada e a imprima descriptografada.

Criptografia Prime-Scramble:
O valor ASCII de cada membro da string é somado ao número primo de mesmo índice. Exemplo:

a b c d e f g h i j
+ + + + + + + + + +
2 3 5 7 11 13 17 19 23 29
= = = = = = = = = =
c e h k p s x { # *
limite inferior: VALOR DECIMAL = 33 <=> CARACTERE = !
limite superior: VALOR DECIMAL = 125 <=> CARACTERE = }

Note que caso a soma do caractere com o número primo seja maior do que o limite superior, ele deve começar novamente a partir do limite inferior. Por exemplo:

i(105) + 23 = 128. 128 > 125. criptografia = 33 + (128 - 126) = 35 = #
```

# Notes

## English

Although the challenge itself was written in Portuguese, I'm a firm
believer that we should NEVER code or write documentation (for developers)
in any other language than English if there's not a very strong and valid
reason for that.

Remember: **The Codebase is bigger than any of us**.

We think we are the owners of the code today, but who knows what the
future holds for us? In a time of urgency, maybe The Company will find
that hiring *a small army* of developers from **Belarus** is The Only Way
to save everybody from Bankruptcy, and there won't be a lot of smiles and
happy faces when the new проявитель (developers) team call back in the
middle of the night saying they can't figure out what "números primos"
(*prime numbers* in Portuguese) means.

## Run!

When in doubt, the script `bin/run-complete.sh` should make everything work
most of the times.

You must have permission to use `pip install`, so I recommend you use any
kind of *virtualenv* tool and activate a proper virtual environment.


**This program was only tested using Python 3.6.8!**


## "Barrel Values"

You see, it's perfectly okay to have a superior limit. Life is like that
all the time, huh? "*Mom! I want another pancake!*" / "*You already ate
five. No more pancakes for you!*".


Yeah, I know. Sad.

But we accept that, because life is that way, we soon learn.


But, let's be honest, an **inferior** limit is **ABSOLUT SHIT**. "*But
Mom! I don't want any more pancakes! I'm already full...*" / "*You're not
leaving the table until you ate your fifteen pancakes!*".


Oh, man, that is **awful**!


So, we take that horrendous `33` lower limit **off** for most part of the
party, because, in the end, its only real use is for **offsetting** the
value into the right index of the characters table. That frees us from
filling our code with **PAGES** of hard to understand stupid conditionals
that, in the end, don't even add up too much for the internal logic.

So we un-offset first and offset again later. I call it "Normalization™".


## Prime Numbers

Do you know why are they called "prime"? It's very interesting and most
people (at least in Brazil) has absolutely no idea of the reason. I've
written a brief explanation in Portuguese here:

[O dia que o professor de Matemática admitiu que estava errado
- Porque, afinal, o número 1 não
  é primo](http://cleber.netlify.com/a-vida-de-cléber/o-dia-que-o-professor-de-matematica-admitiu-que-estava-errado)

### About calculating prime numbers

**DON'T calculate prime numbers in your program**. Never. It's plain
stupid. Really.


**I'M TALKING TO YOU! HEY! PUT THE KEYBOARD DOWN, NOW!**


Why would you waste so much energy all over again? Hell, people are
writing "*the first N prime numbers*" tables for CENTURIES now. Just go to
the web and download it in any proper format you want.

In my case, for instance, I used the .txt file from this URL:

http://www.svobodat.com/primes/

Of course I'm not including the entire table, since the task at hand only
needs a very small ammount of them. I'm saving the small table in the
respository, but there's a simple script called
`bin/create-prime-numbers-table.sh` that creates it again if you want to be
sure (?). After [re-]creation, just keep it there.


## Tests

I included the scripts `bin/prepare-for-tests.sh`, that install the required
Python packages using `pip` (if you use some kind of *virtualenv*, be sure
to activate it properly before running the script) and `bin/run-tests.sh`, the
one that actually run the tests.


The current coverage is **100%** and should not drop below this mark, since the
code is **very** simple.


After running the test suite, you will find a HTML report inside the `htmlcov`
directory. Open the `index.html` file in your favorite browser.
