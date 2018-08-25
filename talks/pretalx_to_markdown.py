#!/usr/bin/env python3
# -*- coding: utf-8

import json
from urllib.parse import quote_plus

# Get talks from here: https://cfp.hack.lu/api/events/hacklu18/talks/?limit=100
# TODO: automate that.

with open('talks.json') as f:
    talks = json.load(f)


all_keynotes = '''# Keynotes
'''
all_talks = '''
# Talks
'''
all_workshops = '''
# Workshops
'''

talk_template = '''
## <a name="{escaped_title}"></a>{title}
by {speaker}

{abstract}

'''

speaker_template = '''
### Bio: <a name="{escaped_speaker}"></a>{speaker}

{bio}

'''

for talk in talks['results']:
    if talk['state'] != 'confirmed':
        print('NOT CONFIRMED', talk['title'])
        continue
    md_talk = talk_template.format(escaped_title=quote_plus(talk['title']),
                                   title=talk['title'],
                                   speaker=', '.join([speaker['name'] for speaker in talk['speakers']]),
                                   abstract=talk['abstract'])
    for speaker in talk['speakers']:
        md_talk += speaker_template.format(speaker=speaker['name'],
                                           escaped_speaker=quote_plus(speaker['name']),
                                           bio=speaker['biography'])

    if talk['submission_type']['en'] in ['Short talk', 'Talk']:
        all_talks += md_talk
    elif talk['submission_type']['en'] in ['Long Workshop', 'Workshop']:
        all_workshops += md_talk
    elif talk['submission_type']['en'] in ['Keynote']:
        all_keynotes += md_talk

headers = '''---
layout: splash
title:  Talks
excerpt: "Talks - Hack.lu 2018"
---

'''

with open('index.md', 'w') as f:
    f.write(headers)
    f.write(all_keynotes)
    f.write(all_talks)
    f.write(all_workshops)
