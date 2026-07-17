# Glossar

**Projekt:** NH3-PowerPlant

**Dokument:** 99_Glossar.md

**Version:** automatisch erzeugt

---

# Einleitung

Dieses Glossar enthält die im Projekt verwendeten Fachbegriffe.

Die Inhalte werden automatisch aus der Glossardatenbank erzeugt.

Manuelle Änderungen an diesem Dokument gehen bei der nächsten Generierung verloren.

---

{% for entry in glossary %}

## {{ entry.term }}

**Abkürzung**

{{ entry.abbreviation }}

**Definition**

{{ entry.definition }}

**Einheit**

{{ entry.unit }}

**Verwendet in**

{% for chapter in entry.references %}
- {{ chapter }}
{% endfor %}

---

{% endfor %}
