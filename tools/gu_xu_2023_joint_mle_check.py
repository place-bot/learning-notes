#!/usr/bin/env python3
"""Independent teaching checks for Gu & Xu (2023); not the authors' software.

Run: python3 tools/gu_xu_2023_joint_mle_check.py
No external dependencies; no paper simulations or official-code claims.
"""
from itertools import product
from math import exp, factorial, isclose, log, prod

def binary_matrices(rows, cols):
    for bits in product((0, 1), repeat=rows * cols):
        yield [list(bits[i * cols:(i + 1) * cols]) for i in range(rows)]

def ideal(a, q):
    return prod(a[k] for k in range(len(a)) if q[k])

def loglik(a, q, r, low, high):
    total = 0.0
    for i, person in enumerate(a):
        for j, item in enumerate(q):
            p = high[j] if ideal(person, item) else low[j]
            total += log(p) if r[i][j] else log(1 - p)
    return total

def near(x, y):
    assert isclose(x, y, rel_tol=1e-10, abs_tol=1e-10), (x, y)

def kl(p, q):
    return (p * log(p / q) if p else 0.0) + (
        (1 - p) * log((1 - p) / (1 - q)) if p < 1 else 0.0
    )

def entropy_term(p):
    return (p * log(p) if p else 0.0) + (
        (1 - p) * log(1 - p) if p < 1 else 0.0
    )

def check_gibbs():
    low, high = [.17, .29], [.83, .72]
    checks = 0
    for a in binary_matrices(2, 2):
        for q in binary_matrices(2, 2):
            for r in binary_matrices(2, 2):
                psi = [[r[i][j] * log(high[j] / low[j])
                        + (1 - r[i][j]) * log((1 - high[j]) / (1 - low[j]))
                        for j in range(2)] for i in range(2)]
                for i, k in product(range(2), repeat=2):
                    analytic = sum(q[j][k] * prod(
                        a[i][m] for m in range(2) if m != k and q[j][m]
                    ) * psi[i][j] for j in range(2))
                    old = a[i][k]
                    a[i][k] = 0
                    l0 = loglik(a, q, r, low, high)
                    a[i][k] = 1
                    l1 = loglik(a, q, r, low, high)
                    a[i][k] = old
                    near(l1 - l0, analytic)
                    checks += 1
                for j, k in product(range(2), repeat=2):
                    analytic = -sum((1 - a[i][k]) * prod(
                        a[i][m] for m in range(2) if m != k and q[j][m]
                    ) * psi[i][j] for i in range(2))
                    old = q[j][k]
                    q[j][k] = 0
                    l0 = loglik(a, q, r, low, high)
                    q[j][k] = 1
                    l1 = loglik(a, q, r, low, high)
                    q[j][k] = old
                    near(l1 - l0, analytic)
                    checks += 1
    near(1 / (1 + exp(-log(.8 / .2))), .8)
    near(1 / (1 + exp(log(.8 / .2))), .2)
    return checks

def check_profile_identity():
    p = [[.15, .32], [.47, .28], [.75, .61], [.88, .79]]
    groups = [[0, 0], [0, 1], [1, 0], [1, 1]]
    checks = 0
    for r in binary_matrices(4, 2):
        empirical = population = rhs = 0.0
        for j, c in product(range(2), repeat=2):
            idx = [i for i in range(4) if groups[i][j] == c]
            n = len(idx)
            hat = sum(r[i][j] for i in idx) / n
            bar = sum(p[i][j] for i in idx) / n
            empirical += n * entropy_term(hat)
            population += n * entropy_term(bar)
            rhs += n * kl(hat, bar) + sum(
                (r[i][j] - p[i][j]) * log(bar / (1 - bar)) for i in idx
            )
        near(empirical - population, rhs)
        checks += 1
    return checks

def check_boolean_lemma():
    counts = {}
    for k in (2, 3):
        profiles = list(product((0, 1), repeat=k))
        count = 0
        for q in binary_matrices(k, k):
            outputs = {tuple(ideal(a, row) for row in q) for a in profiles}
            is_permutation = (all(sum(row) == 1 for row in q)
                              and all(sum(row[c] for row in q) == 1 for c in range(k)))
            assert (len(outputs) == 2 ** k) == is_permutation
            count += len(outputs) == 2 ** k
        assert count == factorial(k)
        for q, other in product(profiles, repeat=2):
            if q != other:
                assert any(ideal(a, q) != ideal(a, other) for a in profiles)
        counts[k] = count
    return counts

def check_mixture_loss():
    count = 0
    for m, n in product(range(1, 8), repeat=2):
        hi, lo = .81, .23
        avg = (m * hi + n * lo) / (m + n)
        loss = m * (hi - avg) ** 2 + n * (lo - avg) ** 2
        near(loss, m * n / (m + n) * (hi - lo) ** 2)
        assert 2 * m * n / (m + n) >= min(m, n)
        count += 1
    return count

if __name__ == "__main__":
    print("Gibbs log-odds checks:", check_gibbs())
    print("Profile-likelihood identities:", check_profile_identity())
    print("Boolean injective matrices by K:", check_boolean_lemma())
    print("Mixture-loss identities:", check_mixture_loss())
    joint_moment = .5 * 0 * 0 + .5 * 1 * 1
    product_of_means = (.5 * 0 + .5 * 1) ** 2
    near(joint_moment, .5)
    near(product_of_means, .25)
    assert joint_moment != product_of_means
    print("Product-of-means counterexample:", joint_moment, product_of_means)
    print("PASS: all independent teaching checks.")
