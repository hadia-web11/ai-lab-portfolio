# Lab 02 Report - Web Scraping, Feature Engineering and EDA
Date: 23 Oct 2026

## NumPy vs Python loop (Task 2.1)
Summing 10,000,000 random numbers: NumPy takes a few milliseconds; the Python for-loop takes seconds
(typically 100-1000x slower). Both give the same sum. NumPy runs the loop in compiled C over a whole array.
(Paste your own timings from the notebook here.)

## EDA findings
- Title length: titles are of similar length (histogram `fig1_title_length.png`).
- Sentiment polarity: articles are mildly positive (about 0.1 to 0.3) and fairly subjective (`fig2_polarity.png`).
- Pair plot (`fig3_pairplot.png`): token count and sentence count are strongly positively correlated (longer articles have more sentences).
- With only 5 articles, no distribution can be generalised to a population.

## TF-IDF interpretation
TF-IDF is high for words that are frequent in a document but rare in the others. With English stop words removed the top terms are content words
(ai, tools, ...). With `stop_words=None` words like "the", "and" dominate, because they are frequent everywhere.
