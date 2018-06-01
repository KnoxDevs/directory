# Template for groups

Below is a template you can use to add your group to this list. Note that the file must be a YML file. We have chosen `.yml` as the extension, but `.yaml` will work as well. We probably won't accept your pull request if you do that tho ;)

Info we're looking for. You can leave any field but name and group blank if you wish.

- **Name**
- Image
- Online links, website and/or twitter
- Blurb, capped at 50 words (forreal)

````yaml
name: #group Name
image: #Logo Upload into assets/images/groups
online: #Online links
    website: #url
    github: #github username
    twitter: # twitter username
    meetup: # this is the meetup url  
location: # group Location
    name: 
    gmap:  # google map short 
slack_channel: #the slack channel most associated with your group!
blurb: > # if you use 1 line, use a `>`, if you multiple lines, use a `|` here, then ensure that you indent! good yaml syntax.
    example text
````
