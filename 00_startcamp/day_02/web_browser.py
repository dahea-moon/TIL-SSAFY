import webbrowser

urls = [
    'www.naver.com',
    'www.google.com',
    'www.slack.com',
    'www.github.com',
    'www.youtube.com'
]

# for url in urls:
#     webbrowser.open(url)

i = 0
while i < 5:
    webbrowser.open(urls[i])
    i += 1
