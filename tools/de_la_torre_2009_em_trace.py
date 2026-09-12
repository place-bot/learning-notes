#!/usr/bin/env python3
"""A deterministic, fully worked EM example. Not a paper-data reproduction."""
import math
from de_la_torre_2009_dina_em import (
    all_attribute_patterns, ideal_response_matrix, e_step, m_step, inverse_matrix,
)

Q = [(1, 0), (0, 1), (1, 1)]
X = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0]]
G = [.20, .10, .25]
S = [.10, .20, .15]
PI = [.25] * 4

def close(a, b, tol=1e-8):
    assert math.isclose(a, b, abs_tol=tol, rel_tol=tol), (a, b)

def counts(x, eta, w):
    totals = []
    h = [[sum(wi[l] * eta[l][j] for l in range(len(eta)))
          for j in range(len(Q))] for wi in w]
    for j in range(len(Q)):
        n1 = sum(row[j] for row in h)
        r1 = sum(xi[j] * hi[j] for xi, hi in zip(x, h))
        n0 = len(x) - n1
        r0 = sum(xi[j] for xi in x) - r1
        close(n0 + n1, len(x))
        close(r0 + r1, sum(xi[j] for xi in x))
        totals.append([n0, r0, n1, r1])
    return h, totals

def score(x, eta, wi, g, s):
    out = []
    for j in range(len(Q)):
        h = sum(wi[l] * eta[l][j] for l in range(len(eta)))
        out += [(1-h)*(x[j]-g[j])/(g[j]*(1-g[j])),
                h*((1-s[j])-x[j])/((1-s[j])*s[j])]
    return out

def main():
    patterns = all_attribute_patterns(2)
    eta = ideal_response_matrix(patterns, Q)
    print("Profiles:", patterns)
    print("ETA:", eta)
    probabilities = [[1-S[j] if row[j] else G[j] for j in range(3)] for row in eta]
    print("Class probabilities:", probabilities)
    w, old_ll = e_step(X, eta, G, S, PI)
    print("Conditional likelihood / marginal / posterior:")
    for xi, wi in zip(X, w):
        likelihoods = [math.prod(p if x else 1-p for x,p in zip(xi,row))
                       for row in probabilities]
        marginal = sum(pi*l for pi,l in zip(PI, likelihoods))
        direct = [pi*l/marginal for pi,l in zip(PI, likelihoods)]
        for a,b in zip(wi,direct):
            close(a,b)
        close(sum(wi),1)
        print(xi, [round(v,9) for v in likelihoods],
              round(marginal,9), [round(v,9) for v in wi])
    h, totals = counts(X, eta, w)
    print("Posterior ideal-state probabilities:", h)
    print("Counts [N0, R0, N1, R1]:", totals)
    g1, s1 = m_step(X, eta, w)
    for j,(n0,r0,n1,r1) in enumerate(totals):
        close(g1[j],r0/n0)
        close(s1[j],(n1-r1)/n1)
    w1, ll1 = e_step(X, eta, g1, s1, PI)
    g2, s2 = m_step(X, eta, w1)
    _, ll2 = e_step(X, eta, g2, s2, PI)
    print("g1:", g1, "s1:", s1)
    print("Posterior at updated parameters:", w1)
    print("g2:", g2, "s2:", s2)
    print("Loglik [initial, after 1, after 2]:", old_ll, ll1, ll2)
    print("Max parameter change round 1:",
          max(abs(a-b) for a,b in zip(G+S,g1+s1)))
    assert ll1 >= old_ll-1e-10 and ll2 >= ll1-1e-10
    pi1 = [sum(row[l] for row in w)/len(X) for l in range(4)]
    print("Optional updated prior:", pi1)
    _, ll_eb = e_step(X, eta, g1, s1, pi1)
    assert ll_eb >= old_ll-1e-10
    scores = [score(xi,eta,wi,G,S) for xi,wi in zip(X,w)]
    print("First student's interleaved score:", scores[0])
    # Independent central finite differences of the actual marginal log likelihood.
    step = 1e-6
    for c in range(6):
        gp,gm,sp,sm = list(G),list(G),list(S),list(S)
        if c%2:
            sp[c//2]+=step
            sm[c//2]-=step
        else:
            gp[c//2]+=step
            gm[c//2]-=step
        lp = e_step(X,eta,gp,sp,PI)[1]
        lm = e_step(X,eta,gm,sm,PI)[1]
        close((lp-lm)/(2*step),sum(row[c] for row in scores),1e-6)
    info = [[sum(row[a]*row[b] for row in scores) for b in range(6)] for a in range(6)]
    assert inverse_matrix(info) is None  # Four score rows cannot span six dimensions.
    print("4-person OPG singular as expected; no invented SEs.")
    toy_cov = inverse_matrix([[4.,1.],[1.,9.]])
    close(toy_cov[0][0],9/35)
    close(toy_cov[1][1],4/35)
    # Check ten updates without claiming they reach convergence/global optimality.
    g,s,ll = list(G),list(S),old_ll
    for _ in range(10):
        wi,_ = e_step(X,eta,g,s,PI)
        g,s = m_step(X,eta,wi)
        _,next_ll = e_step(X,eta,g,s,PI)
        assert next_ll >= ll-1e-10
        ll = next_ll
    print("PASS: direct Bayes, expected counts, M-step, six score derivatives,")
    print("likelihood ascent, singularity, and illustrative matrix inversion.")

if __name__ == "__main__":
    main()
