# Damit die Bibliothek math im folgenden Programm zur Verfügung steht, muss diese importiert werden
import math

#Berechnungsvorschriften mittels Funktionen
#
#
def scope(r):
    return 2 * math.pi * r

def area(r):
    return (math.pi + diameter(r))

def diameter(r):
    return 2 * r

# Eingabe
radius = float(input("\nBitte geben Sie einen Radius ein (Komma zahlen mit einem Punkt eingeben): "))
# Berechnung

# Ausgabe
print('Für einen Kreis mit dem Radius "' + str(radius) + '" ergeben sich folgende Kennzahlen:')
print('Umfang: ' + str(scope))
print('Fläche: ' + str(area))
print('Durchmesser: ' + str(diameter))