# The Thin Line Between Melancholy and Rumination

What happens when we listen to sad music? This is a learning project on **who feels better and who feels worse after sad music**, when it comforts us and when it may pull us down.

This project is a work in progress. I am building it slowly, step by step, alongside my studies, out of curiosity and to learn.

### Why this project?

Many people say that music influences us strongly and that we should be careful about what we listen to. Some even talk about certain frequencies having special effects.

I noticed that I personally listen to a lot of melancholic music, and that it does me good. In everyday life there are not many moments where I simply allow my emotions to be there, without thinking about them too much, without feeling bad and without falling into a low. For me, sad music works like a safety net.

That made me wonder why other people see it differently, and how many people feel the way I do.

For me, music is also art. Through music, people can get to know themselves better or close a chapter of their lives. Some songs I never listen to again, because they belong to a certain time. Others feel like they were written just for me, or they hold memories.

Listening with headphones can feel like a small survival kit. You switch off for a moment, but without losing touch with reality. In that moment you are vulnerable, but nobody around you notices.

I also find that many songs tell the artist's own story. When you really listen and empathise with them, you value their art more, a bit like visiting a museum. You do not always have to project yourself into it. Otherwise you only consume the music instead of really appreciating it.

These are personal observations, not scientific facts. With this project, I want to find out what research and data actually say.

### Research question

Who feels better and who feels worse after a memorable experience with sad music, and how do their reasons and feelings differ?

1. **Observe.** How do people feel after listening to sad music, better, the same or worse?
2. **Compare.** Do people who listen to sad music often feel different from people who rarely do?
3. **Understand.** Which feelings, reasons and attitudes go along with feeling better or worse?
4. **Reflect.** Where is the line between melancholy that helps and rumination that pulls us down?

### Reflection

Is it healthy to seek out sadness on purpose? Can sad music help us process our emotions, or can it keep us stuck in them? The answer is probably different for each person, and data alone cannot fully answer it. But I want to keep this question in mind throughout the project.

### Key concepts

1. Melancholy vs. rumination
2. Emotion regulation
3. The paradox of enjoying sad music
4. Empathy and being moved by art
5. What people report about themselves vs. measurements of the brain and body

### Data and sources

The data comes from Eerola, T. (2016). *Survey Data on Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences.* Harvard Dataverse. https://doi.org/10.7910/DVN/GLSIXB (CC0 1.0)

It is a survey with about 2,400 people from Finland and the UK, who described a memorable experience with sad music. You can find more details in [`data/raw/README.md`](data/raw/README.md).

For background reading I use three studies.

1. Eerola, T. & Peltola, H.-R. (2016). Memorable experiences with sad music – reasons, reactions and mechanisms of three types of experiences. *PLOS ONE*, 11(6), e0157444. https://doi.org/10.1371/journal.pone.0157444  
   This is the study behind the dataset.
2. Garrido, S. & Schubert, E. (2015). Moody melodies: Do they cheer us up? A study of the effect of sad music on mood. *Psychology of Music*, 43(2), 244–261. https://doi.org/10.1177/0305735613501938  
   Here mood got worse after sad music, and rumination was measured.
3. Taruffi, L., Pehrs, C., Skouras, S. & Koelsch, S. (2017). Effects of sad and happy music on mind-wandering and the default mode network. *Scientific Reports*, 7, 14396. https://doi.org/10.1038/s41598-017-14849-0  
   This study shows that sad music turns thoughts inwards.

### Why not streaming data?

It would have been easy to use data from streaming platforms such as Spotify. But streaming data only shows *what* was played, not whether people listened consciously or just let a playlist run, and not how they felt before or after. For my question, I need people's own descriptions of their feelings. That is why I chose survey data instead.

### Project structure

| Folder / file | Content |
|---|---|
| `data/raw/` | original data and documentation (never modified) |
| `data/processed/` | cleaned data in `sad_music_clean.csv` (2,436 people, all three samples in one table) |
| `notebooks/` | the analysis, step by step (see [`notebooks/README.md`](notebooks/README.md)) |
| `src/` | the same steps as the notebooks, as scripts that run in one go |
| `results/` | all tables from the analysis as CSV files, made by `src/analysis.py` |
| `AI_USAGE.md` | how I use AI in this project |

### Status

I have finished the data exploration, the cleaning and the analysis (steps 1 to 10, including a data quality check and statistical tests). Next comes the visualization. Later I will add the results and limitations to this README and turn the notebooks into scripts.

### Key findings so far

In Finland most people felt better after their experience with sad music (74 to 79 %). In the UK most people felt the same (48 %), and only 38 % felt better. Age does not explain this.

People who listen to sad music more often felt better more often, in all three samples. Choosing the music yourself and listening longer go together with feeling better. Comfort, relief and peacefulness are the feelings most linked to feeling better.

Beauty runs through everything. It is the strongest reason, mechanism and part of pleasure linked to feeling better. "Better" and "Worse" were both intense experiences. What separates them is how pleasant it felt, not how strong.

These are connections, not causes. People remembered their experience and answered about themselves. The UK attitude answers (ASM) were not reliable and are left out.

The full analysis and my conclusion are in [`notebooks/03_analysis.ipynb`](notebooks/03_analysis.ipynb).

### Limitations

The data is based on what people report about themselves, and they remember one past experience. This shows how they experienced it, not what happened in the brain. Rumination was not measured directly, so feeling worse after sad music is only a hint and not proof of a downward spiral. The samples also differ in country and in how people were recruited.

### How to run

1. Install Python 3 and the packages with `pip install -r requirements.txt`
2. Run `python src/clean.py` to create the clean data
3. Run `python src/analysis.py` to create all tables in `results/`

The notebooks in `notebooks/` show the same steps with my notes and thoughts. The scripts are the quick way to repeat everything.

### Tools

Python (pandas, matplotlib, scipy), Jupyter, Git and GitHub

### Use of AI

This is a learning project, and I use Claude (Anthropic) as a tutor. In exploration and cleaning, most of the code was written by Claude based on my instructions. I ran and checked every step and made all decisions about the data. From the analysis on, I write more of the code myself.

The topic and research question are my own, and so is the approach, for example first going through all 131 columns, then deciding what is relevant, and exploring each sample separately. The choice of data and columns and the interpretation are also mine.

You can read more in [AI_USAGE.md](AI_USAGE.md).

### Licence

Code in this repository is licensed under the [MIT License](LICENSE). The data is CC0 1.0 (Eerola, 2016).