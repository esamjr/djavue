![vuelogo](docs/vue.png)
![django](docs/django.png)

# Djavue Blog

[![DjaVue](https://circleci.com/gh/HotPotatoC/djavue.svg?style=shield)](https://circleci.com/gh/HotPotatoC/djavue)
[![DjaVue](https://circleci.com/gh/HotPotatoC/djavue.svg?style=svg)](https://circleci.com/gh/HotPotatoC/djavue)

A blog made with Django, VueJS and sqlite3

## Table Of Content

- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Getting Started

Clone the repository

```
$ git clone https://github.com/HotPotatoC/djavue.git
$ cd djavue
```

Install the dependencies

```
$ python -m pip install -r requirements.txt
$ npm install
```

Run the services

```
$ ./runserver
$ npm run serve
```

Then head to `http://localhost:8080/` to see your web application running.

## Project Structure

| Route | Content |
| ------------- | ------------- |
| / | View Articles |
| /post/:id | View an Article post by the id |
| /create | Add a new post |
| /edit/:id | Edit a post |

API

| Method | Route | Content |
| ------------- | ------------- | ------------- |
| GET | /api/v1/articles | View Articles |
| GET | /api/v1/articles/:id | View an Article by the id |
| POST | /api/v1/articles | Add a new Article |

## Contributing

Your contribution is greatly appreciated. Please refer to the [contribution](docs/CONTRIBUTING.md) guide to contribute to this repo.
