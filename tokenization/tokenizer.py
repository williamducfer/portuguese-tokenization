import re
import unicodedata
from nltk.stem.snowball import SnowballStemmer
from os.path import join, dirname

script_file_path = dirname(__file__)

__contractions_filename = join(script_file_path, "conf", "contractions.txt")
__abbreviations_filename = join(script_file_path, "conf", "abbreviations_wikipedia_pt_and_manual_entries.txt")
__stopwords_filename = join(script_file_path, "conf", "stopwords.txt")


def preprocess_text(text, lowercase=True, remove_stopwords=False, stemmize=False, strip_accents=True,
                    expand_contractions=True, use_min_word_length=False, join_tokens_by_char=None):

    text_special_chars_converted = _convert_special_chars(text)

    text_tokenized_list = _tokenize_text(text_special_chars_converted, expand_contractions=expand_contractions)
    text_preprocessed_list = _preprocess_tokenized_text(text_tokenized_list, lowercase=lowercase,
                                                        remove_stopwords=remove_stopwords, stemmize=stemmize,
                                                        strip_accents=strip_accents, min_word_length=use_min_word_length)

    if join_tokens_by_char is not None:
        text_preprocessed_final = join_tokens_by_char.join(text_preprocessed_list)
    else:
        text_preprocessed_final = text_preprocessed_list

    return text_preprocessed_final


def _is_number(token):
    currency_sign_index = token.find('$')
    if currency_sign_index != -1:
        token = token[currency_sign_index + 1:]

    match_idxs = re.findall("[^0-9\.,:\/\-\(\)]+", token)

    if len(match_idxs) == 0:
        token_is_number = True
    else:
        token_is_number = False

    return token_is_number


def _is_email(token):
    match_idxs = re.findall("[a-z0-9]+@[a-z0-9\.]+", token)

    if len(match_idxs) > 0:
        token_is_email = True
    else:
        token_is_email = False

    return token_is_email


def _convert_special_chars(text):
    #
    re_quotes = re.compile(r"[‘’′`'´¿]", re.UNICODE)
    re_double_quotes = re.compile(r"[”“]", re.UNICODE)
    re_underscores = re.compile(r"_[_]+", re.UNICODE)

    text_special_chars_converted = re_quotes.sub("'", text)
    text_special_chars_converted = re_double_quotes.sub('"', text_special_chars_converted)
    text_special_chars_converted = re_underscores.sub('_', text_special_chars_converted)

    return text_special_chars_converted


def _find_real_periods_in_text(text, abbreviations_set):
    period_idx = text.find('.')

    while period_idx != -1:
        beginning_separator_idx = text.rfind(' ', 0, period_idx)
        end_separator_idx = text.find(' ', period_idx)

        word_to_evaluate = text[beginning_separator_idx + 1:end_separator_idx + 1].lower().strip()

        if len(word_to_evaluate) > 2:
            chars_to_remove_from_beginning_and_end = ['(', ')', ':']

            if word_to_evaluate[0] in chars_to_remove_from_beginning_and_end:
                word_to_evaluate = word_to_evaluate[1:]
            if word_to_evaluate[-1] in chars_to_remove_from_beginning_and_end:
                word_to_evaluate = word_to_evaluate[:-1]

        if word_to_evaluate not in abbreviations_set and \
                (not _is_number(word_to_evaluate) or (_is_number(word_to_evaluate) and period_idx == end_separator_idx - 1)) and \
                not _is_email(word_to_evaluate):
            text = text[:period_idx] + ' .\n' + text[period_idx + 1:]
            period_idx += 1

        period_idx = text.find('.', period_idx + 1)

    return text


def _load_words(filename, lowercase=False):
    words_set = set()

    if filename != '':
        with open(filename, 'r', encoding='utf8') as words_file:
            words_lines = words_file.readlines()
            for word in words_lines:
                if lowercase:
                    word_to_add = word.lower().strip()
                else:
                    word_to_add = word.strip()

                words_set.add(word_to_add)

    return words_set


def _load_contractions(filename):
    contractions_dict = {}

    if filename != '':
        with open(filename, 'r', encoding='utf8') as contractions_file:
            contractions_lines = contractions_file.readlines()
            for contraction in contractions_lines:
                contraction_list = re.split('([\w]+) +\+ +([\w]+) += +([\w]+)', contraction)

                contraction_list_filtered = list(filter(None, contraction_list))

                contractions_dict[contraction_list_filtered[2]] = contraction_list_filtered[0:2]

    return contractions_dict


def _split_text_in_sentences(text, abbreviations_set):
    text_processed = _find_real_periods_in_text(text, abbreviations_set)

    sentences = re.split('\n', text_processed)

    return list(sentences)


def _split_sentence_in_words(sentence, contractions_dict, expand_contractions):
    word_list = re.split('[ ]+|(\S{0,2}\$)|(?<![0-9])([\-]+)|(?<![0-9])(:)|([\.]{2,})|(?<![0-9])(,)|(,)(?![0-9])|([?!;\'\"\(\)\[\]])|([\w]+)(/)([\w]+)', sentence)

    word_list_filtered = list(filter(None, word_list))

    if expand_contractions:
        word_list_final = []
        for word in word_list_filtered:
            if word.lower() in contractions_dict.keys():
                contraction_words = contractions_dict[word.lower()]

                if word.isupper():
                    words_to_append = [contraction_word.upper() for contraction_word in contraction_words]
                elif word.istitle():
                    words_to_append = [contraction_words[0].title()] + contraction_words[1:]
                else:
                    words_to_append = contraction_words
            else:
                words_to_append = [word]

            word_list_final.extend(words_to_append)
    else:
        word_list_final = word_list_filtered

    return word_list_final


def _tokenize_text(text, expand_contractions=True):
    abbreviations_set = _load_words(__abbreviations_filename, lowercase=True)
    contractions_dict = _load_contractions(__contractions_filename)

    tokenized_text = []

    text_simplified = re.sub('[\n\t]', ' ', str(text))
    text_simplified += ' '

    sentence_list = _split_text_in_sentences(text_simplified, abbreviations_set)
    for sentence in sentence_list:
        tokenized_sentence = _split_sentence_in_words(sentence, contractions_dict, expand_contractions)

        if len(tokenized_sentence) < 1:
            continue

        tokenized_text.extend(tokenized_sentence)
        tokenized_text.extend([''])

    return tokenized_text


def _preprocess_tokenized_text(token_list, lowercase=True, stemmize=True, remove_stopwords=True,
                               strip_accents=True, min_word_length=True):

    stopwords = _load_words(__stopwords_filename, lowercase=True)
    stemmer = SnowballStemmer("portuguese")

    preprocessed_token_list = []

    for token in token_list:
        token_preprocessed = token

        if remove_stopwords:
            if token.lower() in stopwords:
                continue

        if min_word_length:
            if len(token_preprocessed) < 3 and \
                    len(token_preprocessed) > 0 and \
                    re.search('[0-9]|[^\w]', token_preprocessed) is None:
                continue

        if lowercase:
            token_preprocessed = token_preprocessed.lower()

        if stemmize:
            token_preprocessed = stemmer.stem(token_preprocessed)

        if strip_accents:
            token_preprocessed = unicodedata.normalize('NFD', token_preprocessed)
            token_preprocessed = token_preprocessed.encode('ascii', 'ignore').decode('ascii', 'ignore')

        if len(token_preprocessed) == 0:
            continue

        preprocessed_token_list.append(token_preprocessed)

    return preprocessed_token_list
