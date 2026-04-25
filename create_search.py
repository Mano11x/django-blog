content = open('app/templates/app/home.html').read()
with open('app/templates/app/search.html', 'w') as f:
    f.write(content.replace('Latest Posts', 'Search Results'))
