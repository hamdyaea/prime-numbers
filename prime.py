#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com


def nats(n):
    yield n
    yield from nats(n + 1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


p = sieve(nats(2))

for i in range(100):
    print(next(p))
