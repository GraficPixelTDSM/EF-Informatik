# X = Y 

## Problem:
!!!Das folgende ist nur auf Listen anwendbar!!!  
  
Angenommen wir setzen in einem Code die Variable y mit `y = 5` auf den Wert 5.  
Wenn man jetzt `x = y` in einem Code schreibt, übernimmt x zu diesem Zeitpunkt den Wert von y, also 5.  
Wenn man danach aber den Wert für y verändert z.B. durch `y = y + 1`, wird man beim Drucken beider Variabeln folgendes erhalten:  
`x = 6`  
`y = 6`  
Vielleicht ist man jetzt überrascht, dass x nicht mehr 5 ist. Wir haben ja `x = y` gesetzt, als y noch 5 war und wir haben nur y verändert aber nicht x.  
  
## Erklärung:
Wenn man wie in unserem Beispiel `x = y` setzt, könnte man denken, dass x den aktuellen Wert zum aktuellen Zeitpunkt kopiert, also übernimmt.  
Dem ist aber nicht so. Wir erstellen lediglich eine Referenz von x zu y.  
Wenn sich y jetzt verändert, verändert sich auch x. 