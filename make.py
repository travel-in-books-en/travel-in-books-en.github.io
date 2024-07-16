from os import listdir
from os.path import isfile, join

mypath = '_posts'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filepath in onlyfiles:
    with open(join(mypath,filepath),"w") as f:
        mytitle = ' '.join(filepath.split('-')[3:])[0:-3].title()
        mycategories = '[Novel,Fiction]'
        mytags = '[novel,japanese,fiction]'
        if 'short-stories' in filepath:
            mycategories = '[Short Stories,Fiction]'
            mytags = '[short stories,fiction]'
        str = """---
title: {title}
categories: {categories}
tags: {tags}
---""".format(title=mytitle,categories=mycategories,tags=mytags)
        
        f.write(str)
         