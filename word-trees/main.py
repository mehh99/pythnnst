import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "I love python Coding because Python is easy to learn and simple"

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Tree')
plt.show()