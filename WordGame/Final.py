
# coding: utf-8

# In[13]:


from random import choice, random
from flask import Flask, render_template, request, session

with open('./words.txt') as wordsf:
        words0 = wordsf.readlines()
        # don't convert to list if just iterating (save memory)
        words = list(map(lambda each:each.strip('\n'), words0))
        
def get_source_word():
    results = []
    for w in words:
        if (len(w) > 6):
            results.append(w)
    source = choice(results)
    return (source)


# In[ ]:


app = Flask(__name__)
app.secret_key = 'OneSessionToRuleThemAll'
@app.route('/displayform')
def display_form():
    session['source_word'] = get_source_word()
    return render_template('first.html', source_word=session['source_word'])
@app.route('/processform', methods=['POST'])
def process_form():
    with open('webapp.log', 'a') as logf:
        print(request.form['guesses'], file=logf)
        print('----------------------------', file=logf)
    return render_template('thanks.html',
                            guesses=request.form['guesses'], 
                            the_title='Thanks!')
app.run(debug=True)

