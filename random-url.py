with open('urls.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

print ('[%s]' % ', '.join(map(str, content)))

from random import randint
print(randint(0, len(content)-1))

url = content[randint(0, len(content)-1)]
print(url)

import webbrowser

webbrowser.open(url)