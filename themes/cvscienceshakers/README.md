# Coachella Valley Science Shakers Pelican Theme

This Pelican theme is based on the Magazine Hoot WordPress theme used on the original https://cvscienceshakers.com/ website.

## Overview

This theme replicates the design and styling of the WordPress site, including:
- Header with site title and tagline
- Multi-level navigation menu
- Content area with WordPress Magazine Hoot styling
- Footer with credits
- Custom accent colors (#d1ca14 - yellow-gold)
- Earthquake background image
- Font Awesome icon support
- Responsive design

## Installation

1. Copy this theme directory to your Pelican site's `themes/` directory
2. Configure your `pelicanconf.py` to use this theme:

```python
THEME = 'themes/cvscienceshakers'
SITENAME = 'Coachella Valley Science Shakers'
SITESUBTITLE = "Not educated about earthquakes? That's your fault!"
```

## Features

### Templates Included

- `base.html` - Base template with header, navigation, and footer
- `index.html` - Homepage with featured content and recent articles
- `article.html` - Individual article/blog post template
- `page.html` - Static page template
- `archives.html` - All articles archive
- `categories.html` - Categories listing
- `category.html` - Single category view
- `tags.html` - Tag cloud
- `tag.html` - Single tag view

### CSS Files

All CSS files from the WordPress site have been extracted and included:

- `block-library.min.css` - WordPress block library styles
- `font-awesome.css` - Font Awesome icons
- `lightSlider.css` - Image slider styles
- `gallery.min.css` - Gallery styles
- `main-style.css` - Main theme stylesheet from Magazine Hoot
- `wpblocks.css` - WordPress blocks styling
- `earthquakemonitor.css` - Earthquake monitor plugin styles
- `inline-styles.css` - Extracted inline styles from the homepage

### Custom Styling

The theme includes custom CSS for:
- Accent color: #d1ca14 (yellow-gold)
- Hover color: #9d970f (darker gold)
- Background: #f7f7f7 (light gray)
- White content areas
- Custom button styles
- Menu highlighting

## Configuration

### Recommended Pelican Settings

Add these to your `pelicanconf.py`:

```python
# Site Info
SITENAME = 'Coachella Valley Science Shakers'
SITESUBTITLE = "Not educated about earthquakes? That's your fault!"
SITEURL = ''  # Leave empty for development

# Theme
THEME = 'themes/cvscienceshakers'

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Pagination
DEFAULT_PAGINATION = 10

# Path settings
PATH = 'content'
STATIC_PATHS = ['images', 'extra']
```

## Customization

### Changing Colors

To change the accent color, edit the custom styles in `templates/base.html`:

```css
a, .widget .view-all a:hover {
    color: #d1ca14;  /* Change this color */
}
```

### Navigation Menu

The navigation menu is automatically generated from your Pelican pages. To customize the menu order or structure, use the `MENUITEMS` setting in your `pelicanconf.py`:

```python
MENUITEMS = [
    ('Home', '/'),
    ('About', '/pages/about.html'),
    # Add more menu items...
]
```

### Background Image

To change or remove the earthquake background image, edit the `body` CSS rule in `templates/base.html`.

## Credits

- Original design: [Magazine Hoot WordPress Theme](https://wphoot.com/themes/magazine-hoot/)
- Ported to Pelican for Coachella Valley Science Shakers project
- Font Awesome for icons
- Google Fonts: Roboto, Oswald, Open Sans

## License

This theme is based on the Magazine Hoot WordPress theme and is provided for use with the Coachella Valley Science Shakers project.
