# -*- coding: utf-8 -*-

import argparse
from os import listdir
from os.path import isfile, join, dirname, basename
import tokenizer, util


def get_text_in_ler_format(text, email_address, tokens_per_line):
    document = "#METADATA\n"
    document += "\n"
    document += "#TEXT\n"
    document += "%s\n" % ' '.join(text)
    document += "\n"
    document += "#COLLABORATORS\n"
    document += "%s\n" % email_address
    document += "\n"
    document += "#STATUS\n"
    document += "UNCHECKED\n"
    document += "UNDONE,R-UNDONE\n"
    document += "\n"
    document += "#DESCRIPTION\n"
    document += "ID\tFORM\tPROB\tLEMMA\tPOS\tTAG\tRELATION\tCONNECTOR\n"

    default_line_complement = "0.1\tO\tO\tO;O\tO;O\tO;O"

    token_counter = 0
    for token in text:
        if token == '':
            continue

        if token_counter != tokens_per_line:
            current_line = "%d\t%s\t%s\n" % (token_counter, token, default_line_complement)
            token_counter += 1
        else:
            current_line = "\n%d\t%s\t%s\n" % (token_counter, token, default_line_complement)
            token_counter = 0

        document += current_line


    return document


def tokenize(dataset_directory, output_directory, email_address, lowercase, remove_stopwords,
             stemmize, strip_accents, expand_contractions, use_min_word_length, tokens_per_line):

    util.create_dirs(output_directory)

    dataset_filenames = [join(dataset_directory, f) for f in listdir(dataset_directory) if isfile(join(dataset_directory, f))]

    for dataset_filename in dataset_filenames:
        with open(dataset_filename, 'r') as dataset_file:
            text = dataset_file.read()
            text_preprocessed = tokenizer.preprocess_text(text, lowercase=lowercase, remove_stopwords=remove_stopwords,
                                                          stemmize=stemmize, strip_accents=strip_accents,
                                                          expand_contractions=expand_contractions,
                                                          use_min_word_length=use_min_word_length)

        text_in_ler_format = get_text_in_ler_format(text_preprocessed, email_address, tokens_per_line)

        filename = basename(dataset_filename)
        output_filename = join(output_directory, filename)

        with open(output_filename, 'w') as output_file:
            output_file.write(text_in_ler_format)


if __name__ == '__main__':
    script_directory = dirname(__file__)

    args_parser = argparse.ArgumentParser()

    args_parser.add_argument('dataset_dir', help='Directory with files to be tokenized.')
    args_parser.add_argument('output_dir', help='Directory to save tokenized files.')
    args_parser.add_argument('email_address', help='E-mail address of the package manager in ERAS annotation system.')
    args_parser.add_argument('-l', '--lowercase', type=int, choices=[0, 1], default=1, help='Choose whether lowercase '
                                                                                            'the words in the dataset.')
    args_parser.add_argument('-r', '--remove_stopwords', type=int, choices=[0, 1], default=0, help='Choose whether '
                                                                                                   'remove stop words '
                                                                                                   'in the dataset.')
    args_parser.add_argument('-s', '--stemmize', type=int, choices=[0, 1], default=0, help='Choose whether stemmize '
                                                                                           'the words in the dataset.')
    args_parser.add_argument('-a', '--strip_accents', type=int, choices=[0, 1], default=1, help='Choose whether strip '
                                                                                                'accents from the '
                                                                                                'words.')
    args_parser.add_argument('-c', '--expand_contractions', type=int, choices=[0, 1], default=1, help='Choose whether '
                                                                                                      'expand language '
                                                                                                      'contractions '
                                                                                                      '(e.g. "pelo" '
                                                                                                      'becomes "por" + '
                                                                                                      '"o").')
    args_parser.add_argument('-m', '--min_word_length', type=int, choices=[0, 1], default=0, help='Choose whether only '
                                                                                                  'keep words with '
                                                                                                  'at least three '
                                                                                                  'characters.')
    args_parser.add_argument('-t', '--tokens_per_line', type=int, default=10, help='Number of tokens per line in ERAS '
                                                                                   'annotation system.')

    args = args_parser.parse_args()

    dataset_directory = args.dataset_dir
    output_directory = args.output_dir
    email_address = args.email_address
    lowercase = bool(args.lowercase)
    remove_stopwords = bool(args.remove_stopwords)
    stemmize = bool(args.stemmize)
    strip_accents = bool(args.strip_accents)
    expand_contractions = bool(args.expand_contractions)
    use_min_word_length = bool(args.min_word_length)
    tokens_per_line = args.tokens_per_line

    tokenize(dataset_directory=dataset_directory, output_directory=output_directory,
             email_address=email_address, lowercase=lowercase, remove_stopwords=remove_stopwords,
             stemmize=stemmize, strip_accents=strip_accents, expand_contractions=expand_contractions,
             use_min_word_length=use_min_word_length, tokens_per_line=tokens_per_line)
