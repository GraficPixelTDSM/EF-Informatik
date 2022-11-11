'''
Demo zu Referenzen.
'''
# Erklärung zu den verwendeten Funktionen:
# id(a)   - Gibt die eindeutige Identität des Objektes, welches an a hängt zurück. Jedes Objekt hat seine eigene Identität.
#           So kann man Objekte unterscheiden, selbst wenn sie den selben Inhalt haben.
# type(a) - Gibt an von welchem Datentyp (class) das Objekt ist, welches an a hängt. Jedes Objekt hat einen Datentyp, welcher bestimmt,
#           welche Werte in diesem Objekt gespeichert sein können (z.B. int für ganze Zahl, str für Text, etc.)

# Variablen a und b sind mit einem Objekt vom Typ int (ganze Zahl) verbunden, welches den Wert 10 enthält
a = 10
b = a
print(a, id(a), type(a))  # id(a)
print(b, id(b), type(b))  # id(b)

# Verändern von Variable b hat keinen Einfluss auf a
b = b + 1
print(a, id(a))
print(b, id(b))

# Jetzt werden die int-Objekte an a und b durch eine Liste ersetzt. Beide Variablen führen zum selben list-Objekt.
# Nicht verwirren lassen: Im Debugger sieht es aus, wie wenn a und b zwei verschiedene Objekte wären. Dem ist nicht so!
a = [1, 2, 3]
b = a
print(a, id(a), type(a))
print(b, id(b), type(b))

# Verändern des Elementes mit Index 1. Weil a und b mit ein und dem selben list-Objekt zusammenhängen, ist die Änderung
# über a und b zu sehen --> Beachten Sie, wie das im Debugger dargestellt wird!
b[0] = b[0] + 1
print(a, id(a))
print(b, id(b))
print(b[0], id(b[0]))
print(b[1], id(b[1]))

# Jetzt werden die list-Objekte durch ein str-Objekt ersetzt. Weil beide Texte gleich sind, gibt es nur ein Objekt und
# a und b sind mit diesem einen Objekt verbunden.
a = 'blahblah'
b = 'blahblah'
print(a, id(a), type(a))
print(b, id(b), type(b))

# Verändern des Textes an b: b wird mit einem neuen str-Objekt verbunden, welches den Text in Grossbuchstaben enthält
b = b.upper()
print(a, id(a))
print(b, id(b))
