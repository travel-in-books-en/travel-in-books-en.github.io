from os import listdir
from os.path import isfile, join


def word_to_number(word):
  numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    # Add more as needed
  }

  return numbers.get(word.lower(), "Invalid input")  # Returns the number or an error message


mypath = '_posts'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# categories = set()
# tags = set()
# for filepath in onlyfiles:
#     # print(filepath)
#     with open(join(mypath,filepath),"r") as f:
#       data = f.read().split("\n")
#       # print(data)
#       for d in data:
#         # print(d)
#         if "categories" in d:
#           for cat in d[d.index("[") +1:d.index("]")].split(","):
#             categories.add(cat)
#         if "tags" in d:
#           for tag in d[d.index("[") +1:d.index("]")].split(","):
#             tags.add(tag)
#
# for c in categories:
#   print(c)
# for t in tags:
#   print(t)

translations = {}
with open("translation_map.csv", "r") as f:
  for d in f.read().split("\n"):
    if d != "":
      dd = d.split(",")
      d0 = dd[0].strip()
      d1 = dd[1].strip()
      if "out of" in d1:
        splitd1 = d1.split("out of")[0].strip()
        num_of_10 = word_to_number(splitd1)
        d1 = num_of_10*"⭐" + (10 - num_of_10)*"☆" + " " + str(num_of_10)+"/10"
      #print(d0)
      #print(d1)
      translations[d0.strip()] = d1.strip()

# print(translations)

for filepath in onlyfiles:
    categories = set()
    tags = set()
    with open(join(mypath,filepath),"r") as f:
      data = f.read().split("\n")
      # print(data)
      for d in data:
        # print(d)
        if "categories" in d:
          for cat in d[d.index("[") +1:d.index("]")].split(","):
            categories.add(cat)
        if "tags" in d:
          for tag in d[d.index("[") +1:d.index("]")].split(","):
            tags.add(tag)

    print(categories)
    print(tags)

    translated_cats = []
    translated_tags = []
    for c in categories:
      translated_cats.append(translations[c.strip()])

    for t in tags:
      if t.strip() in translations:
        if not translations[t.strip()].isnumeric():
          translated_tags.append(translations[t.strip()])

    print(translated_cats)

    with open(join(mypath,filepath),"w") as f:
        mytitle = ' '.join(filepath.split('-')[3:])[0:-3].title()
        mycategories = '[' + ','.join(translated_cats) + ']'
        mytags = '[' + ','.join(translated_tags) + ']'
        if 'short-stories' in filepath:
            mycategories = '[Short Stories,Fiction]'
            mytags = '[short stories,fiction]'
        str = """---
title: {title}
categories: {categories}
tags: {tags}
---""".format(title=mytitle,categories=mycategories,tags=mytags)

        str += """
        
| Title | {title} |
| Author | tt  |
| Publication Date | tt   |
| Country | tt |
| Genre | tt  |
        """.format(title=mytitle)
#         print(mytitle, mycategories, mytags)
        f.write(str)
        f.close()
