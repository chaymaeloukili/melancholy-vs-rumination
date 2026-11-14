# AI Usage

This is a learning project. I use Claude (Anthropic) as a tutor, and I want to be open about how.

## So far (exploration and cleaning)
Most of the code was written by Claude based on my instructions. I was not a passive user:
- I decided the approach and the order of the steps (e.g. first going through all 131 columns before cleaning)
- I typed and ran every cell myself, read every output and checked it against the data and the documentation
- I questioned the data: e.g. that streaming data is not suitable, that the samples differ, that missing answers must not be ignored, that `PHYSCHANGE` is not a checkbox
- I found and fixed my own errors (e.g. a `KeyError` and a wrong variable name)
- I made all decisions about which columns to keep, remove or change, and why

## Analysis (03_analysis)

**My own ideas and decisions in the analysis**
- I noticed that counts are misleading when groups have different sizes and asked to compare percentages instead.
- I asked for one table that shows all three samples side by side with the differences between Better and Worse, so they can be compared directly.
- I wanted the feeling, reason and attitude labels shown next to the column codes (e.g. FEELING4 = sadness), so the tables are readable.
- I decided to check the samples one by one (S3, then S2, then the S1 fans), and to test whether age explains the difference between the countries.
- I kept the small group sizes in mind and did not over-interpret them.

**Code**
- I wrote most of the code myself, often by reusing and adapting patterns from `02_clean` (loading the data, crosstabs, selecting samples), and fixed my own errors (`FileNotFoundError`, `IndentationError`, `KeyError`, `AttributeError`, `NameError`).
- Claude gave me hints and templates when I got stuck, and wrote the code for the larger comparison tables with differences and colours on my request.

**Interpretation**
- The analysis of the results is my own: I read every table, wrote down what I noticed and developed my own ideas (e.g. language of songs, sad music as an outlet, a possible translation issue, people listening to sad music as a tool).
- Claude helped me to read the tables correctly (differences vs. percentages, small groups) and to put my notes into English.

## What stays my own
The topic, the research question, the choice of data, all decisions about the data and the interpretation of the results.
