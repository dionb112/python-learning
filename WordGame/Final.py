#!/usr/bin/env python
# coding: utf-8

# In[12]:


from random import randrange

with open('./words.txt') as wordsf:
    words0 = wordsf.readlines()
# convert it to list() if printing, here just iterating (so save memory)
words = (map(lambda each:each.strip('\n'), words0))

# two helper functions from xword
def suggest(hint_string):
    """Take the hint_string and return the possible words."""
    n_letters = len(hint_string)
    known_letters = {}
    for n, letter in enumerate(hint_string.lower()):
        if letter != '-':
            known_letters[n+1] = letter
    return find_words(n_letters, known_letters)
def find_words(length, letters):
    """Find words of a certain length which contain
       the specified positional letters."""
    results = set()
    for w in words:
        w = w.lower().strip()
        if len(w) == length:
            got_one = True
            for loc, let in letters.items():
                if w[loc-1] != let:
                    got_one = False
            if got_one:
                results.add(w)
    return sorted(results)

# using: sortedwords = sorted(words, key=len)
#        print("The longest word in the list is: %s." % (sortedwords[-1],))
# Ensures at least one valid word (I can see the longest length word in the list is 23 chars (include '))
size = randrange(6,23)
source_word = "".join('-' for i in range(size))
results = suggest(source_word)
# get length of results and pick an element with random choice from 0 to length - 1
source_word = results[randrange(0,len(results) - 1)]


# In[ ]:


from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/displayform')
def display_form():
    return render_template('first.html', source_word=source_word)
@app.route('/processform', methods=['POST'])
def process_form():
    with open('webapp.log', 'a') as logf:
        print(request.form['guesses'], file=logf)
        print('----------------------------', file=logf)
    return render_template('thanks.html',
                            guesses=request.form['guesses'], 
                            the_title='Thanks!')
app.run(debug=True)


# In[ ]:




