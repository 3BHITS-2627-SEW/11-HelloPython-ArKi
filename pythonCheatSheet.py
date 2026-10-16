# Datei: pythonCheatSheet.py
# Ausführen: python pythonCheatSheet.py / py pythonCheatSheet.py


# Die ist ein kleines Cheat-Sheet für die Verwendung von Python für C & C++ Programmierer

#Variablen
from turtle import color


eineVariable = 13
print("eineVariable:", eineVariable)
eineVariable = "Blablabla"
print("eineVariable:", eineVariable)

# Typisierung in Python: Ducktyping

eineZweiteVariable: int = 14
print("eineZweiteVariable:", eineZweiteVariable*3)
eineZweiteVariable = "Text"
print("eineZweiteVariable:", eineZweiteVariable*3)

datenTyp = type(eineVariable)
print("DatenTyp von eineVariable:", datenTyp)

print(f"Zahl lautet {eineVariable} und ist Cool!")

einString = str((eineVariable*2))
alternaitvText = "Zahl lautet"+einString+" und ist Cool!"
print(alternaitvText)

eingeleseneZahl = int(input("Bitte eine Zahl eingeben: "))
print("Eingelesene Zahl:", eingeleseneZahl)
print("Eingelesene Zahl DatenTyp:", type(eingeleseneZahl))