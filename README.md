# Tuorepuuro-reseptipankki
_(Tietokantasovellus-kurssi, kevät 2023)_


Sovellus tarjoaa käyttäjälle tuorepuuroreseptitietokannan, josta käyttäjä voi: 
- hakea reseptejä nimellä, tyypillä tai ainesosalla
- lukea reseptejä
- tykätä resepteistä, jolloin resepti tallentuu omien tykättyjen reseptien listaan
- kommentoida reseptejä
- antaa reseptille arvion (1-5 tähteä)
- syöttää tietokantaan oman tuorepuuroreseptin


## Sovelluksen tilanne 5.3.2023 (kurssin loppupalautus):

**Sovelluksessa on seuraavat toiminnot:**
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


**Puuttuu:**
- Ulkoasun säätäminen
- Paljon pylintin ehdottamia korjauksia
- vieminen tuotantoon (fly.io)

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

Käynnistä sovellus terminaalissa seuraavalla käskyllä:

```bash
flask run
```

## Käyttöohje

Käynnistä sovellus ja luo uusi käyttäjätili klikkaamalla "Create it here" -linkkiä. Admin-tasoisen tilin luomiseen tarvitset admin key -avaimen, joka löytyy users.py -tiedoston alusta (rivi 11). Peruskäyttäjä-tiliä (user) luodessasi voit hättää admin key -kentän tyhjäksi.

Jos sinulla on jo käyttäjätunnukset, voit kirjautua suoraan sisään antamalla käyttäjätunnuksesi ja salasanasi.

Kun olet kirjautunut sisään, näet sovelluksen pääsivulla useita toimintopainikkeita:
- Add new recipe: lisää uusi resepti tietokantaan
- List af all recipes: listanäkymä kaikista tietokantaan lisätyistä tuorepuuroresepteistä
- Recipe search: haku tietokannasta reseptin otsikon, raaka-aineen tai tyypin perusteella (myös satunnaisen reseptin arpomiseen on nappi seikkailunhaluisille käyttäjille)
- My favorites: lista resepteistä, jotka olet merkannut suosikiksesi
- Admin tools: pääkäyttäjän työkalut (vaatii pääkäyttäjätasoisen käyttäjätilin)
- The recipe of the week: näyttää viimeisimmän 'viikon reseptin' (pääkäyttäjän julkaisema)
- The lates recipe: näyttää tietokantaan viimeisimmäksi lisätyn reseptin

Voit selata, arvostella ja kommentoida reseptejä, merkata niitä omiksi suosikeiksi ja lisätä omia reseptejä. Admin-oikeuksilla voi julkaista viikon reseptin ja tarvittaessa poistaa asiattomia kommentteja.

Uusia reseptejä lisätessäsi huomioithan, että reseptin nimi ei saa löytyä jo valmiiksi tietokannalta. Luontilomakkeella on täytettävät kaikki lomakkeen kohdat.

Testaaminen kannattaa aloittaa luomalla admin-tunnukset, lisäämällä tietokantaan muutama erityyppinen resepti ja sitten julkaisemalla yksi niistä viikon reseptinä. Näin kaikille sovelluksen toiminnoille löytyy dataa jota käsitellä.


## Käyttöliittymä

Tältä näytti sovelluksen ensimmäinen luonnostelu käyttöliittymäksi:

![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/ui.jpeg)

Lopputulos noudattelee suunnitelmaa suurimmaksi osaksi. Merkittävä muutos on, että jokainen sivupohja näytetään erillään ja valikko ei ole kelluva. Admin ei myöskään hyväksy reseptejä julkaisuun vaan ne julkaistaan heti kun käyttäjä lisää ne tietokantaan.

## Tietokantataulut 

Sovelluksessa on seuraavat tietokantataulut:
- users
- favorites
- upvotes
- recipes
- comments
- recipe of the week

Alkuperäinen suunnitelma:
![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/tables.jpeg)

Lopullinen kuvaus:
![](https://github.com/KatjaKvintus/Overnight-oats-recipe-bank/blob/master/documents/database_model.jpeg)

## Sovelluksen tiedossa olevat puutteet ja ongelmat
- Reseptipankiksi tässä on yksi perustavaa laatua oleva iso ongelma: käyttäjä ei pääse syöttämään omaa reseptiään kokonaan, vaan hän joutuu valitsemaan ainesosat (varsin suppeasta) listasta. Pidin kuitenkin tästä kiinni, koska kurssin tarkoituksena oli harjoitella nimenomaan tietokantasovellusta, ja rajoittamalla vapaateksisyötteitä sitä oli helpompi hallinnoida. Myös reseptin ohje on geneerinen eikä anna tilaa käyttäjän omille ideoille, esim. "liekitä kaurahiutaleet ennen kulhoon lisäämistä".
- Jos pääkäyttäjä ei ole julkaissut yhtään viikon reseptiä, pääsivun nappi 'Recipe of the week' ei anna virheilmoitusta vaan näyttää reseptin tyhjän rungon
- Uutta reseptiä lisätessä sovellus tarkistaa, onko saman nimistä reseptiä jo tietokannassa. Toiminto on toteutettu kömpelösti niin, että html-sivun script ei tunnista virhettä vaan se tulee vasta juuri ennen kantaan viemistä erillisenä virheilmoitussivuna. Lisäksi sovellus hakee kannan kaikki reseptit aina, kun käyttäjä lähtee luomaan uutta reseptiä, mikä on resursseja tuhlaava vaihtoehto, mutta päädyin siihen kun en keksinyt parempaakaan.
- Sovelluksessa ei ole yksittäistä päävalikkoa, joka näkyisi joka sivulla, vaan se on lisätty erikseen jokaisella html-pohjalle pienin variaatioin
- Koodissa käytetään useassa kohdassa muuttujanimiä, joilla on myös Python-merkitys, esim. id, type (mutta en uskaltanut lähteä fiksaamaan niitä, koska pelkäsin että deadlinen koittaessa sovellus ei toimi ollenkaan.)
- Pylintin huomauttamia cyclic importteja ei ole poistettu (sama syy kuin ed. kohdassa)

## Jatkokehitysideat
- Sovelluksen ulkoasu pitäisi rakentaa visuaaliseksi ja esteettömäksi
- Päävalikko kelluvaksi joka sivulle
- Tehokkaammat tietokantahaut (nyt ne on tehty ajatellen pientä tietokantaa, jossa hakujen nopeutta ei ole juuri optimoitu)
- Uuden reseptin syöttämiseen enemmän valinnanvapautta (valikoiden sijaan vapaatekstikenttiä)
