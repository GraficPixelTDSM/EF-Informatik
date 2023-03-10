# API'S

## Was ist eine API?
Eine API ist wie eine Website, aber designt dafür, dass ein Computer sie versteht. Es ist die Schnittstelle im Server, die die Menschliche Information in Computersprache übersetzt. Eine API kann aber noch viel mehr machen...
Der unterschied von einem Webserver zu einer API ist, dass die API einfacher für den Computer zu Interpretieren ist.

## JSON Format
Das JSON Format ist ein Speicherformat welches im Web häufig angewendet wird. Z.b.:
```json
{
    "kruste": "original",
    "belag": ["käse", "wurst", "knoblauch"],
    "status": "vorbereiten"
}
```
Mit diesem Dateiformat kann man sogenannte `Keys` und `Values` mitgeben. Diese können von einer API ausgelesen serden.

Im Beispiel ist `kruste` der `Key` und `original` der `Value`.

## XML Format
Das XML Format ist ähnlich wie das JSON format, jedoch älter, dadurch aber auch Stärker. Hier ein ähnliches Beispiel: 
```xml
<bestellung>
    <kruste>original</kruste>
    <belag>
        <belag>cheese</belag>
        <belag>pepperoni</belag>
        <belag>garlic</belag>
    </belag>
    <status>cooking</status>
</bestellung>
```
`<kruste>` ist die sogenannte `Node Opening Tag`, `Original` ist der Value und `</kruste>`ist der `Node Closing Tag`. 

## HTTP Request:
Ein HTTP Request wird generiert, wenn ein Webserver Aufgerufen wird. Ein solcher Request kann auch von einer API durchgeführt werden.

Damit ein solcher Request funktioniert, müssen ein paar Bedingungen erfüllt sein.

- ### URL
    - Die URL ist die Einzigartige Adresse eines Servers.
    - Sie wird benötigt um den korrekten Server zu finden

- ### Methoden
    - Es gibt verschiedene Methoden, die man bei einem HTTP Reques verwenden kann.
    - GET wird verwendet, wenn wir eine Resource vom Server erhalten wollen
    - POST wird verwendet, wenn der Server eine neue Resource erstellen soll
    - PUT wird verwendet um eine bestehende Resource zu Updaten
    - DELETE wird verwendet, um eine Resource vom Server zu löschen

- ### Headers
    - Headers werden verwendet, um Meta-Information mitzugeben
    - Z.b. Wird im Header mitgegeben, was du für ein gerät verwendest, damit die Website optimal aussieht

- ### Body
    - Der Body beinhaltet kurz gesagt den Inhalt der Website
    - Im HTML format, wird zuoberst `<body>`deklariert. Dies ist der gesamte inhalt.

## HTTP Status Codes
Es gibt verschiedene Statuscodes. `200` Bedeutet Erfolg, während `404` bedeutet, dass die Seite nicht gefunden wurde. Der Statuscode beschreibt, in welchem Zustand sich der Server befindet.

## Endpunkte
Der Endpunkt ist das Ende der Reise. Dort steht ein Server / Computer, der nun nach Protokoll reagieren kann.

## Polling
Beim Polling fragen wir den Server nach Updates, damit wir wissen, wie sich z.b. unser Pizza entwickelt.