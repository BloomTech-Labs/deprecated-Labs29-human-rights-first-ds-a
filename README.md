# Human Rights First Police Use of Force Map

You can find the deployed project at [Human Rights First Police use of Force](https://main.d17v0exvwwwzgz.amplifyapp.com/).

## Contributors


|                                                      [student 1](https://github.com/)                                                       |                                                       [student 2](https://github.com/)                                                        |                                                      [student 3](https://github.com/)                                                       |                                                                                                               |                                                                                                             |
| :-----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/) | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-female.png" width = "200" />](https://github.com/) | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/) | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-female.png" width = "200" />](https://github.com/) | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/) |
|                                [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/)                                |                            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/honda0306)                             |                          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Mister-Corn)                           |                          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/NandoTheessen)                           |                           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/wvandolah)                            |
|                [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)                |                 [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)                 |                [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)                |                 [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)                 |                [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)                |

<br>
<br>


![fastapi](https://img.shields.io/badge/fastapi-0.60.1-blue)
![pandas](https://img.shields.io/badge/pandas-1.1.0-blueviolet)
![plotly](https://img.shields.io/badge/plotly-4.9.0-brightgreen)
![uvicorn](https://img.shields.io/badge/uvicorn-0.11.8-ff69b4)
![praw](https://img.shields.io/badge/praw-7.1.0-red)
![python-dotenv](https://img.shields.io/badge/python--dotenv-0.14.0-green)
![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.9.1-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.23.2-yellow)
![spacy](https://img.shields.io/badge/spacy-2.3.2-lightgrey)
![newspaper3k](https://img.shields.io/badge/newspaper3k-0.2.8-9cf)
![fastapi-utils](https://img.shields.io/badge/fastapi--utils-0.2.1-informational)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-11.3.20-yellowgreen)


## Project Overview

1️⃣ [Trello Board](https://trello.com/b/vUsfsVej/team-a-labs28)

1️⃣ [Product Canvas](https://whimsical.com/47hccoy2w65yxpK8dSfpwz)

Our team is developing an interactive map that identifies potential instances of police use of force across the United States of America for Human Rights First, an independent advocacy and action organization.

We're pulling data from similiar APIs(All locations V2 - https://raw.githubusercontent.com/2020PB/police-brutality/data_build/all-locations-v2.json, 846- https://api.846policebrutality.com/api/incidents) and from Twitter and Reddit. We want to identify aggregate these instances.

### 4️⃣ Key Features


- User can browse incident map
- User can view specific instances with original source links
- User can view map with various filters

## 1️⃣ Tech Stack

### Data Science API built using:

- Python
- Docker
- FastAPI
- AWS Elastic Beanstalk


#### _Data Science goes here_

🚫 Why did you choose this framework?

- Works well with FastAPI
- Recommended to us
- Wanted to learn an in-demand framework

🚫List the rest of the data science features and libraries in the same format as the framework above.

- Pandas
- scikit-learn
- spacy
- nltk
- PRAW
- Tweepy

#### Data Science API deployed to AWS

#### [Back end](🚫link to back end repo here) built using:

#### 🚫 back end framework goes here (link to BE REPO)

- point one
- point two
- point three

🚫 List the rest of the back end end features and libraries in the same format as the framework above

# APIs

## 2️⃣ Data Science API

We are sending json objects to the backend with information about instances of police use of force. This information includes location data (city, state, and geocode) and relevant details about the incident, like the type of force that was used.

## 2️⃣ PRAW

PRAW, The Python Reddit API Wrapper, makes it easy for users to analyze Reddit data. We used PRAW to scrape Reddit for potential instances of police of force.

## 3️⃣ Tweepy

Tweepy is a Python library that allows users to access the Twitter API. We used Tweepy to scan Twitter to find instances of police use of force.

# 3️⃣ Environment Variables

In order for the app to function correctly, the user must set up their own environment variables. There should be a .env file containing the following:

🚫These are just examples, replace them with the specifics for your app

    *  PRAW_CLIENT_ID  - keys for Reddit API
    *  PRAW_CLIENT_SECRET - keys for Reddit API
    *  PRAW_USER_AGENT - keys for Reddit API
    *  TWEEPY_CONSUMER - keys for Twitter API
    *  TWEEPY_SECRET - keys for Twitter API
    *  TWEEPY_ACCESS - keys for Twitter API
    *  TWEEPY_ACCESS_SECRET - keys for Twitter API

# 5️⃣ Content Licenses

🚫For all content - images, icons, etc, use this table to document permission of use. Remove the two placeholders and add you content to this table

| Image Filename | Source / Creator | License                                                                      |
| -------------- | ---------------- | ---------------------------------------------------------------------------- |
| doodles.png    | Nicole Bennett   | [Creative Commons](https://www.toptal.com/designers/subtlepatterns/doodles/) |
| rings.svg      | Sam Herbert      | [MIT](https://github.com/SamHerbert/SVG-Loaders)                             |

# 4️⃣ Testing

🚫Document what you used for testing and why

# 4️⃣ Installation Instructions

🚫explain how to install the required dependencies to get this project up and running with yarn and NPM

## Other Scripts

🚫replace these examples with your own

    * typecheck - runs the TypeScript compiler
    * build - creates a build of the application
    * start - starts the production server after a build is created
    * test - runs tests in **tests** directory \* eject - copy the configuration files and dependencies into the project so you have full control over them

# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./CODE_OF_CONDUCT.md). Please follow it in all your interactions with the project.

## Issue/Bug Request

**If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**

- Check first to see if your issue has already been reported.
- Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
- Create a live example of the problem.
- Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes, where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](🚫*link to your backend readme here*) for details on the backend of our project.
