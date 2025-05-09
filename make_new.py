from os import listdir
from os.path import isfile, join

def persian_to_latin_numbers(text):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    latin_digits = '0123456789'
    translation_table = str.maketrans(persian_digits, latin_digits)
    return text.translate(translation_table)

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
      translations[d0.strip()] = d1.strip()


mypath = '../travel-in-books.github.io/_posts'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
output_path = '_posts'

for filepath in onlyfiles:
  print(filepath)
  if 'template.md' in filepath:
    continue
  mytitle = ' '.join(filepath.split('-')[3:])[:-3]
  categories = set()
  tags = set()
  mycountry = None
  mygenre = None
  with open(join(mypath,filepath),"r") as f:
      data = f.read().split("\n")
      for d in data:
        if "categories" in d:
          for cat in d[d.index("[") +1:d.index("]")].split(","):
            categories.add(cat)
        
        if "tags" in d:
          for tag in d[d.index("[") +1:d.index("]")].split(","):
            tags.add(tag)

        if "سال چاپ" in d:
          myyear = persian_to_latin_numbers(d.split('|')[2].strip())
        
        if "کشور" in d:
          if mycountry is None:
              mycountry = translations[d.split('|')[2].strip()]

        if "ژانر" in d:
          if mygenre is None:
            mygenre = translations[d.split('|')[2].strip()]

      translated_cats = []
      translated_tags = []
      for c in categories:
        translated_cats.append(translations[c.strip()])

      for t in tags:
        if t.strip() in translations:
          if not translations[t.strip()].isnumeric():
            translated_tags.append(translations[t.strip()])

      mycategories = '[' + ','.join(translated_cats) + ']'
      mytags = '[' + ','.join(translated_tags) + ']'

      if 'short-stories' in filepath:
          mycategories = '[Short Stories,Fiction]'
          mytags = '[short stories,fiction]'

      with open(join(output_path,filepath),"w") as f:
        str = """---
title: {title}
categories: {categories}
tags: {tags}
---""".format(title=mytitle,categories=mycategories,tags=mytags)

        str += """
        
| Title | {title} |
| Author | {author}  |
| Publication Date | {year}   |
| Country | {country} |
| Genre | {genre}  |
        """.format(title=mytitle[0:mytitle.index("by")],author=mytitle[mytitle.index("by")+2:],year=myyear,country=mycountry,genre=mygenre)
        f.write(str)
      
      