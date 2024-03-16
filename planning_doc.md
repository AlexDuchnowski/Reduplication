# Overall Structure of Paper
- Intro
- Background Research
- Data & Methods
- Results
- Analysis / Discussion
- Conclusion

# Basic Division of Labour
- Alex: read some lit, set up code that expects a list of words & their sentences --> set up POS analysis & figure out semantic cont. (can we infer it from a sentence or do we need more context?)
- Ford: read some lit, look thru salad-salad dataset & develop typology (look 4 trends, etc.)
- Arushi: read some lit, some preprocessing (filtering char., identify redup, regex'ing)

--> Goal is to be done by the end of Spring Break ~ Reconvene @ Apr. 1, redivide labor 
- Maybe we annotate some small amount of data, then train a langmodel to analyze the rest based on our own judgements (assuming it works)

*Actually writing the paper happens in a few weeks lol --> Analysis may also happen in a few weeks

# Pipeline
- Get Data --> get corp, figure out text
- Preprocess --> filter out extra characters (hypens, parenthesis, brackets), build up POS column, detect reduplication, semantic contribution column
        Note on this: manually check if the reduplications are authentic/valid (do do, really really, etc.) --> there will be a certain amount of noise
        Semantic contribution will also be a period where we filter things
- Analyze --> stats in R, manipulating the data table (no new data, just analyzing present data)
