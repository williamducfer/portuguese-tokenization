# Tokenization

Library to tokenize and preprocess texts
  written in Portuguese.
To use the library,
  it is necessary to execute the pip command below.
```bash
pip install -e git+https://github.com/williamducfer/portuguese-tokenization#egg=tokenization
```

To use the library in its simplest mode,
  it is necessary to execute the steps below.

```python
import tokenization

text = "Bem-vindo, este é um teste."

text_preprocessed = tokenization.preprocess_text(text)

print(text_preprocessed)

>>> ['bem', '-', 'vindo', ',', 'este', 'e', 'um', 'teste', '.', '']
```

Below we present the signature of _preprocess_text_ method.

```python
def preprocess_text(text,
                    lowercase=True,
                    remove_stopwords=False,
                    stemmize=False,
                    strip_accents=True,
                    expand_contractions=True, 
                    use_min_word_length=False, 
                    join_tokens_by_char=None)
```

The project also has two scripts to tokenize files
  from the console, _tokenize_files_in_dir.py_ and
  _tokenize_files_in_dir_for_eras_annotation_system.py_ (https://github.com/jonatasgrosman/eras).
They basically tokenize files contained in a
  dataset directory, and save them in an output 
  directory.
To understand the scripts more deeply,
  one has to call the scripts with _-h_ parameter
  from the command line
  as presented below.

```bash
python tokenize_files_in_dir.py -h
```
