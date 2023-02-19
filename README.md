# Tuorepuuro-reseptipankki
_(Tietokantasovellus-kurssi, kevät 2023)_


Sovellus tarjoaa käyttäjälle tuorepuuroreseptitietokannan, josta käyttäjä voi: 
- hakea reseptejä nimellä tai ainesosalla
- lukea reseptejä
- tykätä resepteistä, jolloin resepti tallentuu omien tykättyjen reseptien listaan
- kommentoida reseptejä
- antaa reseptille arvion (1-5 tähteä)
- syöttää tietokantaan oman tuorepuuroreseptin


## Tilanne 19.2.2022:

Sovelluksessa on seuraavat toiminnot:
- Uuden käyttäjän luominen
- Sisäänkirjauneen käyttäjän nimen näyttäminen main pagella
- Käyttäjän sisään- ja uloskirjautuminen
- Uuden smoothie-reseptin tallennus tietokantaan
- Viimeisimmän kantaan syötetyn reseptin näyttäminen main pagella
- Lista tietokannassa olevista resepteista (linkit varsinaisiin ohjeisiin puuttuvat)

Puuttuu:
- Toimiva reseptihaku
- Reseptin merkitseminen suosikiksi
- Reseptin arvostelu
- Viikon reseptin julkaiseminen
- Ulkoasun säätäminen
- Tietoturva-asioiden huomioonottaminen
- Ohjaavat virheilmoitukset ja virheiden käsittely tilanteissa, joissa käyttäjä yrittää käyttää sovellusta väärin


## Käyttöliittymä (luonnos)

![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/ui.jpeg)



## Tietokantataulut 
(alustava havainnekuva)

![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/tables.j

Sovelluksessa on seuraavat tietokantataulut:
- users
- favorites
- upvotes
- recipes
- comments
- recipe of the week
