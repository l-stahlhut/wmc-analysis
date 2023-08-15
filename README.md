# WMC Battery Analysis

Python implementation of the WMC Battery Analysis (Lewandowsky et al., 2010).
This code writes a file "scores.txt" which contains Subject ID and Scores for the 4 Tasks as well as a total score 
(arithmetic mean). 

## How to use the code

```python
python3 main.py path/to/data
```
Where the data folder contains all results files (MU, SS, OS, SSTM) for all participants.
## WMC
The working memory test battery (Lewandowsky et al.) consists of 4 tasks:
1. *Memory updating task (MU)*: Memorize 3-5 digits & update them through arithmetic tasks
2. *Operation-span task (OS)*: Memorize a sequence of consonants; distractor: true/false arithmetic equations between the consonants. 
3. *Sentence-span task (SS)*: Memorize a sequence of consonants; distractor: true/false sentences between the consonants.
4. *Spatial short-term memory task (SSTM)*: Remember the location of dots in a grid.


### Scoring
- MU, OS, SS: Proportion of items recalled correctly (e.g. remembering five out of six letters in a span-task trial would score 5/6 in that trial.)
- OS, SS: Item is correct if it was reproduced in the correct list position.
- Total score: Mean of these partial scores across trials. 
- SSTM: Max. score is 240
- Q: Should SSTM be included in the total score (mean?)

### Data 
Overviews of the content of the different results files by column. 
- MU: 0 = ID; 1 = trial; 2-9 = responses (typed digits, padded with 0s); 10-15 = correct (1) /incorrect (0), padded with
-1.
- OS & SS: 0 = ID; 1 = trial; 2 = list length; 3-10 = letters presented on screen, padded with %; 11-18: typed response, 
padded with %; 19-26: response time to recall letters; 27-34: equations (distractors) correct/incorrect (1/0); 35-42: 
score for the responses of the equations (0/1); 43-50: response time for equations
- SSTM: Overall score is recorded. Max score is 240. 


Source: Lewandowsky, S. et al. (2010): A working memory test battery for MATLAB. In: Behavior Research Methods 42(2), 
p. 571-585.

## License
[MIT](https://choosealicense.com/licenses/mit/)
