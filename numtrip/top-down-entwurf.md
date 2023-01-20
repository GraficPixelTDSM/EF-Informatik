# Top-Down Entwurf Numtrip




```
                                            main()    #1
                                              |
                                     ist Game_Over == 'True'?
                           ┌─────────────ja───┴───nein─────┐
                        Eingabe                            |
            ┌───────────┘     └─────┐                   Eingabe
        Prüfe die                   |             ┌─────┘     └─────┐ 
         Eingabe                    |         Prüfe die         Zu check() 
  (check_num_imput(inp))            |          Eingabe          hinzufügen
                                    |   (check_num_immput(inp))      |
                   ┌────────────────┘                            Ist gleiche    #2
     Weiterspielen? und möglich = 'True'                        Zahl daneben?
           ┌──ja───┴───nein─────┐                           ┌───ja───┴───nein────────────────────────────────────┐
   Game_Over = 'False' Zeige Shlussnachricht       ┌────────┴────────────┐                                  Ist '0' auf    #3
           |                 an            Verdopple anfangs       füge Zahlen daneben                     dem Spielfeld?
     Kehre zu #1                         gewählte Zahl einmalig    zu check() hinzu                 ┌────────ja──┴─nein──────────────────────┐
       zurück                                                            |                      Zuoberst?                               ist 128 auf
                                                                   Setze den Wert der       ┌──ja───┴───nein─────┐                    dem Spielfeld?
                                                                 Zahlen daneben auf '0'     |                    |               ┌──────ja───┴───nein─────┐
                                                                          |             Generiere eine      Nimm die Zahl    Game_Over = 'True'    Game_Over = 'False'
                                                                    Kehre zu #2        Neue Zahl dafür      darüber und          └───────────┬────────────┘
                                                                      zurück                |              setze sie = '0'            Drucke das Spielfeld
                                                                                            └───────┬────────────┘                      (field_print())
                                                                                                Kehre zu #3                                  |
                                                                                                  zurück                            ist ein Zug noch möglich?
                                                                                                                                ┌───────ja───┴───nein─────┐
                                                                                                                                |                 Game_Over = 'True'
                                                                                                                                └───────────┬─────────────┘
                                                                                                                                      Kehre zu #1
                                                                                                                                        zurück
```