# python-unmotparjour
##### v1.0.0

Simple API Python to get random words with definition (from unmotparjour.fr) - French words

### Installation

`pip install python-unmotparjour`


### Usage

```python

from unmotparjour import UnMotParJour

for i in range(0, 5):
    result = UnMotParJour.get()
    print("# %s\n %s" % (result['word'], result['definition']))

```

or simply :

```python
>>> from unmotparjour import UnMotParJour
>>> print( UnMotParJour() )
```
```
# Théobromine

Nom féminin.
De « theobroma cacao » nom scientifique du cacaoyer. Du grec « theos » qui signifie dieu et  « broma » qui signifie nourriture.
En biochimie, nom de l’alcaloïde principal du cacao. On le trouve aussi dans le thé, le café et aussi la noix de cola.
La théobromine est un diurétique, un cardiotonique et un vasodilatateur des coronaires. 
```

