from setuptools import setup

setup(name='tokenization',
      version='0.1',
      description='Tokenizes strings and text files',
      url='https://ada.ideias.inf.puc-rio.br:30000/datascience/tokenization',
      author='dslab',
      author_email='dslab-ideias@googlegroups.com',
      license='BSD License',
      packages=['tokenization'],
      install_requires=[
          'nltk',
          'six'
      ],
      python_requires='>=3.5',
      zip_safe=False)
