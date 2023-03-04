# Tuorepuuro-reseptipankki
_(Tietokantasovellus-kurssi, kevät 2023)_


Sovellus tarjoaa käyttäjälle tuorepuuroreseptitietokannan, josta käyttäjä voi: 
- hakea reseptejä nimellä, tyypillä tai ainesosalla
- lukea reseptejä
- tykätä resepteistä, jolloin resepti tallentuu omien tykättyjen reseptien listaan
- kommentoida reseptejä
- antaa reseptille arvion (1-5 tähteä)
- syöttää tietokantaan oman tuorepuuroreseptin


## Sovelluksen tilanne 4.3.2023:

Sovelluksessa on seuraavat toiminnot:
- Uuden käyttäjän luominen
- Käyttäjän sisään- ja uloskirjautuminen
- Uuden tuorepuuroreseptin tallennus tietokantaan
- Haku resepteistä tyypin, otsikon tai raaka-aineen perusteella
- Satunnaisen reseptin arpominen (osana hakutoimintoja)
- Lista tietokannassa olevista resepteista
- Reseptin merkitseminen suosikiksi
- Omien suosikkireseptien listaus
- Kommenttien näyttäminen reseptin yhteydessä
- Uuden kommentin lisääminen
- Admin-sivu, jossa on toistaiseksi yksi toiminto: viikon reseptin julkaiseminen
- Reseptin arvostelu (tähtiluokitus)


Puuttuu:
- Ulkoasun säätäminen
- Tietoturva-asioiden huomioonottaminen
- Ohjaavat virheilmoitukset ja virheiden käsittely tilanteissa, joissa käyttäjä yrittää käyttää sovellusta väärin


## Sovelluksen testaaminen

Lataa sovelluksen koodi oikean yläkulman vihreästä Code-napista (> Download zip). Pura zip-tiedosto omalle koneellesi. Lisää juurihakemistoon tiedosto .env ja kopioi sen sisällöksi seuraava:

```bash
DATABASE_URL=<oma local url>
SECRET_KEY=<satunnainen numerosarja>
```

Avaa terminaali ja siirry sovellustiedostokansioon. Luo virtuaaliympäristö ja siirry sinne seuraavilla käskyillä:
```bash
python3 -m venv venv
source venv/bin/activate
```

Luo tietokantataulut:

```bash
psql < schema.sql
```

Käynnistä sovellus terminaalissa käskyllä

```bash
flask run
```


## Käyttöliittymä (luonnos)

![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/ui.jpeg)



## Tietokantataulut 
(havainnekuva)

![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/tables.jpeg)

Sovelluksessa on seuraavat tietokantataulut:
- users
- favorites
- upvotes
- recipes
- comments
- recipe of the week
