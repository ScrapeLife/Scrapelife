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

Dependencies

env.py file with github access toke and username

github (.csv)

Multiple .py files to run model and reproduce the report

prep.py, acquire.py

Run through .ipynb

Random states are set as 123 in the notebook

Disclaimer: The assignment called for us to pull the top 100 most forked repos. Our intial investigation showed that the majority of the top 100 were a large majority JavaScript. To provide diversity to our model, we used the top 120 repos of the four languages:(Python, Java, JavaScript, PHP).

**Acquire:**                
Using github's API, we scraped the top 130 repos of the four most popular languages (Python, Java, javaScript, Php).

**Prep:**
Prepared our data with beautiful soup and regex commands to remove excess noise. 

**Exploration:**
We wanted to find the most occuring words unique to each language repos. We used word clouds to see a overview of the most potent words
of each language. 


**Modeling:**
We split the data (words) into a sparse matrix and input that into a decision tree classifier. Using the full word bank (after cleaning and getting rid of words over 11 characters) we used a max depth of 9 to come uop qith our model of predicting the language of the githiub repository.


**Conclusion:**
After exploring and running our model we were able to conclude that the actual language being present in the readme was a factor, but not the main factor. There are words that are unique to each language repositories that favor the targets.

We used two models: decision tree and logistic regression to classify these repositories languages. 

> The Decision Tree Model:  our test accuracy is:  84.6%

> Logistic Regression Model:  our test accuracy is:  91.5%


We believe the logistic regression model perfomred better because it gave more weight to the unique words in each class (language)
