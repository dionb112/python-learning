
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/displayform')
def display_form():
    return render_template('first.html')
@app.route('/processform', methods=['POST'])
def process_form():
    with open('webapp.log', 'a') as logf:
        print(request.form['guesses'], file=logf)
        print('----------------------------', file=logf)
    return render_template('thanks.html',
                            guesses=request.form['guesses'], 
                            the_title='Thanks!')


app.run(debug=True)

with open('./words.txt') as wordsf:
    words0 = wordsf.readlines()
# or don't convert it back to list if just iterating (save memory)
words = list(map(lambda each:each.strip('\n'), words0))
print(words[0])

