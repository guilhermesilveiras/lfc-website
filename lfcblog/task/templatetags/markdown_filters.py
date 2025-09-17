from django import template
try:
    from markdown import markdown as md  # type: ignore
except Exception:  # pragma: no cover
    def md(text, extensions=None):
        return text
try:
    import bleach  # type: ignore
except Exception:  # pragma: no cover
    class _B:
        class sanitizer:
            ALLOWED_TAGS = set()
            ALLOWED_ATTRIBUTES = {}
        @staticmethod
        def clean(x, tags=None, attributes=None):
            return x
    bleach = _B()  # type: ignore

register = template.Library()

ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS.union({
    'p', 'pre', 'code', 'img', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'thead', 'tbody', 'tr', 'th', 'td', 'blockquote', 'hr'
})
ALLOWED_ATTRS = {
    **bleach.sanitizer.ALLOWED_ATTRIBUTES,
    'img': ['src', 'alt', 'title'],
    'a': ['href', 'title', 'target', 'rel'],
}

@register.filter(name='markdownify')
def markdownify(value):
    if not value:
        return ''
    html = md(value, extensions=['fenced_code', 'codehilite', 'tables', 'toc', 'sane_lists'])
    clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)
    return clean
