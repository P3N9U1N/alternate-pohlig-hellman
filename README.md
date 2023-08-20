# An algorithm for solving the discrete logarithm

This repository contains an algorithm for solving the discrete logarithm. It is efficient if the multiplicative order is a smooth number, making it an alternative to the Pohlig-Hellman algorithm. The Pohlig-Hellman algorithm calculates congruences, so that the discrete logarithm can be derived by the Chinese remainder theorem. This algorithm does the same, but does not need the Chinese remainder theorem, making it slightly faster (using a comparable Python implementation).



## Benchmarks

```
richbench ./ --repeat 5 --times 1
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃                                          Benchmark ┃ Min     ┃ Max     ┃ Mean    ┃ Min (+)         ┃ Max (+)         ┃ Mean (+)        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ base 47, mod 10000000000000000000000343, value 191 │ 7.711   │ 8.080   │ 7.895   │ 7.797 (-1.0x)   │ 8.038 (1.0x)    │ 7.901 (-1.0x)   │
│     base 47, mod 1000000000000000000117, value 191 │ 0.007   │ 0.013   │ 0.010   │ 0.006 (1.0x)    │ 0.009 (1.4x)    │ 0.008 (1.2x)    │
│                    base 1669, mod 9439, all values │ 0.016   │ 0.016   │ 0.016   │ 0.016 (-1.0x)   │ 0.016 (1.0x)    │ 0.016 (1.0x)    │
│              base 6, mod 2420352901, value 1111111 │ 0.001   │ 0.001   │ 0.001   │ 0.001 (1.0x)    │ 0.002 (-1.2x)   │ 0.001 (-1.0x)   │
└────────────────────────────────────────────────────┴─────────┴─────────┴─────────┴─────────────────┴─────────────────┴─────────────────┘
```
