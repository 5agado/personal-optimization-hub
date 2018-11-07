import pandas as pd
import numpy as np
import genanki
import argparse
import os
import sys
from random import shuffle

############################
# Config Params
############################
NB_INCOMPLETE_EXAMPLES = 3
NB_WORDS_REMOVED = 3

############################
# Note Models
############################

base_model = genanki.Model(
  1607392320,
  'Front/Back Model',
  fields=[
    {'name': 'Front'},
    {'name': 'Back'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Front}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
    },
  ])


############################
# Note Generators
############################

def gen_question_answer(entry: dict):
    return genanki.Note(model=base_model, fields=[entry['question'], str(entry['answer'])])


def gen_by_author(entry: dict):
    if 'author' in entry and entry['author']:
        return genanki.Note(model=base_model, fields=[entry['text'] + " by?", entry['author']])


def gen_by_note(entry: dict):
    if entry['notes']:
        return genanki.Note(model=base_model, fields=[entry['notes'], entry['text']])


def gen_text_incomplete(entry: dict, nb_remove=NB_WORDS_REMOVED):
    full_text = entry['text']
    text_parts = full_text.split()
    remove_idxs = np.random.choice(np.arange(len(text_parts)), min(len(text_parts)-2, nb_remove), replace=False)
    partial_text = " ".join(['<...>' if idx in remove_idxs else part for idx, part in enumerate(text_parts)])
    return genanki.Note(model=base_model, fields=[partial_text, full_text])


def generate_deck(data: pd.DataFrame, deck_name: str, out_dir: str):
    my_deck = genanki.Deck(np.random.randint(1000, 1000000000), deck_name)

    # Q/A style sheet
    if 'question' in data:
        for _, entry in data.iterrows():
            note = gen_question_answer(entry)
            my_deck.add_note(note)

    # Remember-text style sheet
    elif 'text' in data:
        for _, entry in data.iterrows():
            note = gen_by_author(entry)
            if note:
                my_deck.add_note(note)
            note = gen_by_note(entry)
            if note:
                my_deck.add_note(note)
            for _ in range(NB_INCOMPLETE_EXAMPLES):
                note = gen_text_incomplete(entry)
                my_deck.add_note(note)
    else:
        print("No known sheet style identified")
        return

    # shuffle notes
    shuffle(my_deck.notes)

    # export deck
    print("Found {} entries".format(len(data)))
    print("Generated {} notes".format(len(my_deck.notes)))

    deck_path = os.path.join(out_dir, '{}.apkg'.format(deck_name))
    print("Exporting deck to {}".format(deck_path))
    print("-----------------------")
    genanki.Package(my_deck).write_to_file(deck_path)


def generate_decks_from_excel(xlsx_path: str, output_dir: str, generate_all=False):
    data = pd.read_excel(xlsx_path, sheet_name=None)
    for sheet_name, df in data.items():
        df.fillna("", inplace=True)
        df['tags'] = df['tags'].apply(lambda x: x.strip().split())
        # Filter entries already exported
        if not generate_all:
            df = df[~df['exported']]
        generate_deck(df, deck_name=sheet_name, out_dir=output_dir)


def load_data(filepath: str, generate_all=False) -> pd.DataFrame:
    data = pd.read_csv(filepath, converters={"tags": lambda x: x.strip().split()})
    data.fillna("", inplace=True)
    if not generate_all:
        data = data[~data['exported']]
    return data


def main(_=None):
    parser = argparse.ArgumentParser(description='ANKI Deck Generation')
    parser.add_argument('-i', '--input-path', type=str, help='Path to the input CSV file containing the data'
                                                             'or Excel one if --process-excel is provided',
                        required=True)
    parser.add_argument('-o', '--output-dir', type=str, help='Directory where to export the generated deck',
                        default='./')
    parser.add_argument('-n', '--deck-name', type=str, default='anki_deck')
    parser.add_argument('--process-excel', action='store_true', default=False)
    parser.add_argument('--generate-all', action='store_true', default=False,
                        help='Force generation of all entries, ignoring the `exported` value')

    args = parser.parse_args()

    if args.process_excel:
        generate_decks_from_excel(args.input_path, args.output_dir, args.generate_all)
    else:
        data_df = load_data(args.input_path, args.generate_all)

        generate_deck(data_df, deck_name=args.deck_name, out_dir=args.output_dir)

if __name__ == "__main__":
    main(sys.argv[1:])