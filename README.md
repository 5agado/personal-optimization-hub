<!-- MarkdownTOC autolink="true" -->

- [Personal Optimization Hub](#personal-optimization-hub)
	- [Setup](#setup)
	- [Spaced Repetition](#spaced-repetition)
		- [Anki Generation](#anki-generation)
			- [Intro](#intro)
			- [Run](#run)
			- [Latex in Anki](#latex-in-anki)
	- [Keylogger](#keylogger)
		- [Links](#links)
		- [Usage](#usage)
		- [TODO](#todo)
- [License](#license)

<!-- /MarkdownTOC -->

# Personal Optimization Hub
A central repository for scripts, utils, tools and resources related to personal optimization

## Setup
Run

     python setup.py install

You will then be able to call directly the following utils.

## [Spaced Repetition](https://www.gwern.net/Spaced-repetition)
Set of utilities to generate and manage spaced repetition content.


### Anki Generation
Generation of Anki decks from csv/xlsx files.

#### Intro

This procedure requires specific naming for the sheet columns. There are two main options, one generally used for quotes and extracts, where you are trying to **remember both the exact text and possible source**, which requires the following minimal columns setup:

    text | notes | tags | exported

another option is the traditional **Q&A**, requiring the following columns setup:

    question | answer | tags | exported

As you can see there should always be a *tags* and *exported* columns. The former is a list of strings, the latter is a boolean value to indicate whether the entry has already been exported, used to avoid the generation of multiple cards for the same content. Additional columns can be used to generate further cards, for example *author*, *source* and *context*. The code will take care to generate the corresponding card if such column (with a valid value) is present.

#### Run

To generate an Anki deck from a csv file simply run

    anki-gen -i <input_csv_path> -o <output_dir> -n <deck_name>

Or if you are processing an xlsx file:

    anki-gen -i <input_xlsx_path> -o <output_dir> --process-excel

This will generate an Anki deck for each sheet, named after the sheet title value.

See `anki-gen -h` for a complete usage description

#### Latex in Anki
To define Latex content in a card just wrap it in the following way:

    [latex]\begin{displaymath}your_content\end{displaymath}[/latex]

Alternatively the code will currently do this for you if you specify the *latex* tag in your entry, and use the ```<$$> your_content </$$>``` syntax in your text.

Some setup is needed in order to view Latex in Anki on MacOS. Overall is about installing Latex and dvipng. See also [here](https://apple.stackexchange.com/questions/224784/issues-with-anki-and-basictex).

Also in order to view Latex on AnkiDroid see [here](https://docs.ankiweb.net/#/math?id=latex). Remember to run **Tools->Check Media** before syncing, such that images will be displayed on AnkiDroid.

## Keylogger
Utility to log and analyze keyboard and mouse events. 

Overall goal is personal optimization. Hope to get some insight about typing/mouse patterns by proper analysis. Even if "reinventing the wheel", writing own code from scratch might provide better learning opportunities and easy the adaptation to own need and requirements, plus less worries about the privacy/security concerns. 

Main idea is to initially try keylogger specifically and only during certain activities (e.g. programming, writing). Possibly trying to log activity details and tools used [tools info might be automatize].

**Privacy** is a big point given that you are saving in plain text all typed content. To consider the more involved you get with the project.

**Tablet/Drawing** tracking is another big aspect to investigate. Apart from basic monitor tracking would be nice to have option of point on canvas + additional details like brush, pressure, etc..

### Links
http://hackspc.com/how-to-make-a-python-keylogger/

### Usage
Manually start and stop logger routine. Proceed to notebook for analysis.

### TODO
* "interface" to start logging + report name. A start and end command/key would be a nice option, but for now focus on manual operations.
* stats ideas: pairs of keys with max in-between delays (should discard too long pauses), letter that causes most errors (need to get back and delete).
* analysis in the future might be automatized and manage deletion of logs file.


# License

Released under version 2.0 of the [Apache License](http://www.apache.org/licenses/LICENSE-2.0)
