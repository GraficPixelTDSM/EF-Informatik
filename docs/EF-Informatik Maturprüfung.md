# Schriftliche Matur

# Programmieren / Software-Engineering

* Top-Down / Bottom Up Entwürfe, Divide & Conquer  
    * Divide & Conquer:  
    Teile und Herrsche heisst, ein Problem, welches schwer zu lösen ist in kleinere Probleme aufteilen um diese vielleicht einfacher zu lösen. Dafür wird in der Informatik meistens eine Kombination zwischen Top-Down und Bottom-Up verwendet.  
    ![](images/DivAndConq.png)
    * Top-Down:  
    Ein grosses Problem wird so häufig in kleinere Teilprobleme geteilt, bis man zu den einzelnen Problemen Funktionen schreiben kann um diese zu lösen. Anschliessend werden die einzelnen Funktionen zusammengeführt, sodass das grosse Problem gelöst ist.  
    * Bottom-up:  
    Hier beginnt man zuerst unten. Das heisst man versucht von Anfnag an die kleinen Probleme zu lösen um sie dann zusammenzufügen, damit ein grösseres Problem gelöst ist. Hier kann es aber passieren, dass man eine ungüsntige Aufteilung in Teilprobleme erhält.  
    

* Programm-Code (Python) lesen & verstehen
  * nochmals NumTrip durchgehen
  * Alte Prüfungen, insb. praktischen 
* Wie funktioniert Python?
  * Scopes? `global`, Unterschied von "Pass by Value" und "Pass by Reference"?

```python
name = 'Marc'
def say_hi(name): # Argument: die übergebene """"Variable""""
  print(f'Hello {name}')
  
say_hi('Reto')

def greet_class(names):
  print(f'Hello everybody! {names}')
  names[0] = 'Maria'
  names = ['Bello']
 
ef = ['Timon', 'Lia']
greet_class(ef)
print(ef)
```

* Fehlerbehandlung / Benutzereingabe
  * `a = int(input('Dein Alter?')`)
* Arbeiten in Teams:
  * Versionsverwaltung Git
* Datenstrukturen
  * 1D, 2D, 3D, nD Listen


***

# Datenbanken / Webapps / API

* ER Diagramme, Kardinalitäten, Zwischentabellen, Primary Key, Foreign Key  
    * ER Diagramme:  
      Entity-Relationship-Diagramme beschreiben Entitäten, Attribute, Beziehungen und Kardinalitäten. Zuerst werden die Entitäten bestimmt.

      ![](images/erdiagrammBeispiel.png)
    * Entität:  
    Ein Objekt au der Realsituation, über das Informationen zu speichern sind. Entitäten sind z.B. Verlag oder Buch. Entitäten werden auf ER-Diagrammen als Rechteck dargestellt.
    * Attribut:  
    Attribute beschreiben Eigenschaften von Entitäten oder Beziehungen. Bei einem Buch könnte das z.B. der Titel, der Preis etc. sein. Attribute werden auf ER-Diagrammen als Elypsen dargestellt. 
    * Beziehung:  
    Sie beschreiben den Zusammenhang zwischen Entitäten. Die Entität "Verlag" hat zur Entität "Buch" die Beziehung "veröffentlicht". Beziehungen werden im ER-Diagramm als Rauten dargestellt. 
    * Kardinalitäten:  
      BEschreibt wie viele Entitäten einer Entitätsmenge an einer konkreten Beziehung beteiligt werden müssen / können. Es gibt die Kardinalitäten 1 (kein oder ein) und m bzw. n (kein, ein, mehrere). Damit sind folgende Beziehungsarten möglich:
        * 1:1  
        Bsp.: Jedes Buch hat genau eine Darstellung, eine Darstellung bezieht sich immer auf das gleiche Buch
        * 1:n  
        Bsp.: Ein Buch wurde von einem Verlag veröffentlicht, ein Verlag kann beliebig viele Bücher veröffentlichen
        * m:n  
        Bsp.: Ein Buch kann von beliebig vielen Menschen bestellt werden, ein Mensch kann beliebig viele Bücher bestellen
    * Zwischentabellen:  
      
    * Primary Key:  
      Jede Entitätsmenge erhält einen Primärschlüssel. Er ist nie gleich. Bei den Büchern kann das die ISBN sein, die pro Buch nur einmal vergeben wird. Der Primärschlüssel wird doppelt unterschrichen. 
    * Foreign Key:  

* Normalisierung, 3 NF
    * Normalisierung:  
      Dabei wird eine Datenbank, dessen Daten weniger gut strukturiert sind, so neu strukturiert, dass Redundanzen ausgeschlossen werden können, aber keine Daten verloren gehen.  
![](images/tabelleNF0.png)
    * NF 1:  
      Alle Attribute weisen einen atomaren Wertebereich auf. Das heisst, sie sind so kleine wie möglich gemacht.  
![](images/tabelleNF1.png)
    * NF 2:  
      Die Tabelle muss in NF 1 sein und jedes Nichtschlüsselattribut muss voll funktional abhängig vom Primärschlüssel sein.  
![](images/tabelleNF2_1.png)  
![](images/tabelleNF2_2.png) ![](images/tabelleNF2_3.png)
    * NF 3:  
    Die Tabelle muss in der NF 2 sein und es darf keine funktionalen Abhängigkeiten zwischen Nichtschlüsselattributen geben.  
![](images/tabelleNF2_1.png)
![](images/tabelleNF3_1.png) ![](images/tabelleNF3_2.png)
       
* HTTP-Requests, Web-API (GET, POST, UPDATE, DELETE)
    * HTTP-Request:  
      Sind Anfragen von einem Client an einen HTTP-Server.
    * Web-API:  
      API's sind Versionen der Webseite, die ein Server lesen kann. Dabei werden unnötige Daten wie Bilder ignoriert und andere Daten wie Jahrgang eines Filmes werden so dargestellt, dass sie einfach abrufbar sind (name = 'Titanic')
        * GET: wird verwendet um eine Ressource anzufordern
        * POST: wird verwendet um eine Ressource zu erschaffen 
        * PUT: wird verwendet um eine Ressource zu ersetzen oder zu erneuern
        * DELETE: wird verwendet um eine Ressource zu löschen
* Cookie, Anmeldedaten, speichern auf Server/DB —> Hash
    * Cookie:  
      Sind kleine Textdateien die lokal gespeichert werden. Kehrt man auf eine Seite zurück, kann diese das Gerät anhand der Cookies erkennen. 
    * Anmeldedaten:  
      Anmeldedaten sind z.B. Nutzername und Passwort
    * Speicherung auf Servern / DB -> Hash
      Beim erstellen eines Kontos wird das Passwort neben dem Benutzernamen auf einem Server gespeichert. Will man sich einloggen ruft die Internetseite den Server ab und prüft, ob das eingegebene Passwort mit dem gespeicherten übereinstimmt. Dameit bei einem Datenleck aber nicht alle Passwörter veröffentlicht werden, werden die Passwörter als Hash gespeichert. Man kann aus einem Hash den Ursprung nicht ableiten. Das eingegebene Passwort wird auch Gehasht und mit dem Server-gehashten Passwort verglichen. 
* SQL-Abfragen:
    * Lesen: alles behandelte (inkl. `Joins`, `Group By`, `SUM`)  
    ```sql
    SELECT
    [DISTINCT]
    Auswahlliste
    FROM Quelle [Alias-Name]
    [WHERE Where-Klausel]
    [ [GROUP BY {Group-by-Attribut}] +
        [HAVING Having-Klausel]]
    [ORDER BY {Sortierungsattribut [ASC|DESC]}
    [LIMIT {Datensatz-Anzahl}];
    ```
    wobei alles, was in eckigen Klammern steht, optional ist.


    `DISTINCT`
    : Jeder Datensatz wird nur einmal ausgegeben, auch wenn er mehrfach in der Tabelle vorkommt.  

    `Auswahlliste`
    : Bestimmt, welche Attribute (Spalten) der Quelle angezeigt werden sollen (`*` für alle) und ob Aggregationsfunktionen angewendet werden sollen. Aufgezählte Elemente sind mit einem *Komma* voneinander getrennt.  

    `Quelle [Alias-Name]`
    : Spezifiziert, wo die Daten herkommen. Es können Relationen angegeben werden und miteinander als kartesisches Produkt oder als Verbund (`JOIN`) verknüpft werden. Durch die Angabe eines *Alias-Namen* können die Relationen für die Abfrage umbenannt werden.  

    `Where-Klausel` 
    : Bestimmt die Bedingungen, unter denen die Daten ausgegeben werden sollen. Einzelne Bedingungen können mit `OR` oder `AND` verknüpft werden.  

    `Group-by-Attribut`
    : Legt fest, ob unterschiedliche Werte als einzelne Zeilen ausgegeben werden sollen oder ob alle Attributwerte aggregiert (bspw. aufsummiert (`SUM`), gemittelt (`AVG`), kleinster Wert (`MIN`), grösster Wert (`MAX`),...) zu einem einzelnen Ergebniswert zusammengefasst werden.   

    `Having-by-Attribut`
    : Ist wie die `WHERE`-Klausel, nur dass sich die angegebenen Bedingungen auf das Ergebnis einer Aggregationsfunktion beziehen.  

    `Sortierungsattribut`
    : Nach dem `ORDER BY` Statement werden Attribute angegeben, nach denen sortiert werden soll. Für eine aufsteigende Reihenfolge (1, 2, 3, ...) wird `ASC` spezifiziert, für eine absteigende Reihenfolge `DESC` (99, 80, 13, ...).  

    `LIMIT`
    : Gibt an wie viele Datensätze angezeigt werden sollen. Besonders hilfreich bei grossen Datensätzen, oder wenn nur eine gewisse Anzahl der *grössten*/*kleinsten* Attributwerte gesucht werden.  

    weitere sql -> https://www.postgresql.org/docs/current/functions-string.html

    * Join  
Um Tabele zu verbinden kann folgende Abfrage getätigt werden:  
```sql
SELECT 
    a.name AS "Name", a.bild AS "Bild", b.name AS "Haustier", b.bild AS "Vorschau" 
FROM legodudes a, haustiere b
```
Damit aber jedes Haustier zu seinem Legodude kommt, kann man den Code um folgendes erweitern:  
```sql
SELECT 
    a.name AS "Name", a.bild AS "Bild", b.name AS "Haustier", b.bild AS "Vorschau" 
FROM legodudes a, haustiere b
WHERE a.id = b.legodude_id
ORDER BY a.name
```
Da solche Abfragen aber ein bisschen lange und unübersichtlich werden können kann man auch `Join` verwenden:  
```sql
SELECT 
    a.name AS "Name", a.bild AS "Bild", b.name AS "Haustier", b.bild AS "Vorschau" 
FROM legodudes a
  JOIN haustiere b ON a.id = b.legodude_id
ORDER BY a.name
```
  * Schreiben: klassische Abfragen mit `SELECT … FROM, *, COUNT,  DISTINCT, WHERE, LIMIT, ORDER BY ASC/DESC`  
    * (Siehe Webseite)
* SQL Injection
  * verstehen, erklären und ausnutzen  
Durch die Eingabe eines Befehls in ein Eingabefeld, welches direkten Zugriff auf die Datenbank hat, kann man Daten abrufen, verändern oder ganze Datenbanken löschen. Statt den Namen in das Textfeld einzugeben, was der eigentliche Gedanke wäre, gibt man einen Befehl ein:  
```sql
Thomas' OR 1=1;--
oder
'; drop DATABASE;--
```
Mit dem semikolon wird die erste Abfrage beendet und die nächste, eigene beginnt. Dabei kann man z.B. die ganze Datenbank löschen. Das nächste Semikolon beendet die Anfrage und die beiden Bindestriche sagen, dass der Rest nur Kommentar ist, sodass der restliche Teil des anfänglichen codes keinen Fehler verursacht.
  * wie verhindern
    * Keine Nutzereingabe
    * Nutzereingabe Sanitizen
    * SQL Prepared Statements (statt verketteten Strings -> SQL-Abfrage wird vorher vorbereitet und Benutzereingaben werden nachher eingefügt)
    * Verwenden von Whitelists, die nur bestimmte Eingaben erlauben
    * Verwenden von Parameter, die z.B. nur Zahlen erlauben

\*\*\*

# Netzwerke

* Aufbau IP-Adresse (IPv4), Sub-Netz Masken, Subnetze
    * IP-Adresse:  

    * Sub-Netz Masken:  

    * Subnetze:  

* Routing, Routing-Tabellen
    * Routing:  

    * Routing-Tabellen:  

* Schichtenmodell
    * [Einzelne Schichten]
* MAC-Adresse, NAT, ARP (Tabelle), DHCP, DNS
    * MAC-Adresse:  

    * NAT:  

    * ARP:  

    * DHCP:  

    * DNS:  

* Hole Punching (Firewall)  

* Netzwerk-Log interpretieren  


# Algorithmen

* Laufzeitabschätzungen mit O(n) Notation  

* Sortiere / Suchen (Insertion Sort, Selection Sort, Merge Sort)
    * Insertion Sort:  

    * Selection Sort:  

    * Merge Sort:  

* Dijkstra / Breitensuche durchführen mit OL/CL
    * Dijkstra:  

    * Breitensuche:  

        * OL / CL:  

* A\*  

* Algorithmus untersuchen in Bezug auf die Laufzeit  

* Rekursion, Stack  
    * Rekursion:  

    * Stack:  


# Robotik

* Event-State Tabellen, Event State Diagramme
    * ES Tabellen:  

    * ES Diagramme:  

* Texte lesen und zu Event-State Tabellen/Diagrammen überführen  

* Aktoren / Sensoren / Ereignisse / Transitionen  
    * Aktoren:  

    * Sensoren:  

    * Ereignisse:  

    * Transitionen:  

* Turing-Maschine  
    * Funktionsweise:  

    * Programmierung:  


* wie setzt man das in Python um? ( `if-elif-elif-…-else`)  


# Rechnerarchitektur

* Turingmaschine-Von-Neumann-Rechner:  

* LMC-Programme lesen, interpretieren, abändern:  

    * [VOLLSTÄNDIGER LMC BEFEHLSSATZ]

* Aufbau und Funktionsweise Von-Neumann-Rechner erklären  

    * Von-Neumann-Zyklus:  

    * Bussystem:  

* Logische Bausteine (Funktionsweise und Wahrheitstabellen):  
    * AND  

    * OR  

    * NOT  

    * XOR  

    * NAND  

    * NOR  

    * XNOR  

* Einfache logische Schaltungen interpretieren und deren Wahrheitstabellen erstellen

* Für gegebene Wahrheitstabellen logische Schaltungen erstellen  

* Unterschiede Von-Neumann- und Harvard-Architektur

* Umwandlung vom Menschenlesbaren Code in Maschinencode (Prozess und Beteiligungen)  
    * Compiler  

    * Assembler  

    * Linker  

    * Loader  

* Compiler-Optimierungen  
    * [ALLE NENNEN]  

* RISC / CISC
    * RISC  

    * CISC  
