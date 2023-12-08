Flask directory listing
dirtree.html
<!doctype html>
<title>Path: {{ tree.name }}</title>
<h1>{{ tree.name }}</h1>
<ul>
{%- for item in tree.children recursive %}
    <li>{{ item.name }}
    {%- if item.children -%}
        <ul>{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>
dirtree.py
def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree


import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dirtree():
    path = os.path.expanduser(u'~')
    return render_template('dirtree.html', tree=make_tree(path))

if __name__=="__main__":
    app.run(host='localhost', port=8888, debug=True)
