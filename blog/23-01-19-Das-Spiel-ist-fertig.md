# NumTrip - Fertig
## Einleitung
Endlich ist es so weit. Ich habe das Spiel fertig programmiert.
Ich bin mit meinem Resultat recht zufrieden, aber ich habe mir oft überlegt, hier und da mal ein kleines Feature einzubauen, dass ich dann aber gelassen habe.
## Zum Spiel Selbst
Das Ziel ist es, die Zahl 128 in einem Kästchen zu erreichen.  
Dann hat man gewonnen. Anschliessend wird man vom Spiel gefragt, ob man unbegrenzt weiterspielen will, oder nicht.  
Dann ist das Ziel des Spiels, eine möglichst hohe Punktzahl zu erreichen.  
Glücklicherweise speichert das Spiel nach jedem Zug und kann jederzeit geladen werden.
## Was sind die Anforderungen an die Spielenden?
Das Spiel wurde mit Python 3.10.6 geschrieben, d.h. kann man sich sicher sein, dass der Code mit dieser Version funktioniert.  
Es braucht also einen Code-Editor bzw. -Runner mit Python 3.10.6.  
## Wie funktioniert das Erkennen gleicher Zahlen in Nachbarfeldern?
Zuerst muss man ein Feld auswählen, von welchem der Algorithmus starten soll. Dessen Koordinate wird an die Liste 'check' angehängt.  
Dann vergleicht das Spiel die Zahl bei der ausgewählten Koordinate (x, y), mit der Zahl, der Koordinate links / rechts / darüber / darunter `(x - 1, y)` / `(x + 1, y)` / `(x, y + 1)` / `(x, y - 1)`.  
```py
anz1 = int(anzeige[y][x - 1].strip())  
anz2 = int(anzeige[y][x].strip())  
if anz2 == anz1:  
```
Wenn das der Fall ist und die Zahl nicht == 0 ist, wird die Koordinate zu 'check' hinzugefügt und die Zahl = 0 gesetzt, damit sie nicht noch einmal geprüft wird und es zu einem loop kommt.  
```py
    check[0].append(x + 1)
    check[1].append(y + 2)
    spiel[y + 1][x] = 0
```
Das wird dann auch für  
`anz1 = int(anzeige[y][x + 1].strip())`,  
`anz1 = int(anzeige[y - 1][x].strip())` und  
`anz1 = int(anzeige[y + 1][x].strip())` wiederholt.  
## Entwicklungsherausforderungen
Das mit dem Speichern ist so eine Sache... Wenn man es implementiert, bevor man den ganzen Code geschrieben hat, muss man noch sehr viel umschreiben und verschieben. Dann fehlen einige Variablen, die nicht existieren, dann muss man mit `try;except` arbeiten...  
*aufatmen\* Ja es ist kompliziert mit dem Speichern und Laden.
## Meine Tipps
- Implementiert speichern und laden erst am Schluss.
- Gebt Variablen Namen, aus denen man ableiten kann, wofür sie stehen.
- Speichert vor dem Ausführen. Manchmal hat es den Code nicht gespeichert, als ich ihn ausgeführt habe und das Programm hat mir einen Fehler angezeigt, den ich schon gelöst habe,... nur nicht gespeichert.
- Schreibt zu schwierigen Codeelementen und Variablen die einen versteckten Nutzen haben Text, der beschreibt, was sie tun.
- Denkt auch in eurer Freizeit über euren Code nach. Vielleicht kommt euch ein "Heureka"-Moment indem ihr eine grandiose Idee habt.

