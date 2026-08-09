# Research questions, contributions and evidence boundaries

## 1. Research questions

Cognitive diagnostic applications typically accomplish two things first:

1. Specify the attributes to be diagnosed;
2. Specify the required attributes for each question to form a \(Q\) matrix.

The second step relies on collaboration between measurement experts, subject matter experts, and teachers. A large item bank will bring obvious labor costs. Zhao and Huang proposed:

> Can a batch of questions that have been marked by experts be used as a training set to allow the text classifier to learn the mapping of "question stem \(\rightarrow\) attributes" and then automatically mark new questions?

## 2. Three main contributions

### 2.1 Write Q row prediction as text supervised classification

The stem of each question is regarded as a short article, and the attributes are regarded as categories. Expert \(Q\) tag has become a supervision signal.

### 2.2 Give the three-stage pipeline

The paper breaks down the implementation into:

\[
\text{Feature extraction and selection}
\longrightarrow
\text{item vectorization}
\longrightarrow
\text{Attribute classification}.
\]

The specific components are:

- `jieba` Chinese tokenization;
- unigram、bigram、trigram；
- Information gain sorting and top-\(k\) filtering;
- TF--IDF；
- Logistic Regression、C-SVM、Gaussian Naive Bayes。

### 2.3 Compare three types of classifiers using real primary school mathematics problems

The experiment reports three \(n\)-gram combinations, three algorithms, and a complete \(3\times3\times2\) comparison with and without feature selection. The best combination is:

\[
\text{unigram+bigram+trigram}
+\text{IG}
+\text{Gaussian NB}.
\]

## 3. Where does the thesis evidence cover?

The proposition directly supported by the experiment is:

> Between the two high-frequency, mutually exclusive attributes of this third-grade mathematics item bank, the item stem vocabulary can provide a learnable classification signal.

Experiments have not directly tested:

- Nine attributes joint classification;
- One question corresponds to multi-label Q rows for multiple attributes;
- Cross-domain migration in new knowledge points or new courses;
- Parameter estimation and student classification quality after automatic labeling enters CDM;
- The efficiency of topic selection after automatic labeling enters CAT;
- Experts review how much the cost has been reduced.

## 4. How to understand innovation

The paper was published in a period when traditional text classification technology had matured. The algorithm components themselves are common, and contributions focus on **task migration**:

\[
\text{Short text classification technology}
\quad\Rightarrow\quad
\text{Q matrix semantic annotation}.
\]

This step opens the route of "item content can be directly entered into the Q build". Today's use of pretraining language models or multimodal models to automatically generate Q lines can be seen as continuing development along this line.

## 5. The most important reading reminder

Papers use automated Q-matrix identification in the title and conclusion. The output in the experiment is actually a single category for each question between `O` and `M`. A more accurate task name is:

\[
\text{binary cognitive-attribute classification from item text}.
\]

Therefore, separate the "original goal" and the "actual verification task" when reading.
