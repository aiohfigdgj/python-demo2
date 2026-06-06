def md_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_list = False
    html_lines = []

    for line in lines:
        line = line.rstrip('\n')

        if line.startswith('#'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            level = line.count('#', 0, line.find(' '))
            title = line.lstrip('#').strip()
            html_lines.append(f'<h{level}>{title}</h{level}>')

        elif line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            item = line[2:].strip()
            html_lines.append(f'<li>{item}</li>')

        elif line.strip():
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)

    if in_list:
        html_lines.append('</ul>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_lines))


md_html('test.md', 'res.html')