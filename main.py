import re
import testParsing
from tkinter.filedialog import askopenfilename

locationTestDune=askopenfilename(title="Fichier de test dune",initialdir="c:\\Users\\conta\\Google Drive\\Matière\\AFIT\\antoine.adam\Source"
                                            "\\builtin\\tests",defaultextension=".ml",initialfile="test_builtin.ml",filetypes=[("Fichier test dune en .ml","test_*.ml")])
namefile=re.findall(r"test_([^\/\\]+)$",locationTestDune)[0]
print("\n"+namefile+":\n")
f = open(locationTestDune, "r")
textBrutTest=f.read()
matches = re.finditer(r"let (\S+)(?=_tests)[^\[]+(.+?)and",textBrutTest, re.MULTILINE | re.DOTALL)
for matchNum, match in enumerate(matches, start=1):
    name=match.group(1)
    tests=testParsing.parseDuneTest(re.sub('[\s+]', '', match.group(2)))
    print("-----===={"+name+"}====-----")
    print("Exécution en mode debug:")
    for e in tests:
        print(testParsing.createTestOcamlBool(name,e))
    print("\nExécution en mode normale:")
    for e in tests:
        print(testParsing.createTestOcamlPrint(name,e))
    print()
