print('Building Site')

#BLOG
top_html = open('templates/top.html').read()
middle_html = open('content/blog.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('docs/blog.html', 'w+').write(combined_html)

#PROJECTS
top_html = open('templates/top.html').read()
middle_html = open('content/projects.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('docs/projects.html', 'w+').write(combined_html)

#CONTACT ME
top_html = open('templates/top.html').read()
middle_html = open('content/contactme.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('docs/contactme.html', 'w+').write(combined_html)

print('Finished combining HTML files')
