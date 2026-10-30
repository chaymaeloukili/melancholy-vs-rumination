# AI Usage

This is a learning project. I use Claude (Anthropic) as a tutor, and I want to be open about how.

## So far (exploration and cleaning)
Most of the code was written by Claude based on my instructions. I was not a passive user:
- I decided the approach and the order of the steps (e.g. first going through all 131 columns before cleaning)
- I typed and ran every cell myself, read every output and checked it against the data and the documentation
- I questioned the data: e.g. that streaming data is not suitable, that the samples differ, that missing answers must not be ignored, that `PHYSCHANGE` is not a checkbox
- I found and fixed my own errors (e.g. a `KeyError` and a wrong variable name)
- I made all decisions about which columns to keep, remove or change, and why

## From now on (analysis and visualisation)
I write more of the code myself. I first try on my own and look up what I need; Claude helps when I get stuck, explains errors and checks my code.
The notebooks show which parts I wrote myself.

## What stays my own
The topic, the research question, the choice of data, all decisions about the data and the interpretation of the results.
