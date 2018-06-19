# Template for Bloggers

Below is a template you can use to add your name as a blogger to this list. Note that the file must be a YML file. We have chosen `.yml` as the extension, but `.yaml` will work as well. We probably won't accept your pull request if you do that tho ;)

Info we're looking for. You can leave any field but name and group blank if you wish.

- **Name**
- Description, capped at 50 words (forreal)
- Online links
    - **website**
    - **feed**
- Social links: e.g., twitter

Include a full url to your feed of your blog. This increases the flexibility (to have feeds generated through external services) at the expense of larger bits carried in each yml file ;).

````yaml
name: #Your name, silly.

description: > # if you use 1 line, use a `>`, if you multiple lines, use a `|` here, then ensure that you indent! good yaml syntax.
    example text

online: #Online links
    website: #url
    feed: #whole url

social:
    twitter:  #username
    github:   #username
````
