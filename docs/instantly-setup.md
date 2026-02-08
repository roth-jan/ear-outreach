# Instantly Kampagnen-Konfiguration

## 1. Account-Struktur

### E-Mail-Accounts hinzufügen
Unter **Email Accounts** → **Add New** → **SMTP Accounts**

Für jeden Strato-Account:
```
SMTP Host:    smtp.strato.de
SMTP Port:    465 (SSL)
IMAP Host:    imap.strato.de
IMAP Port:    993 (SSL)
Username:     [volle E-Mail-Adresse]
Password:     [Passwort]
```

### Sender-Informationen
| Account | Sender Name | Sender Email |
|---------|-------------|--------------|
| 1 | Christian Loch | c.loch@ear-software.de |
| 2 | EAR Software | info@ear-software.de |
| 3 | Christian Loch | c.loch@mahlzeitendienst-software.de |
| 4 | EAR Team | kontakt@mahlzeitendienst-software.de |
| ... | ... | ... |

**Tipp:** "Christian Loch" als Absendername – persönliche Namen haben bessere Open Rates als Firmennamen.

---

## 2. Kampagnen erstellen

### Struktur
```
📁 EAR Outreach
├── 📧 Kampagne A: Private Mahlzeitendienste
├── 📧 Kampagne B: Wohlfahrtsverbände
└── 📧 Kampagne C: Sozialstationen
```

### Kampagne anlegen
1. **Campaigns** → **Add New Campaign**
2. Name: `EAR - Kampagne A - Private Mahlzeitendienste`
3. **Email Accounts** zuweisen (2-3 pro Kampagne)

---

## 3. Sequenz-Einstellungen

### Schedule (für alle Kampagnen gleich)
```
Tage:       Dienstag, Mittwoch, Donnerstag
Zeiten:     08:00 - 11:00, 14:00 - 16:00
Timezone:   Europe/Berlin
```

### Sending Settings
```
Emails per day per account:      30-50
Time gap between emails:         3-5 Minuten
Reply as new thread:             AUS
Track opens:                     AN
Track link clicks:               AUS (erst ab Mail 4 mit Calendly)
```

### Sequence Steps

**Step 1 – Erster Kontakt (Tag 0)**
- Delay: 0 Tage
- Variante A + B als A/B-Test (50/50 Split)

**Step 2 – Follow-up (Tag 3)**
- Delay: 3 Tage nach Step 1
- Variante A + B als A/B-Test
- "Reply to previous email": JA

**Step 3 – Feature-Fokus (Tag 7)**
- Delay: 4 Tage nach Step 2
- Variante A + B als A/B-Test
- "Reply to previous email": NEIN (neuer Thread)

**Step 4 – Breakup (Tag 12)**
- Delay: 5 Tage nach Step 3
- Variante A + B als A/B-Test
- "Reply to previous email": NEIN

---

## 4. A/B-Test Konfiguration

### Pro E-Mail-Step:
1. **Add Variant** klicken
2. Variante A einfügen (Problem-fokussiert)
3. Variante B einfügen (Nutzen-fokussiert)
4. Split: **50/50**
5. Winning metric: **Reply Rate** (nicht Open Rate)

### Nach 200-300 Sends pro Variante:
- Gewinner-Variante identifizieren
- Verlierer deaktivieren oder durch neue Variante ersetzen

---

## 5. Lead-Import

### CSV-Format für Instantly
```csv
email,first_name,last_name,company_name,city,website,type
thomas.mueller@mahlzeit-gmbh.de,Thomas,Müller,Müller Mahlzeitendienst,München,mahlzeit-gmbh.de,privat
```

### Pflichtfelder
| Feld | Instantly-Variable | Verwendung |
|------|-------------------|------------|
| email | {{email}} | Empfänger |
| first_name | {{vorname}} | Anrede |
| company_name | {{firmenname}} | Personalisierung |
| city | {{stadt}} | Lokalisierung |

### Optionale Felder
| Feld | Instantly-Variable | Verwendung |
|------|-------------------|------------|
| last_name | {{nachname}} | - |
| website | {{website}} | Recherche-Referenz |
| type | {{typ}} | Kampagnen-Zuordnung |
| phone | {{telefon}} | Für Follow-up Calls |

### Custom Variables in Instantly
1. **Leads** → **Import** → CSV hochladen
2. Felder mappen:
   - `email` → Email
   - `first_name` → First Name
   - `company_name` → Company Name
   - `city` → Custom Variable `{{stadt}}`
3. **Duplikate:** Instantly prüft automatisch auf doppelte E-Mails

### Leads den Kampagnen zuordnen
- **Kampagne A:** Alle Leads mit `type = privat`
- **Kampagne B:** Alle Leads mit `type = wohlfahrt`
- **Kampagne C:** Alle Leads mit `type = sozialstation`

---

## 6. Blocklist & Bounce-Management

### Blocklist einrichten
Unter **Settings** → **Blocklist**:
- Eigene Domains blocken
- Kunden die "Nein" gesagt haben
- Bounced Emails automatisch entfernen lassen

### Bounce-Einstellungen
```
Auto-pause on bounce rate > 5%:     AN
Remove bounced leads:                AN
Auto-tag replies:                    AN
```

---

## 7. Reply-Management

### Auto-Tags einrichten
| Tag | Trigger | Aktion |
|-----|---------|--------|
| `interessiert` | Manuell | → Demo-Termin buchen |
| `nicht-interessiert` | Manuell | → Blocklist |
| `abwesend` | Auto (OOO detected) | → Später nochmal |
| `weiterleitung` | Manuell | → Neuen Kontakt anlegen |

### Workflow bei Antworten
1. **Positive Antwort:** Sofort persönlich antworten (nicht automatisch!), Demo-Link senden
2. **Negative Antwort:** Höflich bedanken, aus Kampagne entfernen
3. **Rückfrage:** Beantworten, in Kampagne lassen
4. **Out-of-Office:** Notieren, nach Rückkehr nochmal ansprechen

---

## 8. Monitoring & Optimierung

### Täglich prüfen (erste 2 Wochen)
- [ ] Bounce Rate < 5%?
- [ ] Keine Spam-Reports?
- [ ] Replies bearbeitet?

### Wöchentlich prüfen
- [ ] Open Rate > 50%?
- [ ] Reply Rate > 5%?
- [ ] Positive Reply Rate > 2%?
- [ ] A/B-Test Ergebnisse auswerten

### Warnsignale
| Signal | Aktion |
|--------|--------|
| Open Rate < 30% | Betreffzeilen ändern |
| Bounce Rate > 5% | Lead-Qualität prüfen, Kampagne pausieren |
| Spam-Reports | Sofort pausieren, Content prüfen |
| Keine Replies nach 500 Sends | Messaging komplett überarbeiten |
