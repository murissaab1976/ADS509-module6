# %% [markdown]
# # ADS 509 Sentiment Assignment
# 
# This notebook holds the Sentiment Assignment for Module 6 in ADS 509, Applied Text Mining. Work through this notebook, writing code and answering questions where required. 
# 
# In a previous assignment you put together Twitter data and lyrics data on two artists. In this assignment we apply sentiment analysis to those data sets. If, for some reason, you did not complete that previous assignment, data to use for this assignment can be found in the assignment materials section of Blackboard. 
# 

# %% [markdown]
# ## General Assignment Instructions
# 
# These instructions are included in every assignment, to remind you of the coding standards for the class. Feel free to delete this cell after reading it. 
# 
# One sign of mature code is conforming to a style guide. We recommend the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). If you use a different style guide, please include a cell with a link. 
# 
# Your code should be relatively easy-to-read, sensibly commented, and clean. Writing code is a messy process, so please be sure to edit your final submission. Remove any cells that are not needed or parts of cells that contain unnecessary code. Remove inessential `import` statements and make sure that all such statements are moved into the designated cell. 
# 
# Make use of non-code cells for written commentary. These cells should be grammatical and clearly written. In some of these cells you will have questions to answer. The questions will be marked by a "Q:" and will have a corresponding "A:" spot for you. *Make sure to answer every question marked with a `Q:` for full credit.* 
# 

# %%
import os
import re
import emoji
import pandas as pd
import numpy as np

from collections import Counter, defaultdict
from string import punctuation

from nltk.corpus import stopwords

sw = stopwords.words("english")

# %%
# Add any additional import statements you need here




# %%
# change `data_location` to the location of the folder on your machine.
data_location = ""

# These subfolders should still work if you correctly stored the 
# data from the Module 1 assignment
twitter_folder = "twitter/"
lyrics_folder = "lyrics/"

positive_words_file = "positive-words.txt"
negative_words_file = "negative-words.txt"
tidy_text_file = "tidytext_sentiments.txt"

# %% [markdown]
# ## Data Input
# 
# Now read in each of the corpora. For the lyrics data, it may be convenient to store the entire contents of the file to make it easier to inspect the titles individually, as you'll do in the last part of the assignment. In the solution, I stored the lyrics data in a dictionary with two dimensions of keys: artist and song. The value was the file contents. A Pandas data frame would work equally well. 
# 
# For the Twitter data, we only need the description field for this assignment. Feel free all the descriptions read it into a data structure. In the solution, I stored the descriptions as a dictionary of lists, with the key being the artist. 
# 
# 
# 

# %%
# Read in the lyrics data

# %%
# Read in the twitter data

# %%
# Read in the positive and negative words and the
# tidytext sentiment. Store these so that the positive
# words are associated with a score of +1 and negative words
# are associated with a score of -1. You can use a dataframe or a 
# dictionary for this.

# %% [markdown]
# ## Sentiment Analysis on Songs
# 
# In this section, score the sentiment for all the songs for both artists in your data set. Score the sentiment by manually calculating the sentiment using the combined lexicons provided in this repository. 
# 
# After you have calculated these sentiments, answer the questions at the end of this section.
# 

# %%
# your code here

# %% [markdown]
# ### Questions
# 
# Q: Overall, which artist has the higher average sentiment per song? 
# 
# A: <!-- Your answer here -->
# 
# ---
# 
# Q: For your first artist, what are the three songs that have the highest and lowest sentiments? Print the lyrics of those songs to the screen. What do you think is driving the sentiment score? 
# 
# A: <!-- Your answer here -->
# 
# ---
# 
# Q: For your second artist, what are the three songs that have the highest and lowest sentiments? Print the lyrics of those songs to the screen. What do you think is driving the sentiment score? 
# 
# A: <!-- Your answer here -->
# 
# ---
# 
# Q: Plot the distributions of the sentiment scores for both artists. You can use `seaborn` to plot densities or plot histograms in matplotlib.
# 
# 
# 

# %% [markdown]
# ## Sentiment Analysis on Twitter Descriptions
# 
# In this section, define two sets of emojis you designate as positive and negative. Make sure to have at least 10 emojis per set. You can learn about the most popular emojis on Twitter at [the emojitracker](https://emojitracker.com/). 
# 
# Associate your positive emojis with a score of +1, negative with -1. Score the average sentiment of your two artists based on the Twitter descriptions of their followers. The average sentiment can just be the total score divided by number of followers. You do not need to calculate sentiment on non-emoji content for this section.

# %%
# your code here

# %% [markdown]
# Q: What is the average sentiment of your two artists? 
# 
# A: <!-- Your answer here --> 
# 
# ---
# 
# Q: Which positive emoji is the most popular for each artist? Which negative emoji? 
# 
# A: <!-- Your answer here --> 
# 
# 


