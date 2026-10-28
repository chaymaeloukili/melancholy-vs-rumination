# The Thin Line Between Melancholy and Rumination

What happens when we listen to sad music? A learning project on how sad music is linked to our emotions – when it comforts us, and when it may pull us down.

This project is a work in progress. I am building it slowly, step by step, alongside my studies, out of curiosity and to learn.

## Why this project?

Many people say that music influences us strongly and that we should be careful about what we listen to. Some even talk about certain frequencies having special effects.

I noticed that I personally listen to a lot of melancholic music, and that it does me good. In everyday life there are not many moments where I simply allow my emotions to be there – without thinking about them too much, without feeling bad and without falling into a low. For me, sad music works like a safety net.

That made me wonder why other people see it differently, and how many people feel the way I do.

For me, music is also art. Through music, people can get to know themselves better or close a chapter of their lives. Some songs I never listen to again, because they belong to a certain time. Others feel like they were written just for me, or they hold memories.

Listening with headphones can feel like a small survival kit: you switch off for a moment, but without losing touch with reality. In that moment you are vulnerable, but nobody around you notices.

I also find that many songs tell the artist's own story. When you really listen and empathise with them, you value their art more – a bit like visiting a museum. You do not always have to project yourself into it. Otherwise you only consume the music instead of really appreciating it.

These are personal observations, not scientific facts. With this project, I want to find out what research and data actually say.

## Research question

Who feels better and who feels worse after a memorable experience with sad music – and how do their reasons and feelings differ?

1. **Observe:** How do people feel after listening to sad music – better, the same or worse?
2. **Compare:** Do people who listen to sad music often feel different from people who rarely do?
3. **Understand:** Which feelings, reasons and attitudes go along with feeling better or worse?
4. **Reflect:** Where is the line between melancholy that helps and rumination that pulls us down?

## Reflection

Is it healthy to seek out sadness on purpose? Can sad music help us process our emotions, or can it keep us stuck in them? The answer is probably different for each person, and data alone cannot fully answer it. But I want to keep this question in mind throughout the project.

## Key concepts

1. Melancholy vs. rumination
2. Emotion regulation
3. The paradox of enjoying sad music
4. Empathy and being moved by art
5. Self-reports vs. measurements of the brain and body

## Data and sources

**Data:** Eerola, T. (2016). *Survey Data on Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences.* Harvard Dataverse. https://doi.org/10.7910/DVN/GLSIXB (CC0 1.0)

A survey with about 2,400 people from Finland and the UK, who described a memorable experience with sad music. Details: [`data/raw/README.md`](data/raw/README.md)

**Background reading:**
- Eerola, T. & Peltola, H.-R. (2016). Memorable experiences with sad music – reasons, reactions and mechanisms of three types of experiences. *PLOS ONE*, 11(6), e0157444. https://doi.org/10.1371/journal.pone.0157444
- Sachs, M. E., Damasio, A. & Habibi, A. (2015). The pleasures of sad music: a systematic review. *Frontiers in Human Neuroscience*, 9, 404. https://doi.org/10.3389/fnhum.2015.00404
- Taruffi, L. & Koelsch, S. (2014). The paradox of music-evoked sadness: an online survey. *PLOS ONE*, 9(10), e110490. https://doi.org/10.1371/journal.pone.0110490
- Garrido, S. & Schubert, E. (2015). Moody melodies: Do they cheer us up? A study of the effect of sad music on mood. *Psychology of Music*, 43(2), 244–261. https://doi.org/10.1177/0305735613501938
- Taruffi, L., Pehrs, C., Skouras, S. & Koelsch, S. (2017). Effects of sad and happy music on mind-wandering and the default mode network. *Scientific Reports*, 7, 14396. https://doi.org/10.1038/s41598-017-14849-0

## Why not streaming data?

It would have been easy to use data from streaming platforms such as Spotify. But streaming data only shows *what* was played – not whether people listened consciously or just let a playlist run, and not how they felt before or after.
For my question, I need people's own descriptions of their feelings. That is why I chose survey data instead.

## Project structure

| Folder / file | Content |
|---|---|
| `data/raw/` | original data and documentation (never modified) |
| `data/processed/` | cleaned data (coming soon) |
| `notebooks/` | the analysis, step by step (see [`notebooks/README.md`](notebooks/README.md)) |
| `AI_USAGE.md` | how I use AI in this project |

## Status

- Done: data exploration ([`notebooks/01_explore.ipynb`](notebooks/01_explore.ipynb))
- Next: data cleaning
- Later: analysis, charts, and maybe neuroscience data (EEG or fMRI)

## Limitations

- The data are self-reports: people remember one past experience. This shows how they experienced it, not what happened in the brain.
- Rumination was not measured directly. Feeling worse after sad music is only a hint, not proof of a downward spiral.
- The samples differ in country and in how people were recruited.

## Tools

Python (pandas, matplotlib), Jupyter, Git and GitHub

## Use of AI

I use Claude (Anthropic) as a tool. Most of the code was written by Claude based on my instructions; I ran it, checked the results and asked about every part I did not understand. Claude also explains new concepts and helps me document my work.

**My own:** the topic and research question, the approach (e.g. first going through all 131 columns, then deciding what is relevant, and exploring each sample separately), the choice of data and columns, and the interpretation.

Details: [AI_USAGE.md](AI_USAGE.md)

## Licence

Code in this repository is licensed under the [MIT License](LICENSE). The data is CC0 1.0 (Eerola, 2016).
