# coding: utf-8
Article.objects.create(title='title', content='content')
print(Article(1))
print(Article(1).title)
Article[1]
Article(1).title
get_ipython().run_line_magic('save', '()')
