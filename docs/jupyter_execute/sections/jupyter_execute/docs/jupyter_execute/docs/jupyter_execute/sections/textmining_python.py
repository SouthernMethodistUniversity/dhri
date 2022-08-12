#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Introduction-to-Natural-Language-Processing-with-Python" data-toc-modified-id="Introduction-to-Natural-Language-Processing-with-Python-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to Natural Language Processing with Python</a></div><div class="lev1 toc-item"><a href="#Intro-to-Python-Basics" data-toc-modified-id="Intro-to-Python-Basics-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Intro to Python Basics</a></div><div class="lev2 toc-item"><a href="#Operating-this-notebook" data-toc-modified-id="Operating-this-notebook-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Operating this notebook</a></div><div class="lev3 toc-item"><a href="#Basic-Math" data-toc-modified-id="Basic-Math-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Basic Math</a></div><div class="lev2 toc-item"><a href="#Variables-and-Objects" data-toc-modified-id="Variables-and-Objects-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Variables and Objects</a></div><div class="lev3 toc-item"><a href="#Dictionaries" data-toc-modified-id="Dictionaries-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Dictionaries</a></div><div class="lev2 toc-item"><a href="#Loops-and-Functions" data-toc-modified-id="Loops-and-Functions-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Loops and Functions</a></div><div class="lev3 toc-item"><a href="#Loops" data-toc-modified-id="Loops-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Loops</a></div><div class="lev3 toc-item"><a href="#Functions" data-toc-modified-id="Functions-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Functions</a></div><div class="lev2 toc-item"><a href="#DataFrames-and-Pandas" data-toc-modified-id="DataFrames-and-Pandas-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>DataFrames and Pandas</a></div><div class="lev2 toc-item"><a href="#Plotting" data-toc-modified-id="Plotting-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Plotting</a></div><div class="lev1 toc-item"><a href="#Text-Mining-Basics" data-toc-modified-id="Text-Mining-Basics-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Text Mining Basics</a></div><div class="lev2 toc-item"><a href="#Setup" data-toc-modified-id="Setup-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Setup</a></div><div class="lev2 toc-item"><a href="#Counting-Words-and-Characters" data-toc-modified-id="Counting-Words-and-Characters-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Counting Words and Characters</a></div><div class="lev3 toc-item"><a href="#Count-Stopwords" data-toc-modified-id="Count-Stopwords-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Count Stopwords</a></div><div class="lev3 toc-item"><a href="#Other-Ways-to-Count" data-toc-modified-id="Other-Ways-to-Count-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Other Ways to Count</a></div><div class="lev4 toc-item"><a href="#Counting-Special-Characters" data-toc-modified-id="Counting-Special-Characters-3.2.2.1"><span class="toc-item-num">3.2.2.1&nbsp;&nbsp;</span>Counting Special Characters</a></div><div class="lev4 toc-item"><a href="#Counting-Numbers" data-toc-modified-id="Counting-Numbers-3.2.2.2"><span class="toc-item-num">3.2.2.2&nbsp;&nbsp;</span>Counting Numbers</a></div><div class="lev4 toc-item"><a href="#Counting-Uppercase" data-toc-modified-id="Counting-Uppercase-3.2.2.3"><span class="toc-item-num">3.2.2.3&nbsp;&nbsp;</span>Counting Uppercase</a></div><div class="lev1 toc-item"><a href="#Processing-Text" data-toc-modified-id="Processing-Text-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Processing Text</a></div><div class="lev2 toc-item"><a href="#Cleaning-Up-Words" data-toc-modified-id="Cleaning-Up-Words-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Cleaning Up Words</a></div><div class="lev3 toc-item"><a href="#Lowercase" data-toc-modified-id="Lowercase-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Lowercase</a></div><div class="lev3 toc-item"><a href="#Remove-Punctuation" data-toc-modified-id="Remove-Punctuation-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Remove Punctuation</a></div><div class="lev3 toc-item"><a href="#Remove-Stopwords" data-toc-modified-id="Remove-Stopwords-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>Remove Stopwords</a></div><div class="lev3 toc-item"><a href="#Remove-Frequent-Words" data-toc-modified-id="Remove-Frequent-Words-4.1.4"><span class="toc-item-num">4.1.4&nbsp;&nbsp;</span>Remove Frequent Words</a></div><div class="lev3 toc-item"><a href="#Remove-Rare-Words" data-toc-modified-id="Remove-Rare-Words-4.1.5"><span class="toc-item-num">4.1.5&nbsp;&nbsp;</span>Remove Rare Words</a></div><div class="lev3 toc-item"><a href="#Correct-Spelling" data-toc-modified-id="Correct-Spelling-4.1.6"><span class="toc-item-num">4.1.6&nbsp;&nbsp;</span>Correct Spelling</a></div><div class="lev3 toc-item"><a href="#Tokenization" data-toc-modified-id="Tokenization-4.1.7"><span class="toc-item-num">4.1.7&nbsp;&nbsp;</span>Tokenization</a></div><div class="lev2 toc-item"><a href="#Stemming" data-toc-modified-id="Stemming-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Stemming</a></div><div class="lev2 toc-item"><a href="#Lemmatization" data-toc-modified-id="Lemmatization-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Lemmatization</a></div><div class="lev1 toc-item"><a href="#Advanced-Text-Processing" data-toc-modified-id="Advanced-Text-Processing-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Advanced Text Processing</a></div><div class="lev2 toc-item"><a href="#N-grams" data-toc-modified-id="N-grams-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>N-grams</a></div><div class="lev2 toc-item"><a href="#Term-Frequency" data-toc-modified-id="Term-Frequency-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Term Frequency</a></div><div class="lev2 toc-item"><a href="#Inverse-Document-Frequency" data-toc-modified-id="Inverse-Document-Frequency-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Inverse Document Frequency</a></div><div class="lev2 toc-item"><a href="#Term-Frequency-–-Inverse-Document-Frequency-(TF-IDF)" data-toc-modified-id="Term-Frequency-–-Inverse-Document-Frequency-(TF-IDF)-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Term Frequency – Inverse Document Frequency (<a href="https://en.wikipedia.org/wiki/Tf%E2%80%93idf" target="_blank">TF-IDF</a>)</a></div><div class="lev2 toc-item"><a href="#Bag-of-Words" data-toc-modified-id="Bag-of-Words-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span><a href="https://en.wikipedia.org/wiki/Bag-of-words_model" target="_blank">Bag of Words</a></a></div><div class="lev2 toc-item"><a href="#Sentiment-Analysis" data-toc-modified-id="Sentiment-Analysis-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Sentiment Analysis</a></div>

# # Introduction to Natural Language Processing with Python
# 

#  By: Dr. Eric Godat and Dr. Rob Kalescky
#  
#  Edited: Garrett Moore
# 
#  Adapted from: [Ultimate Guide to deal with Text Data (Using Python)](https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/)
#  
#  Natural Language Toolkit: [Documentation](http://www.nltk.org/)
#  
#  Reference Text: [Natural Language Processing with Python](http://www.nltk.org/book/)
#  

# # Intro to Python Basics

# *This section is designed to guide you from having never used Python before to feeling comfortable with basic operations. If you already feel comfortable with this material, feel free to skip to the next section.*
# 
# Python is a programming language capable of just about anything you could want to do. It is designed to be human readable and robust. This particular document is called a Jupyter Notebook. Notebooks are tools for developing Python code and running that code in small steps and see the intermediate results in line.

# ## Operating this notebook

# To operate this notebook, you will need to execute boxes of code, called cells. To do this you can either click the *Run* button on the toolbar or use [Shift]+[Enter].
# 
# Throughout this notebook you will see cells that are not code (like this one). These cells contain text in a language called Markdown. You can execute these cells to render formatted text. A cheatsheet for Markdown can be found [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). There will also be comments with in the code itself that give additional information about the operation of the code, describe functions or show you places where you might want to make changes. These comments are always preceded by an octothorp (#) and in most cases be a different color from the surrounding text.
# 
# Notebooks save automatically, however if you have made big changes your code, you can checkpoint it. This allows you to roll back changes to this point (or any previous checkpoints) should something break in the future.
# 
# There are a few useful [keyboard shortcuts](https://gist.github.com/kidpixo/f4318f8c8143adee5b40) for modifying the cells in a notebook. To use these, click on the far left side of the cell such that the outline changes color (to blue in most cases), press [Enter]] to return to editing the cell's contents.
# 
# -Add a cell **a**bove the current cell   [A]
# 
# -Add a cell **b**elow the current cell   [B]
# 
# -**D**elete the current cell   [D,D]
# 
# **Let's try it out!**

# ### Basic Math

# Python can do simple mathematical operations just like a calculator. Try executing the following cells, then add a cell and have it calculate the sum of the longitude and latitude for SMU in Taos (36.274708,-105.5781171).

# In[1]:


1+1


# In[2]:


2.5-2.0


# ## Variables and Objects

# Calculations are nice but we really want to be able to store our calculations in memory so that we can access them later. We do that by assigning variables. 

# In[3]:


a=2
b=3


# In[4]:


a+b


# Variables can be named just about anything

# In[5]:


pythoniscool=2
SMU=7
lets_text_mine=3


# In[6]:


#Notice that if we assign a value to a variable, our notebook won't return that value to our screen.
#If we want it to show us the value, we can call that variable after it is assigned.
ouranswer = SMU*pythoniscool*lets_text_mine
ouranswer


# So far we have been doing all of our operations on numbers, integers and floats (decimals), but there are other useful objects we can use in Python.
# 
# Strings allow us to store and operate on text data. Strings in Python are surrounded by either single quotes '' or double quotes "".

# In[7]:


ourstring = "Here is a string in Python!"
ourstring


# Uncomment the next cell and try making a string of your own.

# In[8]:


#mystring = <put your string here>
#mystring


# If we later want to see the value stored in a variable we can always use the built in **print** function

# In[9]:


print(ourstring)


# What if we want to have multiple strings stored at once but we don't want to assign a bunch of variables? Then we can use a list.
# 
# Lists are enclosed by brackets [] and separated by commas.

# In[10]:


ourlist = ['This', 'is', "a", "list", 'of', "strings"]


# In[11]:


print(ourlist)


# To access individual elements in a list you call it by its reference number.
# 
# *__Note:__ In Python, counting starts with 0. Thus in the list [a,b,c], a is the 0th element and c is the 2nd*

# In[12]:


first = ourlist[0]


# In[13]:


# Notice we can call the last element by using a negative reference number. This lets us see the end without knowing how long the list is.
last = ourlist[-1]


# In[14]:


print(first,last)


# In[15]:


# If we did want to know the length of our list we can use the len() function
len(ourlist)


# Try making a list and printing the 2nd element from your list. Make sure to remove the #'s for comments.

# In[16]:


#mylist=
#
#


# ### Dictionaries

# Dictionaries are a different way of storing data than lists. They rely on a key and value system as opposed to the order of the entries.
# 
# Dictionaries are enclosed in curly braces {}, the key and value are separated by a colon : and entries are separated by commas ,
# 
# Values can then be accessed by referencing the key.
# 
# Note that finding dictionary values does not go both ways, so using the value to find the key will cause an error.

# In[17]:


ourdictionary = {"Dallas":1341000,"Plano":286143,"Taos":5668}
ourdictionary


# In[18]:


ourdictionary["Taos"] 
#NOTE: ourdictionary[5668] will NOT give you "Taos", but an error.


# Below are the word counts for the *Lord of the Rings* books ([citation](http://lotrproject.com/statistics/books/wordscount)). Can you build a dictionary of the information and then calculate the difference between the *Fellowship of the Ring* and *The Hobbit* and the total number of words for books in the *Lord of the Rings* Trilogy?  Try adding a cell below this one, then compare your answer to the one below!
# 
# |__Book__|__Word Count__|
# |---|---|
# |The Silmarillion|130115|
# |The Hobbit|95356|
# |The Fellowship of the Ring|187790|
# |The Two Towers|156198|
# |The Return of the King|137115|

# In[19]:


# Here is the code answer for writing the dictionary

tolkien = {"The Silmarillion":130115,"The Hobbit":95356,"The Fellowship of the Ring":187790, "The Two Towers":156198, "The Return of the King":137115}

bilbo=tolkien["The Hobbit"]

frodo=tolkien["The Fellowship of the Ring"]

print("The Fellowship of the Ring - The Hobbit")

print(frodo-bilbo)

print("Total Words for the Lord of the Rings Trilogy")

print(tolkien["The Fellowship of the Ring"]+tolkien["The Two Towers"]+tolkien["The Return of the King"])


# ## Loops and Functions

# Computers are much better at doing simple repeatable tasks than humans are so to leverage this advantage, we will cover two different ways of writing these kind of repeatable instructions.

# ### Loops

# Loops are a way of having Python complete a task over and over.
# 
# The most common form if a **for** loop. A **for** loop completes a task a fixed number of times by iterating a variable over the members of a sequence in order.

# In[20]:


#Example for loop
for i in [0,1,2]:
    print(i)


# **Note**: The indention is important, it tells Python that the line *print(i)* belongs inside the loop.

# ### Functions

# Sometimes it would be nice to be able to save a group of instructions in a single block, that way we won't need to rewrite several lines of code each time we want to do that set of operations.
# 
# To do this we define a **function**.
# 
# Functions allow us to define a more complicated set of instructions as a single entity and call that entire block of code directly.
# 
# Functions are defined (*def*), named (lowercase is a standard practice) and accept arguments (). They then can return a value if needed (*return*).
# 
# Python has several built in functions (*print()* is a good example) and when you combine external packages and libraries, there are functions for just about everything you could think of.

# In[21]:


# Example function
def square_me(n):
    return n*n


# In[22]:


square_me(4)


# Try defining your own function that takes 2 arguments and adds them together.

# In[23]:


#def add_me
#
#


# In[24]:


#add_me(7,11)


# Putting loops and functions together is where python can become very powerful.

# In[25]:


# Looping over a function
for i in [0,1,2,3]:
    print(square_me(i)) # note that this is still tabbed in within the for loop


# In[26]:


# A function with a loop
def print_numbers(start,stop):
    for i in range(start,stop): #Here the range() function gives us all the values from start up to but excluding the stop value
        print(i) # this is indented twice, so Python knows it is within the loop within the function


# In[27]:


print_numbers(0,4)


# # Libraries

# Libraries are pre-written chunks of code designed to be integrated into projects for a specific purpose.  The idea is to keep people from having to reinvent the wheel every time they want to write a program.  When we encounter situations where a libary might be useful, we use the keyword *import* to tell the program that we want to use this pre-existing code.  As an example, in the next section you will use a library called Pandas which helps visualize data and make it easier to digest, which is very useful for us.  Because of this, we will import that code into this program simply by running the cell with the import that goes with that code.  Here is what you will see, only in commented code.

# In[28]:


#import pandas as pd

#by using the keyword *as* and giving pandas an alternative name (pd) in this program, it allows us to use the
#functions within pandas while only having to type our pd instead of pandas every time.


# Most programming languages have libraries that allow you to import code this way, and it will save you a lot of time and allow you to quickly use many new functions that are highly polished.

# # DataFrames and Pandas

# Now it is time to use what we have learned to start doing some data science.
# 
# Pandas is the name of a library in which there are functions and tools for doing operations common in data analysis and data science. One particularly great feature is the DataFrame structure which allows us to work with an object similar to an Excel spreadsheet but with the flexibility and power of Python behind it.
# 
# First we will need to import the Pandas library and create a DataFrame. DataFrames are can also be created when you import files (like CSV's) or tables from a database (like SQL).

# In[29]:


import pandas as pd


# In[30]:


#Notice here the data is a dictionary, similar to the one we used above but with the titles and wordcounts as nested lists
d = {"Books":["The Silmarillion","The Hobbit","The Fellowship of the Ring","The Two Towers","The Return of the King"],
     "Words":[130115,95356,187790,156198,137115]}
df = pd.DataFrame(d)
df


# Now we can operate on entire rows or columns in our DataFrame.

# In[31]:


df["Books"] #Selecting the column "Books"


# In[32]:


df[:2] #Selecting the first 2 rows


# In[33]:


df[2:4] #Selecting rows 2 up to 4


# In[34]:


df["Words"][2:4] #Selecting the second and third row from the "Words" column.


# In[35]:


df[2:4]["Words"] #Same result but from the opposite order


# You can also operate on entire columns in your DataFrame. Just be careful because this can give you unexpected results. Rows are generally more consistent for elements within a DataFrame.

# In[36]:


total = sum(df["Words"])
total


# ## Plotting

# Visualizing data is incredibly important when trying to convey findings. There are several libraries available for doing data visualization. Pandas has some built in plotting functionality, but we have provided access to MatPlotLib, Plotly and Seaborn as well.

# In[37]:


# This is only needed in this case because we wanted to show the names of the books. You could make a similar plot in Pandas.
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
# This allows the plot to be shown inline in the notebook


# In[38]:


plot = df.plot(kind='bar') # we are setting the type of plot to a bar graph
plot.set_xticklabels(df['Books']); #This lets us rename the x axis labels


# That concludes our tutorial for basic Python.
# 
# As you proceed forward, the remainder of this notebook is focused on mining text data.

# # Text Mining Basics

# ## Setup

# These are the basic libraries we will use in for data manipulation (pandas) and math functions (numpy). We will add more libraries as we need them.
# 
# As a best practice, it is a good idea to load all your libraries in a single cell at the top of a notebook, however for the purposes of this tutorial we will load them as we go.

# In[39]:


import pandas as pd
import numpy as np


# Load a data file into a pandas DataFrame.
# 
# This tutorial was designed around using sets of data you have yourselves in a form like a CSV, TSV, or TXT file.  Feel free to use any set of data, but for now we will use a dataset created from scraping this [Multilingual Folktale Database](http://www.mftd.org/).
# 
# This file is a CSV filetype, common for text data, but your data may also be stored as TSV's, TXT's, or other file types.  This will slightly change how you read from Pandas, but the concept is largely the same for the different filetypes.  Just keep this in mind when you see references to CSV.
# 
# To proceed, you will need to have this file downloaded and in the same folder as this notebook. Alternatively you can put the full path to the file.  Typically, your program will look for the file with the name you specified in the folder that contains your program unless you give the program a path to follow.

# In[40]:


import glob
glob.glob("*.csv") #Allows us to check the files in the current directory, if folktales.csv is not here, then we need to give the path


# In[41]:


filename = 'folktales.csv' #If you need to put the path to the file, do so here.
data = pd.read_csv(filename)#if your filetype is not CSV, you may need to add " , sep = 'separating_character_here' " after the filename.  This may require extra manipulation, so be careful.
#an alternative, depending on your filetype and situation, may be read_table as opposed to read_csv
data.head() # We will use the .head() attribute to limit the amount of the DataFrame is displayed on screen. It is not necessary for computation.


# Here we can see all the information available to us from the file in the form of a Pandas DataFrame. For the remainder of this tutorial, we will focus primarily on the full text of each data chunk, which we will name the *Story* column.  With your data set this is likely to be something very different, so feel free to call is something else.

# ## Counting Words and Characters

# The first bit of analysis we might want to do is to count the number of words in one piece of data. To do this we will add a column called *wordcount* and write an operation that applies a function to every row of the column.
# 
# Unpacking this piece of code, *len(str(x).split(" ")*, tells us what is happening.
# 
# For the content of cell *x*, convert it to a string, *str()*, then split that string into pieces at each space, *split()*.
# 
# The result of that is a list of all the words in the text and then we can count the length of that list, *len()*.

# In[42]:


data['wordcount'] = data['Story'].apply(lambda x: len(str(x).split(" ")))
data[['Story','wordcount']].head()


# We can do something similar to count the number of characters in the data chunk, including spaces. If you wanted to exclude whitespaces, you could take the list we made above, join it together and count the length of the resulting string.

# In[43]:


data = data.fillna("No Information Provided") #If some of our data is missing, this will replace the blank entries. This is only necessary in some cases


# In[44]:


data['char_count'] = data['Story'].str.len() ## this also includes spaces, to do it without spaces, you could use something like this: "".join()
data[['Story','char_count']].head()


# Now we want to calculate the average word length in the data.
# 
# Let's define a function that will do that for us:

# In[45]:


def avg_word(sentence):
    words = sentence.split()
    return (sum(len(word) for word in words)/len(words))


# We can now apply that function to all the data chunks and save that in a new column.

# In[46]:


data['avg_word'] = data['Story'].apply(lambda x: avg_word(x))
data[['Story','avg_word']].head()


# We can then sort by the average word length.

# In[47]:


data[['Story','avg_word']].sort_values(by='avg_word', ascending=True).head()


# ### Count Stopwords

# Stopwords are words that are commonly used and do little to aid in the understanding of the content of a text. There is no universal list of stopwords and they vary on the style, time period and media from which your text came from.  Typically, people choose to remove stopwords from their data, as it adds extra clutter while the words themselves provide little to no insight as to the nature of the data.  For now, we are simply going to count them to get an idea of how many there are.
# 
# For this tutorial, we will use the standard list of stopwords provided by the Natural Language Toolkit python library.

# In[48]:


#import nltk
#nltk.download('stopwords')


# In[49]:


from nltk.corpus import stopwords
stop = stopwords.words('english')


# To count the number of stopwords in a chunk of data, we make a list of all the words in our data that are also in the stopword list. We can then just take the length of that list and store it in a new column

# In[50]:


data['stopwords'] = data['Story'].apply(lambda x: len([x for x in x.split() if x in stop]))
data[['Story','stopwords']].head()


# ### Other Ways to Count

# There are other types of counting we might want to do. These might be more or less relevant depending on the test you are working with.
# 
# For completeness, we have put them here but we will skip over them in this tutorial

# #### Counting Special Characters

# This is really only useful for Twitter or other Internet texts but you could imagine wanting to count quotations or exclamations with something similar.

# In[51]:


data['special_char'] = data['Story'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
data[['Story','special_char']].head()


# #### Counting Numbers

# This counts the number of numerical digits in a text, which for strict text may not be helpful, but mostly numerical data will make more use of this.

# In[52]:


data['numerics'] = data['Story'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
data[['Story','numerics']].sort_values(by='numerics', ascending=False).head()


# #### Counting Uppercase

# Counting uppercase words could give us an indication of how many sentences or proper nouns are in a text but this is likely too broad to be used to classify either on its own.

# In[53]:


data['upper'] = data['Story'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
data[['Story','upper']].head()


# # Processing Text

# A major component of doing analysis on text is the cleaning of the text prior to the analysis.
# 
# Though this process destroys some elements of the text (sentence structure, for example), it is often necessary in order to describe a text analytically. Depending on your choice of cleaning techniques, some elements might be preserved better than others if that is of importance to your analysis.

# ## Cleaning Up Words

# This series of steps aims to clean up and standardize the text itself. This generally consists of removing common elements such as stopwords and punctuation but can be expanded to more detailed removals.

# ### Lowercase

# Here we enforce that all of the text is lowercase. This makes it easier to match cases and sort words.
# 
# Notice we are assigning our modified column back to itself. This will save our modifications to our DataFrame

# In[54]:


data['Story'] = data['Story'].apply(lambda x: " ".join(x.lower() for x in x.split()))
data['Story'].head()


# ### Remove Punctuation

# Here we remove all punctuation from the data. This allows us to focus on the words only as well as assist in matching.

# In[55]:


data['Story'] = data['Story'].str.replace('[^\w\s]','')
data['Story'].head()


# ### Remove Stopwords

# Similar to what we did earlier when we counted stopwords, we now want to remove the stopwords. We will again use the NLTK list of stopwords but this time keep a list of words that do not appear in the list of stopwords.

# In[56]:


from nltk.corpus import stopwords
stop = stopwords.words('english')
stop.append("come")


# In[57]:


data['Story'] = data['Story'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
data['Story'].head()


# ### Remove Frequent Words

# If we want to catch common words that might have slipped through the stopword removal, we can build out a list of the most common words remaining in our text.
# 
# Here we have built a list of the 10 most common words. Some of these words might actually be relevant to our analysis so it is important to be careful with this method.

# In[58]:


freq = pd.Series(' '.join(data['Story']).split()).value_counts()[:10]
freq


# We now follow the same procedure with which we removed stopwords to remove the most frequent words.

# In[59]:


freq = list(freq.index)
data['Story'] = data['Story'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
data['Story'].head()


# ### Remove Rare Words

# By analogy, we can remove the most rare words. Some of these are strange misspellings or [hapax legomenon](https://en.wikipedia.org/wiki/Hapax_legomenon) (one off words that don't appear anywhere else in the text).

# In[60]:


freq = pd.Series(' '.join(data['Story']).split()).value_counts()[-10:]
freq


# Again, removing words following the same process as the stopword removal.

# In[61]:


freq = list(freq.index)
data['Story'] = data['Story'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
data['Story'].head()


# ### Correct Spelling

# Misspellings can cause inaccuracies in text analysis. For example, "the" and "teh" are likely intended to be the same word and a reader might gloss over that typo, but a computer would view them as distinct.
# 
# To help address this we will leverage the [TextBlob package](https://textblob.readthedocs.io/en/dev/) to check the spelling.
# 
# Since this can be slow and often of questionable usefulness, we have limited the check to the first 5 rows of our DataFrame.
# 
# It is also worth keeping in mind that, much like autocorrect on your phone, the spellchecking here is not going to be perfectly accurate and could result in just as many errors as it fixes (especially if you are working on text from edited or published sources).

# In[62]:


from textblob import TextBlob
data['Story'][:5].apply(lambda x: str(TextBlob(x).correct()))


# ### Tokenization

# Tokenization is the process of splitting up a block of text into a sequence of words or sentences.
# 
# For those familiar with R and the Tidyverse, this would be referred to as unnesting tokens
# 
# Here we show all the tokenized words from the first data chunk in our Dataframe.

# In[63]:


#import nltk
#nltk.download('punkt')


# In[64]:


TextBlob(data['Story'][0]).words


# ## Stemming

# Stemming is the process of removing suffices, like "ed" or "ing".
# 
# We will use another standard NLTK package, PorterStemmer, to do the stemming.

# In[65]:


from nltk.stem import PorterStemmer
st = PorterStemmer()
data['Story'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))


# As we can see "wonderful" became "wonder", which could help an analysis, but "deathbed" became "deathb" which is less helpful.

# ## Lemmatization

# Lemmatization is often a more useful approach than stemming because it leverages an understanding of the word itself to convert the word back to its root word. However, this means lemmatization is less aggressive than stemming (probably a good thing).

# In[66]:


#import nltk
#nltk.download('wordnet')


# In[67]:


from textblob import Word
data['Story'] = data['Story'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
data['Story'].head()


# At this point we have a several options for cleaning and structuring our text data. The next section will focus on more advanced ways to study text analytically.

# # Advanced Text Processing

# This section focuses on more complex methods of analyzing textual data. We will continue to work with our same DataFrame.

# ## N-grams

# N-grams are combinations of multiple words as they appear in the text. The N refers to the number of words captured in the list. N-grams with N=1 are referred unigrams and are just a nested list of all the words in the text. Following a similar pattern, bigrams (N=2), trigrams (N=3), etc. can be used.
# 
# N-grams allow you to capture the structure of the text which can be very useful. For instance, counting the number of bigrams where "said" was preceded by "he" vs "she" could give you an idea of the gender breakdown of speakers in a text. However, if you make your N-grams too long, you lose the ability to make comparisons.
# 
# Another concern, especially in very large data sets, is that the memory storage of N-grams scales with N (bigrams are twice as large as unigrams, for example) and the time to process the N-grams can balloon dramatically as well.
# 
# All that being said, we would suggest focusing on bigrams and trigrams as useful analysis tools.

# In[68]:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
n_grams = TextBlob(data['Story'][1]).ngrams(2)


# In[69]:


characters=[]
for i in ['wolf', 'mouse', 'rabbit', 'children']:
     characters.append(lemmatizer.lemmatize(i))


# In[70]:


for n in n_grams:
    if n[1] in characters:
        print(n)


# In[71]:


from nltk import ngrams
from collections import Counter

ngram_counts = Counter(ngrams(data['Story'][1].split(), 2))
for n in ngram_counts.most_common(10):
    print(n)


# ## Term Frequency

# Term Frequency is a measure of how often a term appears in a document. There are different ways to define this but the simplest is a raw count of the number of times each term appears.
# 
# There are other ways of defining this including a true term frequency and a log scaled definition. All three have been implemented below but the default will the raw count definition, as it matches with the remainder of the definitions in this tutorial.
# 
# |Definition|Formula|
# |---|---|
# |Raw Count|$$f_{t,d}$$|
# |Term Frequency|$$\frac{f_{t,d}}{\sum_{t'\in d}f_{t',d}}$$|
# |Log Scaled|$$\log(1+f_{t,d})$$|
# 
# 

# In[72]:


## Raw Count Definition
tf1 = (data['Story'][0:5]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()

## Term Frequency Definition
#tf1 = (data['Story'][0:5]).apply(lambda x: (pd.value_counts(x.split(" ")))/len(x.split(" "))).sum(axis = 0).reset_index() 

## Log Scaled Definition
#tf1 = (data['Story'][0:10]).apply(lambda x: 1.0+np.log(pd.value_counts(x.split(" ")))).sum(axis = 0).reset_index() 

tf1.columns = ['words','tf']
tf1.sort_values(by='tf', ascending=False)[:10]


# ## Inverse Document Frequency

# Inverse Document Frequency is a measure of how common or rare a term is across multiple documents. That gives a measure of how much weight that term carries.
# 
# For a more concrete analogy of this, imagine a room full of NBA players; here a 7 foot tall person wouldn't be all that shocking. However if you have a room full of kindergarten students, a 7 foot tall person would be a huge surprise.
# 
# The simplest and standard definition of Inverse Document Frequency is to take the logarithm of the ratio of the number of documents containing a term to the total number of documents.
# 
# $$-\log\frac{n_t}{N} = \log\frac{N}{n_t}$$
# 

# In[73]:


for i,word in enumerate(tf1['words']):
    tf1.loc[i, 'idf'] = np.log(data.shape[0]/(len(data[data['Story'].str.contains(word)])))

tf1[:10]


# ## Term Frequency – Inverse Document Frequency ([TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf))

# Term Frequency – Inverse Document Frequency (TF-IDF) is a composite measure of both Term Frequency and Inverse Document Frequency.
# 
# From [Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf):
# "A high weight in TF–IDF is reached by a high term frequency (in the given document) and a low document frequency of the term in the whole collection of documents; the weights hence tend to filter out common terms"
# 
# More concisely, a high TD-IDF says that a word is very important in the documents in which it appears.
# 
# There are a few weighting schemes for TF-IDF. Here we use scheme (1).
# 
# |Weighting Scheme|Document Term Weight|
# |---|---|
# |(1)|$$f_{t,d}\cdot\log\frac{N}{n_t}$$|
# |(2)|$$1+\log(f_{t,d})$$|
# |(3)|$$(1+\log(f_{t,d}))\cdot\log\frac{N}{n_t}$$|

# In[74]:


tf1['tfidf'] = tf1['tf'] * tf1['idf']
tf1.sort_values(by='tfidf', ascending=False)[:10]


# It is worth noting that the *sklearn* library has the ability to directly calculate a TD-IDF matrix.

# In[75]:


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',
 stop_words= 'english',ngram_range=(1,1))
data_vect = tfidf.fit_transform(data['Story'])

data_vect


# ## [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model)

# [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) a way to represent text based on the idea that similar texts will contain similar vocabulary. There is a lot to this model and we provide merely a simple implementation of it here.

# In[76]:


from sklearn.feature_extraction.text import CountVectorizer
bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")
data_bow = bow.fit_transform(data['Story'])
data_bow


# ## Sentiment Analysis

# Sentiment is a way of measuring the overall positivity or negativity in a given text.
# 
# To do this we will use the built in sentiment function in the *TextBlob* package. This function will return the polarity and subjectivity scores for each data chunk.

# In[77]:


data['Story'][:5].apply(lambda x: TextBlob(x).sentiment)


# Focusing on the polarity score, we are able to see the overall sentiment of each data chunk. The closer to 1 the more positive and the closer to -1 the more negative.

# In[78]:


data['sentiment'] = data['Story'].apply(lambda x: TextBlob(x).sentiment[0] )
data[['Story','sentiment']].head()


# Here we have textted the sentiment scores for the first 10 chunks.
# 
# Notice they tend to be positive but not exceedingly so.

# In[79]:


plot_1 = data[['sentiment']][:10].plot(kind='bar')


# Now we have sorted and textted all of the sentiment scores for the chunks in our database.
# 
# We can clearly see that most of the text data is positive but not overwhelmingly so (as seen by the long tail of the distribution). However, the parts that are negative tend to be more polarized than the positive ones (a shorter tail and sharper peak).

# In[80]:


plot_2 = data[['sentiment']].sort_values(by='sentiment', ascending=False).plot(kind='bar')


# ## Using TF-IDF and Machine Learning

# This is significantly more advanced than the rest of the tutorial. This takes the TF-IDF matrix and applies a [k-means clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering). This groups the texts into clusters of similar terms from the TF-IDF matrix. This algorithm randomly seeds X "means", the values are then clustered into the nearest mean. The centroid of the values in each cluster then becomes the new mean and the process repeats until a convergence is reached.

# In[81]:


import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

groups = 10

num_clusters = groups
num_seeds = groups
max_iterations = 300
labels_color_map = {
    0: '#20b2aa', 1: '#ff7373', 2: '#ffe4e1', 3: '#005073', 4: '#4d0404',
    5: '#ccc0ba', 6: '#4700f9', 7: '#f6f900', 8: '#00f91d', 9: '#da8c49'
}
pca_num_components = 2
tsne_num_components = 2

# calculate tf-idf of texts
tfidf = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',stop_words= 'english',ngram_range=(1,1))
tf_idf_matrix = tfidf.fit_transform(data['Story'])

# create k-means model with custom config
clustering_model = KMeans(
    n_clusters=num_clusters,
    max_iter=max_iterations,
    precompute_distances="auto",
    n_jobs=-1
)

labels = clustering_model.fit_predict(tf_idf_matrix)
#print(labels)

X = tf_idf_matrix.todense()

# ----------------------------------------------------------------------------------------------------------------------

reduced_data = PCA(n_components=pca_num_components).fit_transform(X)
# print(reduced_data)

import matplotlib.patches as mpatches
legendlist=[mpatches.Patch(color=labels_color_map[key],label=str(key))for key in labels_color_map.keys()]

fig, ax = plt.subplots()
for index, instance in enumerate(reduced_data):
    #print(instance, index, labels[index])
    pca_comp_1, pca_comp_2 = reduced_data[index]
    color = labels_color_map[labels[index]]
    ax.scatter(pca_comp_1, pca_comp_2, c=color)
plt.legend(handles=legendlist)
plt.show()



# t-SNE plot
#embeddings = TSNE(n_components=tsne_num_components)
#Y = embeddings.fit_transform(X)
#plt.scatter(Y[:, 0], Y[:, 1], cmap=plt.cm.Spectral)
#plt.show()


# In[82]:


tfidf_test = tf1.sort_values(by='tfidf', ascending=False)[:1000]


# In[83]:


title_groups = np.transpose([labels,data['Title'],data['Story Type']])


# These are the titles of the texts in each cluster. Keep in mind that each time you run the algorithm, the randomness in generating the initial means will result in different clusters.

# In[84]:


for i in range(len(title_groups)):
    data.loc[i,'Group'] = title_groups[i][0]


# In[85]:


for i in range(groups):
    print("")
    print("#### {} ###".format(i))
    print("")
    for el in title_groups:
        if el[0]==i:
            print("{}".format(el[1]))


# Now, we are going to make a word cloud based on our data set!

# In[86]:


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
stop_words = set(STOPWORDS)
#stopwords.update([""])


# If you want to update the stopwords after you see the wordcloud, type them into the empty list above and remove the # sign.

# In[ ]:


word = " ".join(data['Story'])
wordcloud = WordCloud(stopwords=stop, background_color="white").generate(word)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# The above code creates a wordcloud based off all the words (except for stop words) in all of the stories. While this can be fun, it may not be as interesting as a wordcloud for a single story. Let's compare:

# In[ ]:


for i in range(0, 5):
    word = data['Story'][i]
    wordcloud = WordCloud(stopwords=stop, background_color="white").generate(word)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# 
