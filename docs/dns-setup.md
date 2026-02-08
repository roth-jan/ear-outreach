# DNS & E-Mail Setup-Anleitung

## 1. Domains

### Zu registrieren (bei Strato)
| Domain | Zweck |
|--------|-------|
| `ear-software.de` | Haupt-Absenderdomain |
| `mahlzeitendienst-software.de` | Variante für A/B |
| `lieferservice-software.info` | Variante |
| `touren-planer.info` | Variante |
| `essen-lieferung.info` | Variante |

### E-Mail-Accounts pro Domain (2-3 Stück)
```
c.loch@[domain]
info@[domain]
kontakt@[domain]
```

---

## 2. DNS-Einstellungen (Strato)

### SPF-Record
Für jede Domain einen TXT-Record anlegen:
```
Typ:   TXT
Host:  @
Wert:  v=spf1 include:_spf.strato.de include:_spf.instantly.ai ~all
```

**Warum?** SPF sagt dem Empfänger-Server: "Diese Server dürfen im Namen dieser Domain E-Mails senden." Ohne SPF landen Mails im Spam.

### DKIM
- Bei Strato: **Automatisch aktiv** für Strato-E-Mail-Accounts
- Für Instantly: Im Instantly-Dashboard unter "Email Accounts" → Domain hinzufügen → DKIM-Schlüssel wird generiert
- Den generierten DKIM-TXT-Record bei Strato eintragen:
```
Typ:   TXT
Host:  instantly._domainkey
Wert:  [wird von Instantly bereitgestellt]
```

### DMARC
```
Typ:   TXT
Host:  _dmarc
Wert:  v=DMARC1; p=none; rua=mailto:dmarc@ear-software.de
```

**Empfehlung:** Erst `p=none` (Monitoring), nach 2-4 Wochen auf `p=quarantine` umstellen.

### Custom Tracking Domain (für Instantly)
```
Typ:   CNAME
Host:  track
Wert:  [wird von Instantly bereitgestellt, z.B. custom.instantly.ai]
```

---

## 3. E-Mail Warm-up

### Warum Warm-up?
Neue E-Mail-Accounts haben keine Reputation. Wenn du sofort 50 Mails/Tag schickst, landest du im Spam. Warm-up baut schrittweise Reputation auf.

### Warm-up Zeitplan

| Tag | Mails/Tag | Aktion |
|-----|-----------|--------|
| 1-3 | 2-5 | Nur an eigene Accounts, antworten |
| 4-7 | 5-10 | Instantly Warm-up aktivieren |
| 8-14 | 10-20 | Warm-up läuft automatisch |
| 15-21 | 20-30 | Langsam hochfahren |
| 22+ | 30-50 | Volle Kapazität |

### Instantly Warm-up aktivieren
1. Instantly → Email Accounts → Account auswählen
2. "Warm-up" Tab → **Enable**
3. Einstellungen:
   - Daily warm-up limit: **40**
   - Ramp-up: **2 per day**
   - Reply rate: **30-40%**
4. **Warm-up NICHT deaktivieren** wenn Kampagnen starten – parallel laufen lassen!

### Warm-up Dauer
- **Minimum: 2 Wochen** bevor erste Kampagne startet
- **Ideal: 3 Wochen** für bessere Reputation
- Pro Domain versetzt starten (nicht alle gleichzeitig)

---

## 4. Domain Health Check

### Vor Kampagnenstart prüfen:

#### Mail-tester.com
1. E-Mail an die angezeigte Adresse senden
2. Score prüfen: **Ziel: 9/10 oder höher**
3. Falls < 9: SPF/DKIM/DMARC korrigieren

#### MXToolbox.com
- SPF Check: `mxtoolbox.com/spf.aspx`
- DKIM Check: `mxtoolbox.com/dkim.aspx`
- DMARC Check: `mxtoolbox.com/dmarc.aspx`
- Blacklist Check: `mxtoolbox.com/blacklists.aspx`

#### Google Postmaster Tools
- Anmelden unter `postmaster.tools.google.com`
- Domain verifizieren
- Reputation und Spam-Rate überwachen

---

## 5. Best Practices

### Domain-Rotation
- Nicht alle Mails von einer Domain senden
- Domains gleichmäßig über Kampagnen verteilen
- Beispiel:
  - Kampagne A: `ear-software.de` + `touren-planer.info`
  - Kampagne B: `mahlzeitendienst-software.de` + `essen-lieferung.info`
  - Kampagne C: `lieferservice-software.info` + `ear-software.de`

### Sender-Accounts pro Domain
- 2-3 Accounts pro Domain
- Max. 30-50 Mails pro Account pro Tag
- = 60-150 Mails pro Domain pro Tag
- = 300-750 Mails gesamt pro Tag (5 Domains)

### Red Flags vermeiden
- Keine Links in den ersten 1-2 Mails (außer Calendly in Breakup)
- Kein HTML/Bilder – nur Plain Text
- Keine Spam-Wörter: "kostenlos", "Angebot", "nur heute"
- Personalisierung nutzen ({{vorname}}, {{firmenname}})
- Unsubscribe-Link NICHT in Cold-E-Mails (wirkt wie Newsletter/Spam)

---

## 6. Checkliste vor Kampagnenstart

- [ ] Alle Domains registriert
- [ ] E-Mail-Accounts angelegt (2-3 pro Domain)
- [ ] SPF-Record für jede Domain eingetragen
- [ ] DKIM für Instantly konfiguriert
- [ ] DMARC-Record angelegt
- [ ] Custom Tracking Domain eingerichtet
- [ ] Warm-up für alle Accounts aktiviert (min. 2 Wochen)
- [ ] Mail-tester.com Score ≥ 9/10
- [ ] Keine Blacklist-Einträge (MXToolbox)
- [ ] Test-Mails gesendet und im Posteingang angekommen (nicht Spam)
