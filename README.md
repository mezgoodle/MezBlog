# MezBlog

[![Language](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Hello everyone! This is the repository of blog application on Django framework.

## Table of contents

- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Build status](#build-status)
- [Badges](#badges)
- [Screenshots](#screenshots)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Tests](#tests)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

I want to learn Django and make _one more_ blog app with this framework. So it is, I have found tutorial, do something and added own features.

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

![Django CI](https://github.com/mezgoodle/MezBlog/workflows/Django%20CI/badge.svg)

## Badges

[![Theme](https://img.shields.io/badge/Theme-Blog-brightgreen?style=flat-square)](https://www.google.com/search?q=django+shop&rlz=1C1CHZO_ukUA900UA900&oq=django+shop&aqs=chrome..69i57j0l5j69i60l2.2903j1j7&sourceid=chrome&ie=UTF-8)
[![Platform](https://img.shields.io/badge/Platform-Django-brightgreen?style=flat-square)](https://www.djangoproject.com/)
 
## Screenshots

- Main page

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/mezblog1.PNG)

- Pagination

![Screenshot 2](https://raw.githubusercontent.com/mezgoodle/images/master/mezblog2.PNG)

- Сomments

![Screenshot 3](https://raw.githubusercontent.com/mezgoodle/images/master/mezblog3.PNG)

- Share page

![Screenshot 4](https://raw.githubusercontent.com/mezgoodle/images/master/mezblog4.PNG)

## Tech/framework used

**Built with**

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Features

On the website you can add articles, share them, make pagination.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mezgoodle/MezBlog.git
```

2. Install all dependencies with [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

## Fast usage

1. Rename `.env_sample` to `.env` and fill the variables like:

```bash
EMAIL_HOST_PASSWORD="<YOUR_EMAIL_PASSWORD>"
```

2. Move to _mysite_ directory, make migrations and create super-user:

```bash
cd mysite
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

3. Start the development server:

```bash
python3 manage.py runserver
```

## Tests

You can see all tests in [**tests.py**](https://github.com/mezgoodle/MezBlog/blob/master/mysite/blog/tests.py). And there results [here](https://github.com/mezgoodle/MezBlog/actions?query=workflow%3A%22Django+CI%22).

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits

Credit to tutorial:

- [Article on DJANGOCENTRAL](https://djangocentral.com/building-a-blog-application-with-django/)

## License

MIT © [mezgoodle](https://github.com/mezgoodle)
