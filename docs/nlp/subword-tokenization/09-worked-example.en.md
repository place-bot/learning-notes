# Complete hand calculation: BPE and WordPiece

## 1. Small corpus

Use five words with frequency numbers:

|word|Frequency|
|---|---:|
| `hug` | 10 |
| `pug` | 5 |
| `pun` | 12 |
| `bun` | 4 |
| `hugs` | 5 |

In order to highlight the merging standards, the suffix token is not added here for the time being.

## 2. BPE initialization

```text
hug  ×10 → h u g
pug  × 5 → p u g
pun  ×12 → p u n
bun  × 4 → b u n
hugs × 5 → h u g s
```

Adjacent pair frequency:

| Pair |Calculate|Frequency|
|---|---|---:|
| `(h,u)` | 10 + 5 | 15 |
| `(p,u)` | 5 + 12 | 17 |
| `(b,u)` | 4 | 4 |
| `(u,g)` | 10 + 5 + 5 | 20 |
| `(u,n)` | 12 + 4 | 16 |
| `(g,s)` | 5 | 5 |

The highest frequency pair is `(u,g)`, in the first round:

```text
u + g → ug
```

New split:

```text
h ug   ×10
p ug   × 5
p u n  ×12
b u n  × 4
h ug s × 5
```

## 3. BPE Round 2

Main pair frequency:

| Pair |Frequency|
|---|---:|
| `(h,ug)` | 15 |
| `(p,ug)` | 5 |
| `(p,u)` | 12 |
| `(b,u)` | 4 |
| `(u,n)` | 16 |
| `(ug,s)` | 5 |

The highest is `(u,n)`:

```text
u + n → un
```

Get:

```text
h ug   ×10
p ug   × 5
p un   ×12
b un   × 4
h ug s × 5
```

## 4. BPE Round 3

The frequency of `(h,ug)` is 15, which is currently the highest:

```text
h + ug → hug
```

Get:

```text
hug    ×10
p ug   × 5
p un   ×12
b un   × 4
hug s  × 5
```

The first three merge rules are:

```text
rank 0: u g
rank 1: u n
rank 2: h ug
```

## 5. Use this set of BPE encoding `hugs`

```text
h u g s
→ h ug s # use rank 0
→ hug s # use rank 2
```

If `hug + s` has not been learned, the final output is `hug | s`.

## 6. WordPiece initialization

Use `##` to mark non-initial positions:

```text
h ##u ##g       ×10
p ##u ##g       × 5
p ##u ##n       ×12
b ##u ##n       × 4
h ##u ##g ##s   × 5
```

Frequency of each unit:

|unit|Frequency|
|---|---:|
| `h` | 15 |
| `p` | 17 |
| `b` | 4 |
| `##u` | 36 |
| `##g` | 20 |
| `##n` | 16 |
| `##s` | 5 |

## 7. Calculate common WordPiece Score

For `(##u, ##g)`:

\[
\frac{20}{36\times20}=\frac{1}{36}.
\]

For `(h, ##u)`:

\[
\frac{15}{15\times36}=\frac{1}{36}.
\]

For `(##g, ##s)`:

\[
\frac{5}{20\times5}=\frac{1}{20}.
\]

Although `(##g, ##s)` only appears 5 times, it has the highest score, so the common WordPiece trainer refactoring will be merged first:

```text
##g + ##s → ##gs
```

In the first round, BPE selected `u+g` with an absolute frequency of 20, and the two have different merge histories.

## 8. Runtime sharding may also be different

Assume that the final WordPiece vocabulary contains:

```text
hug, ##s, hu, ##gs
```

longest-match-first encoding `hugs`:

```text
hugs → hug | ##s
```

If a set of BPE merge order first forms `hu` and `gs`, it may be encoded as:

```text
hugs → hu | gs
```

The final result is determined by the respective true vocabulary and rules. This example shows the algorithm mechanism and does not mean that the real vocabulary of BERT or GPT-2 must be segmented this way.

## 9. Hand calculation conclusion

1. BPE training compares the absolute frequency of pairs;
2. Common WordPiece score will consider the marginal frequency of components;
3. BPE encoding replay merge priority;
4. WordPiece encoding performs longest prefix matching on the final vocabulary;
5. Both the training standard and the runtime algorithm may produce different token sequences.

