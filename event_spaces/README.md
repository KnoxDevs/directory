# Event Spaces

Do you know of an event space / or operate an event space that you would like to see represented on the KnoxDevs website? There are three primary ways, in descending preference, to get your event space added!

1) Send a Pull Request. (highly recommended!) 

New to pull requests? Here are a couple of tutorials: [from Github](https://help.github.com/articles/about-pull-requests/), [from Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github), [from Thinkful](https://www.thinkful.com/learn/github-pull-request-tutorial/). We have a template [below](#template-for-event-spaces) to get you ready to send a good PR!

2) Submit an issue. 

Has the idea of sending a PR freak you out? Remember that if you're just submtting a PR on 1 file, you might be able to just edit the file here on Github and then propose the PR. Still, if that's too much, submit an issue [above](https://github.com/KnoxDevs/knoxdevs.github.io/issues). We can step you through the change you would like to have made.

3) Get in touch on Slack. 

Has the idea of submitting an issue seem like a massive pain to just update text? Okay. get in touch on [Slack](https://knoxdevs.slack.com/messages/) with one of the many KnoxDevs members. They can help you out... if you ask nicely ;).

## Template for Event Spaces

Below is a template you can use to add your event space to this list via a Pull Request. Note that the file must be a YML file. We have chosen `.yml` as the extension, but `.yaml` will work as well. We probably won't accept your pull request if you do that tho ;)

Info we're looking for. You can leave any field but name and location blank if you wish.

- **Name**
- Description (please keep to 50 characters or so)
- Online links, e.g., website
- Social links: e.g., twitter
- **Location**

````yaml
name: #Event Space Name

online: #Online links
    website: 

social:
    twitter:  

location: # Event Space Location
    address:
    latitude:
    longitude:

description: > # if you use 1 line, use a `>`, if you multiple lines, use a `|` here, then ensure that you indent! good yaml syntax.
    example text
````
