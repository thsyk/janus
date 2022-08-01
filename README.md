# JANUS
<img src="https://user-images.githubusercontent.com/86777463/180721589-1603bfe7-da7b-4366-add3-7928ad7b6898.png" width="200" height="200">

**Create random non-boring usernames with Janus**<br>
Alfred-Workflow: [Janus-For-Alfred](https://github.com/manesspl/janus-for-alfred)

## About
Janus is a command line tool for a fast and easy creation of **non-boring** usernames. Lenght, style and number of created usernames is configureable.  Janus chooses randomly out of more than 145.000 database entries and combines them in various ways.

## Examples
If you are looking for a generator that creates usernames like `MIRACLEFRUIT`, `AsIa.STiLeTtO`, `High-Kuh` or `MuddyMacro` you have finally found the right place. I have never found it. That's why Janus exists.

## Installation
Requirements: Python > 3.8

### Clone Repository:

```
$ git clone https://github.com/manesspl/janus
$ cd Janus
```

### Install into a Python virtual environment:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

## Usage

Run Janus by simply starting the script: `$ pyhton3 janus.py <options>`. <br><br>
Help is available via `$ pyhton3 janus.py --help`.

**Options**:<br>
- ```-l, --long``` — Generate longer usernames<br>
- ```-n, --number INTEGER``` — Define the number of generated usernames (Default: 10)<br>
- ```--style``` — Choose style of username: `low` = lowercase, `up` = UPPERCASE, `mix` = MiXeD, `cap` = In Small Caps<br>
