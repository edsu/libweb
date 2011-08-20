Have you ever wanted a machine readable list of URLs for library websites 
around the world? It's pretty unlikely, but if you have, read on.

This screen scraper will crawl [LIBWEB](http://lists.webjunction.org/libweb/)
and extract information about library websites around the world and 
persist it as JSON. The libraries.json file that is committed here has name,
location and the URL for 7990 libraries.

    [
      {
        "url": "http://libraries.adelphi.edu/", 
        "name": "Adelphi University", 
        "location": "Garden City NY"
      }, 
      {
        "url": "http://www.sunyacc.edu/Library/", 
        "name": "Adirondack Community College", 
        "location": "Queensbury NY"
      }, 
      {
        "url": "http://www.acp.edu/academics_library.html", 
        "name": "Albany College of Pharmacy", 
        "location": "Albany NY"
      }, 
      {
        "url": "http://www.albertus.edu/academic/library.shtml", 
        "name": "Albertus Magnus College", 
        "location": "New Haven CT"
      }, 
      {
        "url": "http://www.albright.edu/library/", 
        "name": "Albright College", 
        "location": "Reading PA"
      }, 
      {
        "url": "http://www.herr.alfred.edu/", 
        "name": "Alfred University", 
        "location": "Alfred NY"
      }, 
      ...
    ]

To re-crawl LIBWEB you will need to install [Python](http://python.org), 
[lxml](http://pypi.python.org/pypi/lxml) and then run libraries.py


License: [CCO](http://creativecommons.org/about/cc0)
