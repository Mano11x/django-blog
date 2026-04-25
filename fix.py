content = open('app/templates/app/home.html').read()
search_bar = '<form method=GET action=/search/ style=margin-bottom:2rem><input type=text name=q placeholder=Search...><button type=submit>Search</button></form>'
content = content.replace('<h1>Latest Posts</h1>', '<h1>Latest Posts</h1>' + search_bar)
open('app/templates/app/home.html', 'w').write(content)
print('Done!')
