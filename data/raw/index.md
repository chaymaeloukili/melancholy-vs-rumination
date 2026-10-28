# title: Survey Data on Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences
- grant:  Academy of Finland Grant 270220 (Surun Suloisuus)
- date: 21-04-2016
- authors: T. Eerola
- affliation: Durham University, UK
- subset: Main data
- location: Harvard Dataverse
- publication: Eerola, T., & Peltola, H.-R. (in preparation). Memorable Experiences with Sad Music – Reasons, Reactions and Mechanisms of Three Types of Experiences. Plos One.
- citation: University of Durham. Department of Music, Structure of Sadness [computer file]. 1st Edition. Durham, Country Durham: Harvard Dataverse [distributor], April 2016, http://dx.doi.org/10.7910/DVN/GLSIXB

## S1_data.csv

Sample 1 (Finnish Convenience Sample) (1577 rows, 131 columns). CSV comma-delimited file.

## S2_data.csv

Sample 2 (UK Representative Sample) (414 rows, 131 columns). CSV comma-delimited file.

## S3_data.csv

Sample 3 (Finnish Quota Sample) (445 rows, 131 columns). CSV comma-delimited file.

### Structure of the Data

All datasets, `S1-S3_data.csv`, contain the following column variables:

- `subj` *[integer]*: unique id for each subject
- `age` *[string]*: age (*18 to 24*, *25 to 34*, *35 to 44,*45 to 54*, *55 to 64*, *65 to 74*, *75 or older*)
- `gender` *[string]*: gender (*female*,*male*)
- `listen` *[string]*: How often subject listens to music (*1-2/year*, *1-2/mo*, *1/week*, *mult/week*, *daily*, *mult./day*)
- `expert` *[string]*: Musical expertise (*Non-Musician*,*Music Lover*, *Amateur musician*, *Semi-professional musician*, *Professional musician*)
- `listensad` *[string]*: How often subject listens to sad music (*Frequently*,*Often*,*Sometimes*,*Rarely*,*I don't listen to sad music voluntarily*)
- `ASM1-ASM25` *[integer]*: Answers to Attitudes towards Sad Music (1-7), see ASM_label.csv for labels of each 25 items.
- `R1-R24` *[integer]*: Answers to Reasons for listening to Sad Music (binary), see REASON_label.csv for labels of each 24 items.
- `AGO` *[string]*: How long time ago was the memorable experience (*less than day*, *2-5 days*, *6-10 days*, *11-30 days*, *1-6 months*, *7-12 months*, *over year*).
- `CHOICE` *[string]*: Was the music chosen by the subject? (*Self-chosen*, *Not self-chosen*)
- `REASON1-REASON13` *[integer]*: Was the reason for listening to sad music in that particular instance? (*1*, *NA*).
- `FAM` *[string]*: Was the music familiar to the subject? (*unfamiliar*,*somewhat familiar*,*familiar,*extremely familiar*)
- `IMPORTANCE` *[string]*: How autobiographically important was the music to the subject? (*Not at all*,*Quite Important*,*Important*,*Extremely Important*)
- `DURATION` *[string]*: How long did the episode last? (*<5min*,*5-10 min*,*10-30 min*,*31-60 min*,*60 min+*)
- `FEELING1-FEELING36` *[integer]*: Was the FEELING term that fitted the experience? (*1*, *NA*), see FEELING_label.csv
- `INTENSITY` *[integer]*: How intense was the emotion in the episode? (1-7, 1=not intense at all, 7 = extremely intense)
- `PLEASURE` *[integer]*: How pleasurable was the emotion in the episode? (1-7, 1=not pleasurable at all, 7 = extremely pleasurable)
- `PHYS1-PHYS5` *[integer]*: Was were the physical reactions associated with the episode? (*1*, *NA*), see PHYS_label.csv
- `MEC1-MEC10` *[integer]*: Was were the mechanisms associated with the episode? (*1*, *NA*), see MEC_label.csv
- `MOODCHANGE` *[string]*: How was your mood after the episode? (*Worse*,*Same*,*Better*,*NA*)
- `PHYSCHANGE` *[string]*: How was your physical state after the episode? (*Worse*,*Same*,*Better*,*NA*)
- `ESSENTIAL1-ESSENTIAL3` *[string]*: How often have you experienced feelings ... (see ESSENTIAL_LABELS.csv for details)? (*Never*,*Rarely*,*Sometimes*,* *Frequently*,*Very Frequently*)

## Additional Data Labels

### ASM_label.csv

Information about the 25 items from the Attitudes to Sad Music (Eerola, Peltola, & Vuoskoski, 2015). Each item is in a separate line, corresponds to data files ASM1-ASM25 (where ASM1 is the item #1 etc.).

### REASON_label.csv

Information about the 13 items that represent the reasons for listening to particular sad music during the episode. Each item is in a separate line, corresponds to data files REASON1-REASON13 (where REASON1 is the item #1 etc.).

### FEELING_label.csv

Information about the 36 terms that people could choose to represent the emotion experienced during the episode. Each item is in a separate line, corresponds to data files FEELING1-FEELING36 (where FEELING1 is the item #1 etc.).

### MEC_label.csv

Information about the 10 items representing the mechanisms responsible for the emotion during the episode (Adapted from Juslin, 2015). Each item is in a separate line, corresponds to data files MEC1-MEC10 (where MEC1 is the item #1 etc.).

### PHYS_label.csv

Information about the 5 items representing the physical reactions in response to memorable the episode. Each item is in a separate line, corresponds to data files PHYS1-PHYS5 (where PHYS1 is the item #1 etc.).

### ESSENTIAL_label.csv

Information about 3 broad concepts of emotions experienced generally (how often). Adapted from Peltola and Eerola (2016). Each item is in a separate line, corresponds to data files ESSENTIAL1-ESSENTIAL10 (where ESSENTIAL1 is the item #1 etc.).

## References

* Eerola, T., Peltola, H.-R., & Vuoskoski, J. K. (2015). Attitudes towards sad music are related to both preferential and contextual strategies. *Psychomusicology: Music, Mind, and Brain, 25(2)*, 116-123. 

* Peltola, H.-R. & Eerola, T. (2016). Fifty Shades of Blue: Classification of music-evoked sadness. *Musicae Scientiae, 20(1)*, 84-102. 

* Juslin, P. N., Barradas, G., & Eerola, T. (2015). From Sound to Significance: Exploring the Mechanisms Underlying Emotional Reactions to Music. *American Journal of Psychology, 128(3)*, 281-304. 

