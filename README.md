# Fitness

A project I use for refreshing myself in SQL and Python.

It manages/seeds a database of exercises and users for tracking progress.

## Vision
Inspired by Hevy, my goal is to create a free and open source app for tracking your fitness progress.
To achieve this, data will be hosted locally or in free third-party places (e.g., using a Youtube channel to link to exercise demos).
Peer-to-peer networking is planned for social engagement.
In honesty, Godot would be a perfect fit for this (and would streamline a lot of work), but I also want to explore tech stacks more commonly used in the corporate world.

## Current state of project
Still working to achieve v1.0.

## Hi, Recruiter! :wave:
Please take a look at the python/onboarding/ folder for a demo of basic Python concepts and usage with Pandas and NumPy.

## Getting started
1. Install Python with pip.
2. At the root of this project, run "pip install -r python/requirements.txt".
3. Download the sqlite shared libraries and commandline tools to your machine and put them somewhere on disc (e.g. C:\sqlite).
4. Add the folder with the sqlite libraries and tools to your system's "PATH".
5. (Optional) Install the DB Browser for SQLite.

## Notes
- All dates and times are stored in UTC.
- I'm trying to use the datatypes in the SQL database that are the most universally supported across systems. A note is given to indicate any specific usage (e.g., TEXT used as a DATETIME).
