#!/usr/bin/env python3
"""
Lead-Validierung und Aufbereitung für Instantly-Import.

Funktionen:
- E-Mail-Format prüfen
- Pflichtfelder prüfen
- Duplikate entfernen
- Typ-Zuordnung validieren (privat/wohlfahrt/sozialstation)
- Aufteilen nach Kampagne (A/B/C)
- Statistik ausgeben
"""

import csv
import re
import sys
import os
from collections import Counter

# Pflichtfelder
REQUIRED_FIELDS = ['email', 'first_name', 'company_name', 'city', 'type']
VALID_TYPES = ['privat', 'wohlfahrt', 'sozialstation']
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Bekannte Catch-All / Generische Adressen die oft bouncen
GENERIC_PREFIXES = ['info@', 'kontakt@', 'office@', 'mail@', 'post@']


def validate_email(email):
    """Prüft ob E-Mail-Format gültig ist."""
    if not email:
        return False, "Leer"
    if not EMAIL_REGEX.match(email):
        return False, "Ungültiges Format"
    return True, "OK"


def validate_row(row, row_num):
    """Validiert eine einzelne Lead-Zeile."""
    errors = []

    # Pflichtfelder prüfen
    for field in REQUIRED_FIELDS:
        if field not in row or not row[field].strip():
            errors.append(f"Zeile {row_num}: Feld '{field}' fehlt oder leer")

    # E-Mail prüfen
    if 'email' in row:
        valid, msg = validate_email(row['email'].strip())
        if not valid:
            errors.append(f"Zeile {row_num}: E-Mail ungültig ({msg}): {row.get('email', '')}")

    # Typ prüfen
    if 'type' in row and row['type'].strip().lower() not in VALID_TYPES:
        errors.append(f"Zeile {row_num}: Ungültiger Typ '{row['type']}' (erlaubt: {', '.join(VALID_TYPES)})")

    return errors


def check_generic_email(email):
    """Warnt bei generischen E-Mail-Adressen."""
    email_lower = email.lower()
    for prefix in GENERIC_PREFIXES:
        if email_lower.startswith(prefix):
            return True
    return False


def process_leads(input_file):
    """Hauptfunktion: Leads validieren, deduplizieren und aufteilen."""

    if not os.path.exists(input_file):
        print(f"FEHLER: Datei '{input_file}' nicht gefunden!")
        sys.exit(1)

    leads = []
    errors = []
    warnings = []
    seen_emails = set()
    duplicates = 0

    # CSV lesen
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        # Header prüfen
        if reader.fieldnames:
            missing_headers = [h for h in REQUIRED_FIELDS if h not in reader.fieldnames]
            if missing_headers:
                print(f"FEHLER: Fehlende Spalten: {', '.join(missing_headers)}")
                print(f"Vorhandene Spalten: {', '.join(reader.fieldnames)}")
                sys.exit(1)

        for i, row in enumerate(reader, start=2):
            # Validieren
            row_errors = validate_row(row, i)
            if row_errors:
                errors.extend(row_errors)
                continue

            # Normalisieren
            email = row['email'].strip().lower()
            row['email'] = email
            row['type'] = row['type'].strip().lower()
            row['first_name'] = row.get('first_name', '').strip()
            row['last_name'] = row.get('last_name', '').strip()
            row['company_name'] = row.get('company_name', '').strip()
            row['city'] = row.get('city', '').strip()

            # Duplikat-Check
            if email in seen_emails:
                duplicates += 1
                continue
            seen_emails.add(email)

            # Generische E-Mail warnen
            if check_generic_email(email):
                warnings.append(f"Generische E-Mail: {email} ({row['company_name']})")

            leads.append(row)

    # Aufteilen nach Kampagne
    kampagne_a = [l for l in leads if l['type'] == 'privat']
    kampagne_b = [l for l in leads if l['type'] == 'wohlfahrt']
    kampagne_c = [l for l in leads if l['type'] == 'sozialstation']

    # Output-Verzeichnis
    output_dir = os.path.dirname(input_file) or '.'

    # Kampagnen-CSVs schreiben
    fieldnames = ['email', 'first_name', 'last_name', 'company_name', 'city', 'website', 'type', 'phone']

    for name, data in [('kampagne-a-private', kampagne_a),
                       ('kampagne-b-wohlfahrt', kampagne_b),
                       ('kampagne-c-sozialstationen', kampagne_c)]:
        output_file = os.path.join(output_dir, f'{name}.csv')
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)

    # Report
    print("=" * 60)
    print("EAR OUTREACH – Lead-Validierung Report")
    print("=" * 60)
    print(f"\nInput-Datei: {input_file}")
    print(f"\nGesamt gelesen:    {len(leads) + len(errors) + duplicates}")
    print(f"Valide Leads:      {len(leads)}")
    print(f"Fehlerhafte:       {len(errors)}")
    print(f"Duplikate:         {duplicates}")
    print(f"\n--- Aufteilung nach Kampagne ---")
    print(f"Kampagne A (Privat):          {len(kampagne_a)}")
    print(f"Kampagne B (Wohlfahrt):       {len(kampagne_b)}")
    print(f"Kampagne C (Sozialstationen): {len(kampagne_c)}")

    # Städte-Verteilung
    cities = Counter(l['city'] for l in leads)
    print(f"\n--- Top 10 Städte ---")
    for city, count in cities.most_common(10):
        print(f"  {city}: {count}")

    if warnings:
        print(f"\n--- Warnungen ({len(warnings)}) ---")
        for w in warnings[:20]:
            print(f"  ⚠ {w}")
        if len(warnings) > 20:
            print(f"  ... und {len(warnings) - 20} weitere")

    if errors:
        print(f"\n--- Fehler ({len(errors)}) ---")
        for e in errors[:20]:
            print(f"  ✗ {e}")
        if len(errors) > 20:
            print(f"  ... und {len(errors) - 20} weitere")

    print(f"\n--- Output-Dateien ---")
    print(f"  {output_dir}/kampagne-a-private.csv ({len(kampagne_a)} Leads)")
    print(f"  {output_dir}/kampagne-b-wohlfahrt.csv ({len(kampagne_b)} Leads)")
    print(f"  {output_dir}/kampagne-c-sozialstationen.csv ({len(kampagne_c)} Leads)")
    print("=" * 60)

    return len(errors) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Verwendung: python validate-leads.py <leads.csv>")
        print("Beispiel:   python validate-leads.py ../leads/alle-leads.csv")
        sys.exit(1)

    success = process_leads(sys.argv[1])
    sys.exit(0 if success else 1)
