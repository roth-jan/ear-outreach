# ÜBERGABE TAB 4 – EAR Outreach Kampagne

---

## AUFTRAG

Aufbau einer kompletten Cold-E-Mail Outreach-Kampagne für **EAR (Essen auf Rädern)** – eine Software-Komplettlösung für Mahlzeitendienste/Essen-auf-Rädern-Anbieter.

**Produkt:** EAR Software
**Landingpage:** https://www.essen-auf-raedern.eu/
**Kernfunktionen:**
- Tourenplanung mit Google Maps Integration
- Automatische Packlisten & Etikettendruck
- Kundenverwaltung mit Sonderwünschen, Allergien, Lieferhinweisen
- Rezeptverwaltung & Einkaufslisten
- Bestellmanagement

**Kampagnen-Tool:** Instantly (Account vorhanden, wird auch für eine andere Kampagne genutzt – WebMenü)
**Domain-Anbieter:** Strato

---

## STATUS

### Erledigt:
- GitHub Repository erstellt und gepusht
- 3 komplette E-Mail-Sequenzen geschrieben (je 4 Mails × A/B-Varianten)
- DNS & E-Mail Setup-Anleitung erstellt
- Instantly Kampagnen-Konfiguration dokumentiert
- Lead-CSV-Vorlage + Python-Validierungsscript erstellt und getestet
- KPI-Tracking Dashboard (HTML/JS) gebaut

### Offen:
- Domains bei Strato kaufen und einrichten (DNS, E-Mail-Accounts)
- E-Mail-Accounts in Instantly verbinden
- Warm-up starten
- Leads sammeln und importieren
- Kampagnen in Instantly anlegen und starten
- Landingpage prüfen/optimieren für die Kampagne

### Aktueller Stand:
Alle Vorbereitungs-Materialien sind fertig. Der nächste Schritt ist Domain-Kauf + DNS-Setup + Warm-up. Leads werden parallel vom User gesammelt.

---

## ERGEBNISSE

### GitHub Repository
- **URL:** https://github.com/roth-jan/ear-outreach
- **Lokaler Pfad:** `~/aws-projekte/ear-outreach/`
- **Branch:** `main`
- **2 Commits** bisher, alles gepusht

### E-Mail-Sequenzen (3 Kampagnen × 4 Mails × A/B = 24 E-Mail-Varianten)

**Kampagne A – Private Mahlzeitendienste:**
- Mail 1 (Tag 0): A="Tourenplanung noch mit Excel?" / B="Jede Mahlzeit pünktlich – ohne Tourenplanung-Stress"
- Mail 2 (Tag 3): A="Re: Tourenplanung noch mit Excel?" / B="Kurze Frage zu den Touren bei {{firmenname}}"
- Mail 3 (Tag 7): A="Was Google Maps für Ihre Touren tun kann" / B="Ihre Fahrer fahren wahrscheinlich 20% zu viel"
- Mail 4 (Tag 12): A="Soll ich aufhören zu schreiben?" / B="Letzte Mail von mir"

**Kampagne B – Wohlfahrtsverbände (DRK, Malteser, Johanniter, Caritas, Diakonie):**
- Mail 1 (Tag 0): A="Tourenplanung noch mit Excel und Papierlisten?" / B="Mehr Zeit für das Wesentliche – weniger für Tourenplanung"
- Mail 2 (Tag 3): A="Re: Tourenplanung noch mit Excel und Papierlisten?" / B="Kurze Frage zum Mahlzeitendienst beim {{firmenname}}"
- Mail 3 (Tag 7): A="Allergien, Diäten, Lieferhinweise – alles auf einen Blick" / B="Was passiert, wenn der Fahrer den Sonderwunsch nicht kennt?"
- Mail 4 (Tag 12): A="Soll ich aufhören zu schreiben?" / B="Letzte Mail von mir"

**Kampagne C – Sozialstationen:**
- Mail 1 (Tag 0): A="Mahlzeitendienst nebenbei managen – muss das so bleiben?" / B="Mahlzeitendienst digitalisieren – in 2 Wochen"
- Mail 2 (Tag 3): A="Re: Mahlzeitendienst nebenbei managen..." / B="Was passiert, wenn Ihre Tourenplanerin mal krank ist?"
- Mail 3 (Tag 7): A="Packlisten und Etiketten – auf Knopfdruck statt per Hand" / B="Wie viele Etiketten schreiben Sie noch per Hand?"
- Mail 4 (Tag 12): A="Soll ich aufhören zu schreiben?" / B="Letzte Mail von mir"

**Personalisierungs-Variablen:** `{{vorname}}`, `{{firmenname}}`, `{{stadt}}`, `{{absender_vorname}}`, `{{absender_nachname}}`, `{{calendly_link}}`

### Domains (zu registrieren bei Strato)

| Domain | Zweck |
|--------|-------|
| `ear-software.de` | Haupt-Absenderdomain |
| `mahlzeitendienst-software.de` | Variante für A/B |
| `lieferservice-software.info` | Variante |
| `touren-planer.info` | Variante |
| `essen-lieferung.info` | Variante |

**WICHTIG:** User hat gesagt er hat EINE Domain bereits – aber NICHT gesagt welche. Das muss noch geklärt werden.

**WICHTIG:** Ein anderer Claude-Chat kümmert sich parallel um Domain-Käufe bei Strato. NICHT bei Strato eingreifen, um Konflikte zu vermeiden.

### E-Mail-Accounts pro Domain (2-3 Stück)
```
c.loch@[domain]
info@[domain]
kontakt@[domain]
```

### DNS-Records (für jede Domain bei Strato einzutragen)

**SPF:**
```
Typ: TXT | Host: @ | Wert: v=spf1 include:_spf.strato.de include:_spf.instantly.ai ~all
```

**DKIM:**
```
Typ: TXT | Host: instantly._domainkey | Wert: [von Instantly generiert]
```

**DMARC:**
```
Typ: TXT | Host: _dmarc | Wert: v=DMARC1; p=none; rua=mailto:dmarc@ear-software.de
```

**Custom Tracking Domain:**
```
Typ: CNAME | Host: track | Wert: [von Instantly bereitgestellt]
```

### Instantly-Einstellungen

**SMTP für Strato-Accounts:**
```
SMTP Host:    smtp.strato.de
SMTP Port:    465 (SSL)
IMAP Host:    imap.strato.de
IMAP Port:    993 (SSL)
```

**Sendeplan:**
- Tage: Dienstag, Mittwoch, Donnerstag
- Zeiten: 08:00-11:00, 14:00-16:00
- Timezone: Europe/Berlin
- Mails pro Tag pro Account: 30-50
- Time gap: 3-5 Minuten

**Warm-up Einstellungen:**
- Daily warm-up limit: 40
- Ramp-up: 2 per day
- Reply rate: 30-40%
- Minimum 2 Wochen vor Kampagnenstart
- Warm-up parallel zu Kampagnen laufen lassen

### Lead-Validierungsscript

Python-Script unter `scripts/validate-leads.py`:
- Prüft E-Mail-Format, Pflichtfelder, Typen
- Entfernt Duplikate
- Teilt Leads automatisch in 3 Kampagnen-CSVs auf
- Gibt Statistik-Report aus

Verwendung:
```bash
python3 ~/aws-projekte/ear-outreach/scripts/validate-leads.py leads/alle-leads.csv
```

Output: 3 CSVs (`kampagne-a-private.csv`, `kampagne-b-wohlfahrt.csv`, `kampagne-c-sozialstationen.csv`)

### CSV-Format für Leads
```csv
email,first_name,last_name,company_name,city,website,type,phone
```
- `type` muss sein: `privat`, `wohlfahrt` oder `sozialstation`

### KPI-Dashboard
- HTML-Datei unter `dashboard/index.html`
- Speichert Daten in localStorage
- Zeigt: Open Rate, Reply Rate, Positive Replies, Demo-Termine
- Pro Kampagne und gesamt
- A/B-Test Tracking
- Wochen-Tracking
- CSV-Export

### KPI-Ziele
| Metrik | Ziel |
|--------|------|
| Open Rate | >50% |
| Reply Rate | >5% |
| Positive Reply Rate | >2% |
| Demo-Termine | 1-2% der Leads |

### Zielgruppen

| Segment | Priorität | Idealer Kunde |
|---------|-----------|---------------|
| Private Mahlzeitendienste | HOCH | 50+ Mahlzeiten/Tag, Excel/Papier, mehrere Fahrer |
| Wohlfahrtsverbände (DRK, Malteser, Johanniter, Caritas, Diakonie) | HOCH | Lokale Orts-/Kreisverbände, NICHT Bundesebene |
| Sozialstationen | MITTEL | Pflege + Mahlzeitendienst kombiniert |

### Lead-Quellen
| Quelle | Methode | Erwartete Leads |
|--------|---------|-----------------|
| Google Maps | "Essen auf Rädern" + Stadt (>20.000 Einwohner) | 3.000-5.000 |
| Wohlfahrtsverband-Websites | DRK, Malteser, Johanniter Kreisverbände | 2.000-3.000 |
| Pflegenavigator/Pflegelotse | Verzeichnisse für Pflegedienste | 1.000-2.000 |
| Gelbe Seiten | Kategorie: Mahlzeitendienst, Menüservice | 1.000-2.000 |
| Branchenverzeichnisse | bpa, vdek | 500-1.000 |

---

## OFFENE AUFGABEN

1. **Klären welche Domain der User bereits hat** – Er sagte "eine Domain haben wir" aber nicht welche der 5 geplanten. Fragen!

2. **Domains bei Strato kaufen** – ACHTUNG: Ein anderer Chat macht das parallel. Abklären ob das schon erledigt ist oder der User das selbst macht. NICHT selbst bei Strato im Browser agieren.

3. **E-Mail-Accounts bei Strato anlegen** – Pro gekaufter Domain 2-3 Accounts (c.loch@, info@, kontakt@). Entweder über Strato-Admin-Panel oder der User macht das.

4. **DNS-Records bei Strato eintragen** – SPF, DKIM, DMARC, Custom Tracking Domain. Details in `docs/dns-setup.md`.

5. **Domains & Accounts in Instantly verbinden** – SMTP/IMAP-Einstellungen (Strato). Details in `docs/instantly-setup.md`.

6. **Warm-up starten** – Mindestens 2 Wochen vor Kampagnenstart. Einstellungen: 40/Tag, Ramp-up 2/Tag, Reply Rate 30-40%.

7. **Leads sammeln** – User sammelt Adressen parallel. Wenn CSVs da sind: durch `validate-leads.py` jagen → 3 Kampagnen-CSVs generieren → in Instantly importieren.

8. **Kampagnen in Instantly anlegen** – 3 Kampagnen mit den E-Mail-Sequenzen aus den Markdown-Dateien. A/B-Tests konfigurieren (50/50 Split).

9. **Calendly-Link erstellen** – Wird in der Breakup-Mail (Mail 4) verwendet. Variable `{{calendly_link}}`. Muss noch eingerichtet werden.

10. **Absender-Infos festlegen** – `{{absender_vorname}}` und `{{absender_nachname}}` – vermutlich "Christian Loch" aber bestätigen.

11. **Landingpage prüfen** – https://www.essen-auf-raedern.eu/ – Sicherstellen dass sie für Leads optimiert ist die über Cold-E-Mail kommen.

12. **Kampagnen starten** – Nach Warm-up (2-3 Wochen) mit 500-1000 Leads starten, dann optimieren und skalieren.

---

## KONTEXT

### Zugänge & Accounts
- **GitHub:** Token liegt in `/Users/jhrothntconsult.de/.claude/github-token`. User: `roth-jan`. Authentifizierung via: `GITHUB_TOKEN=$(cat /Users/jhrothntconsult.de/.claude/github-token) gh [command]`
- **Instantly:** Account vorhanden (wird auch für WebMenü-Kampagne genutzt). Login-Daten nicht bekannt – User muss im Browser einloggen oder Zugangsdaten geben.
- **Strato:** Account vorhanden. Login-Daten nicht bekannt. NICHT selbst bei Strato im Browser agieren – anderer Chat oder User macht das.

### Wichtige Entscheidungen
- **Tonalität:** Professionell, direkt, nicht aufdringlich – "auf Augenhöhe". Keine Emojis in den Mails.
- **Plain Text:** Keine HTML-Mails, keine Bilder. Nur Plain Text für bessere Deliverability.
- **Kein Hard-Selling:** Immer einen einfachen Ausweg lassen. Ziel ist 15-Minuten-Gespräch/Demo.
- **Wohlfahrtsverbände dezentral:** Immer lokale Orts-/Kreisverbände ansprechen, NIE Bundesebene.
- **Format angelehnt an WebMenü-Outreach:** Es gibt eine bestehende Outreach-Kampagne unter `~/aws-projekte/webmenue-outreach/` die als Vorlage diente.

### Parallele Aktivitäten
- **Anderer Claude-Chat** kümmert sich um Domain-Käufe bei Strato → NICHT einmischen
- **User sammelt Leads parallel** → Werden als CSV geliefert

### Browser-Nutzung
- Playwright MCP ist verfügbar für Browser-Automatisierung
- Chrome hatte Probleme (Konflikte mit laufender System-Chrome-Instanz). Lösung: `browser_install` ausführen um Playwright-eigenes Chrome zu installieren, dann funktioniert es.
- User will dass der Chat Browser-Aktionen übernimmt – "ich klicke nur auf kaufen"
- **Ausnahme: NICHT bei Strato** (anderer Chat / User macht das)

---

## DATEIEN

Alle Dateien im Repo `~/aws-projekte/ear-outreach/`:

```
~/aws-projekte/ear-outreach/
├── README.md                                    # Projekt-Übersicht, Zielgruppen, KPIs, Zeitplan
├── ÜBERGABE.md                                  # Diese Datei
├── emails/
│   ├── kampagne-a-private/
│   │   └── sequenz.md                           # 4 Mails × A/B für private Mahlzeitendienste
│   ├── kampagne-b-wohlfahrt/
│   │   └── sequenz.md                           # 4 Mails × A/B für Wohlfahrtsverbände
│   └── kampagne-c-sozialstationen/
│       └── sequenz.md                           # 4 Mails × A/B für Sozialstationen
├── leads/
│   ├── beispiel-leads.csv                       # 3 Beispiel-Leads zum Testen
│   ├── instantly-import-vorlage.csv             # Leere CSV-Vorlage für Lead-Import
│   ├── kampagne-a-private.csv                   # Generiert vom Script (Test-Output)
│   ├── kampagne-b-wohlfahrt.csv                 # Generiert vom Script (Test-Output)
│   └── kampagne-c-sozialstationen.csv           # Generiert vom Script (Test-Output)
├── scripts/
│   └── validate-leads.py                        # Lead-Validierung, Deduplizierung, Aufteilung
├── docs/
│   ├── dns-setup.md                             # SPF, DKIM, DMARC, Warmup-Anleitung
│   └── instantly-setup.md                       # Instantly SMTP, Sequenzen, A/B-Test Config
├── dashboard/
│   └── index.html                               # KPI-Tracking Dashboard (HTML/JS/localStorage)
└── templates/                                   # (leer, für Instantly-Import Templates)
```

### Referenz-Dateien (nicht in diesem Repo)
- `~/aws-projekte/webmenue-outreach/kampagne-a-caterer.md` – Vorlage/Referenz für E-Mail-Format
- `~/aws-projekte/webmenue-outreach/kampagne-b-kita-traeger.md` – Weitere Referenz
- `/Users/jhrothntconsult.de/.claude/github-token` – GitHub Auth Token
- `/Users/jhrothntconsult.de/.claude/CLAUDE.md` – Globale Claude-Anweisungen (Test-Standards, GitHub-Automation)

---

*Übergabe erstellt am 08.02.2026 von Claude Opus 4.6 – Tab 4*
