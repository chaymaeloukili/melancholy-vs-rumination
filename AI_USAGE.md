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



## Analysis, steps 7b to 10 (03_analysis)

**My own ideas and decisions in the analysis**
- I noticed that one topic needed too many tables, which led to using one function for all situation questions.
- I looked at every table myself, interpreted it and gave reasons for what I saw.
- I wrote my notes partly in German and partly in English, and went over the grammar with Claude.
- I wrote my own conclusion in German, based on all my notes.

**Code**
- Claude wrote most of the code in steps 8 and 9 on my request (the functions `mood_by`, `chi_test` and `chi_items`) and explained each part.
- I adapted these patterns for the other topics and fixed my own errors.

**Statistics**
- I asked which test to use, what the values mean (p-value, Cramér's V), when a value is high or low, and why.
- After that I applied this understanding to the rest of the tests myself.
- I also checked with Claude whether the UK attitude answers are plausible (step 7b).

**Interpretation**
- After interpreting the results myself, I asked Claude to confirm them and explain why something is the way it is. Sometimes Claude pointed out small details, for example when a group was too small.
- Claude translated my conclusion into English in my style and checked that every sentence matches the data.



## Scripts (src/)

**Code**
- I decided to turn the notebooks into scripts, because they are easier to run for other people.
- Claude wrote the scripts based on my notebooks `02_clean` and `03_analysis`. I ran them and checked that the results are the same as in my notebooks.