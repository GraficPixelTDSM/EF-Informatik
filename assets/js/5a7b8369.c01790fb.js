"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[202],{3905:(e,n,t)=>{t.d(n,{Zo:()=>u,kt:()=>m});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var p=r.createContext({}),d=function(e){var n=r.useContext(p),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},u=function(e){var n=d(e.components);return r.createElement(p.Provider,{value:n},e.children)},o={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},c=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,p=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),c=d(t),m=i,h=c["".concat(p,".").concat(m)]||c[m]||o[m]||a;return t?r.createElement(h,l(l({ref:n},u),{},{components:t})):r.createElement(h,l({ref:n},u))}));function m(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,l=new Array(a);l[0]=c;var s={};for(var p in n)hasOwnProperty.call(n,p)&&(s[p]=n[p]);s.originalType=e,s.mdxType="string"==typeof e?e:i,l[1]=s;for(var d=2;d<a;d++)l[d]=t[d];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}c.displayName="MDXCreateElement"},7082:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>p,contentTitle:()=>l,default:()=>o,frontMatter:()=>a,metadata:()=>s,toc:()=>d});var r=t(7462),i=(t(7294),t(3905));const a={},l="NumTrip - Fertig",s={permalink:"/EF-Informatik/23-01-19-Das-Spiel-ist-fertig",editUrl:"https://github.com/GraficPixelTDSM/EF-Informatik/tree/main/blog/23-01-19-Das-Spiel-ist-fertig.md",source:"@site/blog/23-01-19-Das-Spiel-ist-fertig.md",title:"NumTrip - Fertig",description:"Einleitung",date:"2024-02-02T12:27:45.000Z",formattedDate:"2. Februar 2024",tags:[],readingTime:2.2,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"arbeiten-an-numtrip",permalink:"/EF-Informatik/22-12-02-arbeiten-an-numtrip"},nextItem:{title:"API erstellen",permalink:"/EF-Informatik/23-03-17-Erstellen-einer-API"}},p={authorsImageUrls:[]},d=[{value:"Einleitung",id:"einleitung",level:2},{value:"Zum Spiel Selbst",id:"zum-spiel-selbst",level:2},{value:"Was sind die Anforderungen an die Spielenden?",id:"was-sind-die-anforderungen-an-die-spielenden",level:2},{value:"Wie funktioniert das Erkennen gleicher Zahlen in Nachbarfeldern?",id:"wie-funktioniert-das-erkennen-gleicher-zahlen-in-nachbarfeldern",level:2},{value:"Entwicklungsherausforderungen",id:"entwicklungsherausforderungen",level:2},{value:"Meine Tipps",id:"meine-tipps",level:2}],u={toc:d};function o(e){let{components:n,...t}=e;return(0,i.kt)("wrapper",(0,r.Z)({},u,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"einleitung"},"Einleitung"),(0,i.kt)("p",null,"Endlich ist es so weit. Ich habe das Spiel fertig programmiert.\nIch bin mit meinem Resultat recht zufrieden, aber ich habe mir oft \xfcberlegt, hier und da mal ein kleines Feature einzubauen, dass ich dann aber gelassen habe."),(0,i.kt)("h2",{id:"zum-spiel-selbst"},"Zum Spiel Selbst"),(0,i.kt)("p",null,"Das Ziel ist es, die Zahl 128 in einem K\xe4stchen zu erreichen.",(0,i.kt)("br",{parentName:"p"}),"\n","Dann hat man gewonnen. Anschliessend wird man vom Spiel gefragt, ob man unbegrenzt weiterspielen will, oder nicht.",(0,i.kt)("br",{parentName:"p"}),"\n","Dann ist das Ziel des Spiels, eine m\xf6glichst hohe Punktzahl zu erreichen.",(0,i.kt)("br",{parentName:"p"}),"\n","Gl\xfccklicherweise speichert das Spiel nach jedem Zug und kann jederzeit geladen werden."),(0,i.kt)("h2",{id:"was-sind-die-anforderungen-an-die-spielenden"},"Was sind die Anforderungen an die Spielenden?"),(0,i.kt)("p",null,"Das Spiel wurde mit Python 3.10.6 geschrieben, d.h. kann man sich sicher sein, dass der Code mit dieser Version funktioniert.",(0,i.kt)("br",{parentName:"p"}),"\n","Es braucht also einen Code-Editor bzw. -Runner mit Python 3.10.6.  "),(0,i.kt)("h2",{id:"wie-funktioniert-das-erkennen-gleicher-zahlen-in-nachbarfeldern"},"Wie funktioniert das Erkennen gleicher Zahlen in Nachbarfeldern?"),(0,i.kt)("p",null,"Zuerst muss man ein Feld ausw\xe4hlen, von welchem der Algorithmus starten soll. Dessen Koordinate wird an die Liste 'check' angeh\xe4ngt.",(0,i.kt)("br",{parentName:"p"}),"\n","Dann vergleicht das Spiel die Zahl bei der ausgew\xe4hlten Koordinate (x, y), mit der Zahl, der Koordinate links / rechts / dar\xfcber / darunter ",(0,i.kt)("inlineCode",{parentName:"p"},"(x - 1, y)")," / ",(0,i.kt)("inlineCode",{parentName:"p"},"(x + 1, y)")," / ",(0,i.kt)("inlineCode",{parentName:"p"},"(x, y + 1)")," / ",(0,i.kt)("inlineCode",{parentName:"p"},"(x, y - 1)"),".  "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"anz1 = int(anzeige[y][x - 1].strip())  \nanz2 = int(anzeige[y][x].strip())  \nif anz2 == anz1:  \n")),(0,i.kt)("p",null,"Wenn das der Fall ist und die Zahl nicht == 0 ist, wird die Koordinate zu 'check' hinzugef\xfcgt und die Zahl = 0 gesetzt, damit sie nicht noch einmal gepr\xfcft wird und es zu einem loop kommt.  "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"    check[0].append(x + 1)\n    check[1].append(y + 2)\n    spiel[y + 1][x] = 0\n")),(0,i.kt)("p",null,"Das wird dann auch f\xfcr",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("inlineCode",{parentName:"p"},"anz1 = int(anzeige[y][x + 1].strip())"),",",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("inlineCode",{parentName:"p"},"anz1 = int(anzeige[y - 1][x].strip())")," und",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("inlineCode",{parentName:"p"},"anz1 = int(anzeige[y + 1][x].strip())")," wiederholt.  "),(0,i.kt)("h2",{id:"entwicklungsherausforderungen"},"Entwicklungsherausforderungen"),(0,i.kt)("p",null,"Das mit dem Speichern ist so eine Sache... Wenn man es implementiert, bevor man den ganzen Code geschrieben hat, muss man noch sehr viel umschreiben und verschieben. Dann fehlen einige Variablen, die nicht existieren, dann muss man mit ",(0,i.kt)("inlineCode",{parentName:"p"},"try;except")," arbeiten...",(0,i.kt)("br",{parentName:"p"}),"\n","*aufatmen","*"," Ja es ist kompliziert mit dem Speichern und Laden."),(0,i.kt)("h2",{id:"meine-tipps"},"Meine Tipps"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Implementiert speichern und laden erst am Schluss."),(0,i.kt)("li",{parentName:"ul"},"Gebt Variablen Namen, aus denen man ableiten kann, wof\xfcr sie stehen."),(0,i.kt)("li",{parentName:"ul"},"Speichert vor dem Ausf\xfchren. Manchmal hat es den Code nicht gespeichert, als ich ihn ausgef\xfchrt habe und das Programm hat mir einen Fehler angezeigt, den ich schon gel\xf6st habe,... nur nicht gespeichert."),(0,i.kt)("li",{parentName:"ul"},"Schreibt zu schwierigen Codeelementen und Variablen die einen versteckten Nutzen haben Text, der beschreibt, was sie tun."),(0,i.kt)("li",{parentName:"ul"},'Denkt auch in eurer Freizeit \xfcber euren Code nach. Vielleicht kommt euch ein "Heureka"-Moment indem ihr eine grandiose Idee habt.')))}o.isMDXComponent=!0}}]);