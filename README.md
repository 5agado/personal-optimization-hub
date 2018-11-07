# Personal Optimization Hub
A central repository for scripts, utils, tools and resources related to personal optimization

## Setup
Run

     python setup.py install

You will then be able to call directly the following utils.

## [Spaced Repetition](https://www.gwern.net/Spaced-repetition)
Set of utilities to generate and manage spaced repetition content.

For example generation of ANKI decks from csv/xlsx files. Files need at least *text* and *note* columns, or *question* and *answer* ones. There should always be a *tags* column.

To generate an ANKI deck simply run

    anki-gen -i <input_csv_path> -o <output_dir> -n <deck_name>

Or if you are processing an .xlsx file (decks names will be derived from sheets names):

    anki-gen -i <input_xlsx_path> -o <output_dir> --process-excel

See `anki-gen -h` for a complete usage description

### Latex in ANKI
Need some setup in order to view Latex in Anki on MacOS. Overall is about installing Latex and dvipng. See also [here](https://apple.stackexchange.com/questions/224784/issues-with-anki-and-basictex).

To define Latex content in a card just wrap it in the following way:

    [latex]\begin{displaymath}your_content\end{displaymath}[/latex]

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
