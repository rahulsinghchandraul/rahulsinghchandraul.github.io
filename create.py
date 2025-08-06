#!/usr/bin/python3

import markdown2 as mk
import glob


def main(filename):
    # Read markdown data
    with open(f'{filename}') as fp_in:
        md_data = fp_in.read()

    # Convert markdown to html
    html_data = mk.markdown(md_data)

    with open(f'{filename[:-2]}html', 'w') as fp_out:
        with open('header.htm') as fp_in:
            header_data = fp_in.read()

        # Checking the subdirectories and adjusting the paths of files
        # included in the header
        dir_count = filename.count('/') - 1
        if dir_count:
            header_data = header_data.replace('./', '../' * dir_count)
        if filename == './misc.md':
            header_data += '<script src="https://cdn.wordart.com/wordart.min.js" async defer></script>\n'

        # Writing html header
        fp_out.write(header_data)

        # Writing the content
        fp_out.write(html_data)

        content = '<center>&#9643;&emsp;&#9643;&emsp;&#9643;&emsp;&#9643;</center>'
        fp_out.write(content)


if __name__ == '__main__':
    markdown_files = glob.glob('./**/*.md', recursive=True)

    for filename in markdown_files:
        main(filename)
