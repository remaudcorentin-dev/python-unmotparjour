
from unmotparjour import UnMotParJour

for i in range(0, 5):
    result = UnMotParJour.get()
    print("# %s\n %s" % (result['word'], result['definition']))
