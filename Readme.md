# Readme ScrapeLife

Goal: For this project, you will be scraping data from GitHub repository 
README files. The goal will be to build a model that can predict what 
programming language a repository is, given the text of the README file.



Deliverables

A well-documented jupyter notebook that contains your analysis
One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.



Required Libraries:
- Pandas
- Beautiful Soup
- numpuy
- matplotlib
- os
- re
- unicodedata
- nltk

Disclaimer: The assignment called for us to pull the top 100 most forked repos. Our intial investigation showed that the majority of the top 100 was all java based repos. In order to improve our model to work with other languages, e decided to ouyll the top 120 repos of the four languages (Python, Java, javaScript, Php).

Acquire:
Using github's API and beautiful soup to scrape the top 130 repos of four different languages (Python, Java, javaScript, Php).

Prep:
Prepared our data with beautiful soup and regex commands to remove excess noise. 

Exploration:
We wanted to find the most occuring words unique to each language repos. We used word clouds to see a overview of the most potent words
of each language. 


Modeling:

