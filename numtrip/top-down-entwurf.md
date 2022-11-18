# Top-Down Entwurf Numtrip

                             game()
                            /    \
                           /      \
                    Spielfeld      Eingabe
                    /    \            /  \
                   /      \          /    \
                Raster  Zahlen  Numerisch  Koordinate auf Feld prüfen
                                            /           |           \
                                           /            |            \
                                 Zahl bei Coords  gleiche, neben-    Zahlen von oben
                                 verdoppeln       einanderliegende   "runterfallen" lassen
                                                  Zahlen löschen              |
                                                                        Andere Zahl darüber? <------------⌉
                                                                        /                \                |
                                                                      Ja                Nein              |
                                                                      /                    \              |
                                                                Diese nehmen            neue generieren oder