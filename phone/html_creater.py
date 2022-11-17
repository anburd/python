
def create(data):
    html = '<html>\n<head>\n<meta charset="windows-1251">\n</head>\n<body>\n'
    style = 'style="font-size:18px;"'
    for element in data:
        html +='\t<p {}> '.format(style)
        for i in element:
            html += '\t{} '.format(i)
        html += '</p>\n'

    html += '\t</body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html
