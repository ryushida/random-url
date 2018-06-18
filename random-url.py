with open('urls.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

print ('[%s]' % ', '.join(map(str, content)))

import webbrowser

webbrowser.open('https://github.com/')