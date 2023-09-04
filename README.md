# Phase 3 Week 3 Code Challenge: Restaurants

For this project, we'll be working with a restaurant review domain.

We have three models: `Restaurant`, `Review`, and `Customer`.

For our purposes, a `Restaurant` has many `Review`s, a `Customer` has many

`Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`.

`Restaurant` - `Customer` is a many to many relationship.

Get the additional project details [here](/SQLAlchemy-Code-Challenge_Restaurants.pdf).

## Topics

- SQLAlchemy Migrations

- SQLAlchemy Relationships

- Class and Instance Methods

- SQLAlchemy Querying

***

## Setup Requirements

- Visual Studio Code, see [here](https://code.visualstudio.com/)
- Any [supported](https://www.python.org/downloads/) OS / environments / Windows Subsystem for Linux (WSL), details [here](https://learn.microsoft.com/en-us/windows/python/web-frameworks)
- Git and Github
- Python (Recommend version 3.10+), get the latest [here](https://www.python.org/downloads/)
- Pipenv, a Python virtualenv management tool, see details [here](https://pypi.org/project/pipenv/)

## Installation

- Clone/Download the code from the repository, navigate to the directory on the terminal
- Run `pipenv install` to install required packages
- Run `pipenv shell` to use the project in created project environment

## Language(s)

- Python

## Packages

- SQLAlchemy
- Alembic
- Faker

## Author

[Eugene Aduogo](https://github.com/eugenemrg)

## License

Copyright (C) 2023

Licensed under GNUv3. See [license](/LICENSE)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.