#!/usr/bin/env python

import json

from lxml import html

from urlparse import urlparse, urljoin


def get_libraries(url="http://lists.webjunction.org/libweb/", seen={}):
    if seen.has_key(url):
        return

    doc = html.parse(url)
    seen[url] = True

    print "crawling %s" % url

    for li in doc.xpath('.//li'):
        a = li.find('.//a')
        if a == None:
            continue

        parts  = [s.strip() for s in li.text_content().strip().split("\n")]

        link = urlparse(a.attrib['href'])

        if len(parts) == 2 and link.netloc and \
                link.netloc != 'lists.webjunction.org':
            yield {'name': parts[0], 
                   'location': parts[1],
                   'url': a.attrib['href']}

        elif link.netloc == '':
            for library in get_libraries(urljoin(url, a.attrib['href']), seen):
                yield library


if __name__ == "__main__":
    libraries = []
    for library in get_libraries():
        libraries.append(library)
    open('libraries.json', 'w').write(json.dumps(libraries, indent=2))
    print "wrote data for %i libraries to libraries.json" % len(libraries)
