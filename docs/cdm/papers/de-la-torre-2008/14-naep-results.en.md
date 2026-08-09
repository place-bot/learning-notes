#NAEP result and item case

## Test level result

Original Q:

\[
\bar g+\bar s=.6923.
\]

When \(\varepsilon\) increases from 0, the indicator first decreases; after exceeding about .011, it turns upward. The optimal point is:

\[
\varepsilon=.011,\qquad
\bar g+\bar s=.6847.
\]

Definitely improved to

\[
.6923-.6847=.0076.
\]

The improvement is about 1.1% of the original value, consistent with what the authors call modest improvement.

## Q Consistency rate

At \(\varepsilon=.011\):

- 773 of the 810 Q grids are the same as the original Q, with a consistency rate of 95%;
- 68 of the 90 lines are identical, with a consistency rate of 76%;
- There are 37 grid changes in total, affecting 22 questions.

If the priority is to pursue consistency with the original Q, you can choose:

\[
\varepsilon=.001.
\]

At this time:

- Grid consistency rate 98%;
- The consistency rate for the entire row is 87%;
- \(\bar g+\bar s=.6895\), still .6923 lower than the original.

As the threshold continues to increase, the consistency rate eventually stops at approximately:

- Grid 88%, i.e. 713/810;
- 37% of the entire row, or 33/90.

## Change distribution by question

Original Figure 5 compares the changes in each question \(s+g\) when comparing \(\varepsilon=.001\) and .011:

- About 10 questions got worse;
- Most questions improved;
- Most improvements for \(\varepsilon=.001\) are in .00--.01;
- Most improvements for \(\varepsilon=.011\) are in .00--.02;
- Only a few questions have been significantly improved.

A decrease in the average metric does not mean that every question has improved.

## Case 1: Confirm the original specification

The original Q requirements for question 45:

- Attribute 2: Measurements, units and conversions;
- Attribute 3: Data display;
- Attribute 5: Score;
- Property 7: Interpolation, Extrapolation and Estimation.

\(\varepsilon=.011\)'s recommendation is to retain these four properties. This question shows that statistical results can provide support for existing expert specifications.

## Case 2: Questioning redundant attributes

Question 80 originally required attributes 6, 7, and 9:

\[
\widehat g=.31,\qquad \widehat s=.50.
\]

After the candidate only retains attribute 6:

\[
\widehat g=.24.
\]

This result questions whether properties 7 and 9 are indeed necessary to answer the question. You still need to check the item content and answer process before deleting it.

## Case 3: Propose equivalent explanation

Question 52 Original requirement:

- Attribute 2: Measurements, units and conversions;
- Property 7: Interpolation, Extrapolation and Estimation.

The original estimate was approximately:

\[
\widehat g=.42,\qquad \widehat s=.07.
\]

The recommendation vector retains attribute 2, replaces attribute 7 with attribute 9 "higher-order thinking", and the item parameters remain almost unchanged.

The data lack clear discriminability between these two cognitive explanations. This case illustrates the possibility that empirically nearly equivalent specifications exist for a Q row.

## Case 4: Confirm that the item lacks diagnostic information

Both sets of question 19 have a correct answer rate of .54:

\[
P(X=1\mid\eta=0)
\approx
P(X=1\mid\eta=1)
=.54,
\]

\[
\delta\approx0.
\]

Low \(\delta\) sometimes comes from Q being written incorrectly; for question 19, the search confirmed that the original q-vector is the best candidate. Therefore, under the current nine-attribute system, this question indeed lacks diagnostic distinction.

## How to locate result

The NAEP app supports four uses:

1. Confirm the original q-vector;
2. Question whether certain attributes are necessary;
3. Propose statistically equivalent alternative specifications;
4. Distinguish between "Q is written incorrectly" and "item has no information under the current attribute system".

Since the initial DINA fit was clearly poor, .6847 was still high, and modifying Q did not address the entire model misfit.

