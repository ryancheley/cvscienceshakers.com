AUTHOR = 'Abigail Cheley'
SITENAME = 'Coachella Valley Science Shakers'
SITESUBTITLE = "Not educated about earthquakes? That's your fault!"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/cvscienceshakers'

STATIC_PATHS = [
    "images",
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False


DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

MENUITEMS = [
    ("About Us", "/pages/about-us", [
        ("Interviews of the team", "/pages/interviews-of-the-team"),
        ("Field Trips", "/pages/field-trips"),
        ("The Coachella Valley", "/pages/the-coachella-valley"),
        ("Cited Sources", "/pages/cited-sources"),
    ]),
    ('Whitewater Preserve', '/pages/whitewater-preserve', [
        ('Geography', '/pages/geography'),
        ('Seismic Activity', '/pages/seismic-activity'),
        ('Alluvial Fans', '/pages/alluvial-fans'),
    ]),    
    ("The San Andreas Fault", "/pages/the-san-andreas-fault", [
        ("Seismic Activity", "/pages/san-andreas-seismic-activity"),
        ("Aquifers", "/pages/san-andreas-aquifers"),
    ]),
    ("Seismology", "/pages/seismology", [
        ("Types of Faults", "/pages/types-of-faults", [
            ("Convergent", "/pages/convergent"),
            ("Divergent", "/pages/divergent"),
            ("Strike Slip", "/pages/strike-slip"),
            ("Thrust Faults", "/pages/thrust-faults"),
        ]),
        ("Measuring Earthquakes", "/pages/measuring-earthquakes"),
    ]),
]
