#!/usr/bin/env python

import os
from mkp import dist

# Get Version from Git Tag
version = os.getenv('GITHUB_REF_NAME')

dist({
    'author': 'Michael Neese',
    'description': 'Send notifications via ntfy',
    'download_url': 'https://github.com/Madic-/checkmk-ntfy',
    'name': 'ntfy',
    'title': 'ntfy.sh notification script',
    'version': version,
    'version.min_required': '2.0.0',
})
