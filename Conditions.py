"""
Verzweigung in Python mittels if
Bei Python sind Einrückungen essentiell! Hiermit werden zusammengehörige Blöcke definiert. Alle eingerückten
Zeilen die aufeinander folgen (ggf. auch mit Leerzeilen dazwischen) werden demselben Anweisungsblock
hinzugerechnet. Bei anderen Programmiersprachen wird hier häufig mit geschweiften Klammern gearbeitet {}
"""

wert = 5

if wert < 6:
    print('Der Wert ist kleiner als 6')
    print('Auch diese Zeile ist von der Bedingung betroffen')
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')

wert = 6

if wert < 6:
    print('Der Wert ist kleiner als 6')
    print('Auch diese Zeile ist von der Bedingung betroffen')
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')

# Die neuste Version von Python (Version 3) kann ebenfalls mit geschweiften Klammern umgehen.
# Allerdings ist diese Schreibweise für Python absolut unüblich
# Des Weiteren besteht die Einschränkung, dass nur eine Anweisungszeile in den Klammern stehen darf
wert = 6
if wert < 6: {
print('Der Wert ist kleiner als 6')
}
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')



# if-else-Anweisung

# Wenn nun neben der Prüfung und dem DANN-Ergebnis auch noch der Teil WENN NICHT benötigt wird, so muss die
# if-Anweisung um einen else-Teil erweitert werden.

y = 5

if y == 4:
    print('y ist vier')
else:
    print('y ist nicht vier')

# Nun kann es aber auch sein, dass man mehrere Prüfungen vornehmen möchte. Dies lässt sich mit der if-elif-else-Syntax machen
y = 5

if y == 4:
    print('y ist vier')
elif y == 5:
    print('y ist fünf')
else:
    print('y ist weder vier noch fünf')

print('-----------------')

y = 3

if y == 4:
    print('y ist vier')
elif y == 5:
    print('y ist fünf')
else:
    print('y ist weder vier noch fünf')

# Folgende Fehler treten gerade am Anfang häufig auf:
# 1. Die Einrückungen werden falsch gesetzt. Diese sind allerdinsg für Python zwingend korrekt einzuhalten
# 2. statt elif wird elseif geschrieben
# 3. statt einem Vergleich mit == wird eine Zuweisung mit = versucht
# 4. Der Doppelpunkt am Ende einer Prüfungszeile fehlt
# 5. Es wurde nicht auf Groß-/Kleinschreibung geachtet. Python ist allerdings Case-Sensitive!