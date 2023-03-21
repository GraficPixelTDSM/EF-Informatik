"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[528],{3905:(e,n,t)=>{t.d(n,{Zo:()=>l,kt:()=>p});var i=t(7294);function r(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);n&&(i=i.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,i)}return t}function s(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){r(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function o(e,n){if(null==e)return{};var t,i,r=function(e,n){if(null==e)return{};var t,i,r={},a=Object.keys(e);for(i=0;i<a.length;i++)t=a[i],n.indexOf(t)>=0||(r[t]=e[t]);return r}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(i=0;i<a.length;i++)t=a[i],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(r[t]=e[t])}return r}var c=i.createContext({}),u=function(e){var n=i.useContext(c),t=n;return e&&(t="function"==typeof e?e(n):s(s({},n),e)),t},l=function(e){var n=u(e.components);return i.createElement(c.Provider,{value:n},e.children)},d={inlineCode:"code",wrapper:function(e){var n=e.children;return i.createElement(i.Fragment,{},n)}},m=i.forwardRef((function(e,n){var t=e.components,r=e.mdxType,a=e.originalType,c=e.parentName,l=o(e,["components","mdxType","originalType","parentName"]),m=u(t),p=r,k=m["".concat(c,".").concat(p)]||m[p]||d[p]||a;return t?i.createElement(k,s(s({ref:n},l),{},{components:t})):i.createElement(k,s({ref:n},l))}));function p(e,n){var t=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var a=t.length,s=new Array(a);s[0]=m;var o={};for(var c in n)hasOwnProperty.call(n,c)&&(o[c]=n[c]);o.originalType=e,o.mdxType="string"==typeof e?e:r,s[1]=o;for(var u=2;u<a;u++)s[u]=t[u];return i.createElement.apply(null,s)}return i.createElement.apply(null,t)}m.displayName="MDXCreateElement"},2615:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>s,default:()=>d,frontMatter:()=>a,metadata:()=>o,toc:()=>u});var i=t(7462),r=(t(7294),t(3905));const a={},s="Login-Seite",o={unversionedId:"netzwerke/login-cookies",id:"netzwerke/login-cookies",title:"Login-Seite",description:"I - Was ist ein Cookie",source:"@site/docs/netzwerke/login-cookies.md",sourceDirName:"netzwerke",slug:"/netzwerke/login-cookies",permalink:"/EF-Informatik/docs/netzwerke/login-cookies",draft:!1,editUrl:"https://github.com/GraficPixelTDSM/EF-Informatik/tree/main/docs/netzwerke/login-cookies.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"API'S",permalink:"/EF-Informatik/docs/netzwerke/apis"},next:{title:"Numtrip Datenstruktur",permalink:"/EF-Informatik/docs/numtrip/datenstruktur"}},c={},u=[{value:"I - Was ist ein Cookie",id:"i---was-ist-ein-cookie",level:2},{value:"II - Weshalb ist ein Cookie praktisch? Wie funktioniert ein Login damit?",id:"ii---weshalb-ist-ein-cookie-praktisch-wie-funktioniert-ein-login-damit",level:2},{value:"III - Unser Beispiel benutzt eine einfache Benutzerdatenbank. Was darf NIE so gemacht werden, wie wirs gemacht haben? Welche Ans\xe4tze gibts zur Verbesserung?",id:"iii---unser-beispiel-benutzt-eine-einfache-benutzerdatenbank-was-darf-nie-so-gemacht-werden-wie-wirs-gemacht-haben-welche-ans\xe4tze-gibts-zur-verbesserung",level:2}],l={toc:u};function d(e){let{components:n,...a}=e;return(0,r.kt)("wrapper",(0,i.Z)({},l,a,{components:n,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"login-seite"},"Login-Seite"),(0,r.kt)("h2",{id:"i---was-ist-ein-cookie"},"I - Was ist ein Cookie"),(0,r.kt)("p",null,"Ein Cookie ist ein kleines St\xfcck Text, das von einem Webserver generiert und an einen Webbrowser bzw. ein Ger\xe4t gesendet wird. Der Browser bzw. das Ger\xe4t speichert die empfangenen Cookies f\xfcr eine vorbestimmte Zeit oder f\xfcr die Dauer einer Benutzersitzung auf einer Website. Bei zuk\xfcnftigen Anfragen des Benutzers an den Webserver werden die relevanten Cookies angeh\xe4ngt."),(0,r.kt)("h2",{id:"ii---weshalb-ist-ein-cookie-praktisch-wie-funktioniert-ein-login-damit"},"II - Weshalb ist ein Cookie praktisch? Wie funktioniert ein Login damit?"),(0,r.kt)("p",null,"Ein Cookie kann Daten, wie Passwort und Benutzernamen speichern. Bei einem erneuten Aufrufen der Seite, erkennt die Seite das Cookie und kann die Daten (Passwort, Benutzername) direkt ablesen. Der Benutzer muss sich nicht jedes mal erneut einloggen, da der Server die Arbeit danks des Cookies \xfcbernimmt.  "),(0,r.kt)("h2",{id:"iii---unser-beispiel-benutzt-eine-einfache-benutzerdatenbank-was-darf-nie-so-gemacht-werden-wie-wirs-gemacht-haben-welche-ans\xe4tze-gibts-zur-verbesserung"},"III - Unser Beispiel benutzt eine einfache Benutzerdatenbank. Was darf NIE so gemacht werden, wie wirs gemacht haben? Welche Ans\xe4tze gibts zur Verbesserung?"),(0,r.kt)("p",null,"Es k\xf6nnen unendlich viele Benutzer erstellt werden, in k\xfcrzester Zeit. Das kann die Datenbank schnell auslasten. Man k\xf6nnte ein Cookie dauerhaft speicher und somit sagen, dass nur eine bestimmte Anzahl an Accounts pro Ger\xe4t zul\xe4ssig sind, man k\xf6nnte das gleiche Konzept aber auch mit der IP verfolgen. Andererseits kann man auch eine E-Mail-Authentifizierung einf\xfchren.",(0,r.kt)("br",{parentName:"p"}),"\n","Ein weiteres Sicherheitsproblem ist auch die Accountsicherheit. Erstens: Es gibt keine 2FA, Zweitens: Wenn man die Cookiedaten mit den Entwicklertools \xe4ndert, kann man sich auf jeden Account anmelden, solange man nur den Benutzernamen kennt.",(0,r.kt)("br",{parentName:"p"}),"\n","Man muss nur die Variable ",(0,r.kt)("inlineCode",{parentName:"p"},"name")," gleich den Benutzernamen der Person setzen, in dessen Account man rein will, anschliessend muss man noch eine zweite Variable ",(0,r.kt)("inlineCode",{parentName:"p"},"auth")," gleich ",(0,r.kt)("inlineCode",{parentName:"p"},"true")," setzen. Anschliessend muss man die Seite neu laden und man ist im Account drin.",(0,r.kt)("br",{parentName:"p"}),"\n",(0,r.kt)("img",{src:t(7741).Z,width:"707",height:"370"}),(0,r.kt)("br",{parentName:"p"}),"\n","Das Passwort k\xf6nnte man als Hash auf dem Server speichern und das normale Passwort im Cookie speichern. Dann muss man nur noch das Cookie-Passwort hashen und mit dem Server abgleichen."))}d.isMDXComponent=!0},7741:(e,n,t)=>{t.d(n,{Z:()=>i});const i=t.p+"assets/images/cookiesF12-8d5c9fa59683f990357e9c890665365c.png"}}]);