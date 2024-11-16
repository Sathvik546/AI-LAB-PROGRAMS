#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[31]:


nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt')
text="""Hello Mr.Smith, How are you doing today? The weather is great and city is awesome.the sky is pinkish-blue. You should'nt eat cardboard"""


# In[6]:


sent=nltk.sent_tokenize(text)
print(sent)


# In[7]:


import re
#text="saaaaMMM"
print(text.lower())
text = re.sub(r"[^a-z\'A-Z]", " ",text.lower())
text


# In[9]:


words= text.split()
print(words)


# In[11]:


from nltk.corpus import stopwords
print(stopwords.words("english"))


# In[20]:


words = [w for w in words if w not in stopwords.words("english")]
print (words)


# In[22]:


from nltk.stem.porter import PorterStemmer
stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)


# In[25]:


from nltk.stem.wordnet import WordNetLemmatizer
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)


# In[37]:


from nltk import pos_tag,RegexpParser

tagged=pos_tag(lemmed)
print(tagged)
for i,(word, tag) in enumerate(tagged):
    if word == "weather":
        tagged[i] = (word, "NN")
    if word =="eat":
        tagged[i] = (word, "VB")
chunker=RegexpParser("""
NP:{}
P:{}
V:{}
PP:{}
VP:{}
""")
output = chunker.parse(tagged)
print("After extracting",output)


# In[36]:


nltk.download('averaged_perceptron_tagger')


# In[ ]:




