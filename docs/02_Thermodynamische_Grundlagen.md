# Thermodynamische Grundlagen

## Dokumentstatus

| Eigenschaft | Wert |
|-------------|------|
| Dokument | 02_Thermodynamische_Grundlagen.md |
| Version | 0.1 (Entwurf) |
| Bearbeitungsstand | Entwurf |
| Letzte Änderung | 15.07.2026 |
| Autor | Projekt NH3-PowerPlant |

---

# 1 Einleitung

Die Untersuchung der im Projekt *NH3-PowerPlant* vorgeschlagenen Anlagenarchitektur erfordert eine Betrachtung grundlegender thermodynamischer Zusammenhänge.

Dabei steht nicht die vollständige Darstellung der Thermodynamik im Vordergrund, sondern die Einführung jener Begriffe und Zusammenhänge, die für das Verständnis der späteren Berechnungen notwendig sind.

Insbesondere werden folgende Fragen behandelt:

- Warum kann Wärme nicht vollständig in Arbeit umgewandelt werden?
- Welche Aussage treffen der erste und der zweite Hauptsatz der Thermodynamik?
- Warum genügt eine reine Energiebilanz nicht zur Bewertung einer Anlage?
- Welche Rolle spielt die Exergie?
- Warum sind Temperaturunterschiede entscheidend für den Wirkungsgrad?

Diese Grundlagen bilden den theoretischen Rahmen für alle folgenden Kapitel.

---

# 2 Energie

Energie ist eine Erhaltungsgröße.

Sie kann weder erzeugt noch vernichtet werden, sondern lediglich zwischen verschiedenen Energieformen umgewandelt werden.

Typische Energieformen innerhalb der betrachteten Anlage sind

- elektrische Energie,
- mechanische Energie,
- thermische Energie,
- Druckenergie,
- innere Energie des Arbeitsmediums.

Für stationäre Kreisprozesse gilt grundsätzlich

\[
\sum E_{zu} = \sum E_{ab}
\]

Diese Aussage beschreibt jedoch ausschließlich die Energiemenge.

Sie enthält keinerlei Information darüber, wie hochwertig oder nutzbar diese Energie ist.

---

# 3 Erster Hauptsatz der Thermodynamik

Der erste Hauptsatz beschreibt die Energieerhaltung.

Für ein stationäres System gilt vereinfacht

\[
Q + W = \Delta H
\]

mit

- \(Q\) Wärmestrom
- \(W\) technische Arbeit
- \(H\) Enthalpie

Im Kreisprozess verschwindet keine Energie.

Alle Energieflüsse müssen vollständig bilanziert werden.

Für das vorliegende Projekt bedeutet dies:

- elektrische Energie der Wärmepumpe,
- aufgenommene Umweltwärme,
- abgegebene Wärme,
- Turbinenarbeit,
- Generatorleistung

müssen sich gegenseitig ausgleichen.

Der erste Hauptsatz beantwortet jedoch nicht die Frage, ob eine bestimmte Energieform zur Verrichtung mechanischer Arbeit geeignet ist.

---

# 4 Zweiter Hauptsatz der Thermodynamik

Der zweite Hauptsatz beschreibt die Richtung thermodynamischer Prozesse.

Er besagt unter anderem:

- Wärme fließt spontan nur von warm nach kalt.
- Jede reale Energieumwandlung erzeugt Entropie.
- Kein Kreisprozess kann die gesamte zugeführte Wärme vollständig in Arbeit umwandeln.

Damit erklärt der zweite Hauptsatz die Existenz unvermeidbarer Verluste.

Diese Verluste entstehen beispielsweise

- in Wärmeübertragern,
- in Turbinen,
- in Verdichtern,
- durch Reibung,
- durch endliche Temperaturdifferenzen.

Der zweite Hauptsatz begrenzt somit den maximal erreichbaren Wirkungsgrad jeder Wärmekraftmaschine.

---

# 5 Temperatur als Qualitätsmerkmal der Wärme

Wärme besitzt keine einheitliche Wertigkeit.

Beispielsweise besitzen

- 100 kJ bei 400 °C,
- 100 kJ bei 80 °C,
- 100 kJ bei 10 °C

denselben Energieinhalt.

Ihre Fähigkeit, mechanische Arbeit zu leisten, unterscheidet sich jedoch erheblich.

Je höher die Temperatur einer Wärmequelle ist,

desto größer ist ihr theoretisches Arbeitsvermögen.

Aus diesem Grund besitzen Hochtemperaturkraftwerke grundsätzlich höhere Wirkungsgrade als Niedertemperaturanlagen.

---

# 6 Carnot-Wirkungsgrad

Die theoretische Obergrenze jeder Wärmekraftmaschine wird durch den Carnot-Wirkungsgrad beschrieben.

\[
\eta_C = 1-\frac{T_k}{T_h}
\]

mit

- \(T_h\) Temperatur der Wärmequelle
- \(T_k\) Temperatur der Wärmesenke

Alle Temperaturen sind in Kelvin einzusetzen.

Der Carnot-Wirkungsgrad stellt keine reale Anlageneffizienz dar.

Er beschreibt ausschließlich die theoretisch maximal erreichbare Grenze.

Beispiel:

| Wärmequelle | Senke | Carnot |
|-------------|-------|--------:|
| 600 °C | 20 °C | ca. 66 % |
| 300 °C | 20 °C | ca. 46 % |
| 80 °C | 20 °C | ca. 17 % |

Bereits dieses Beispiel verdeutlicht die Herausforderung von Niedertemperatur-Kraftwerken.

---

# 7 Wärmepumpe

Eine Wärmepumpe arbeitet thermodynamisch in umgekehrter Richtung.

Sie transportiert Wärme von einer niedrigen Temperatur auf ein höheres Temperaturniveau.

Die Güte einer Wärmepumpe wird durch den COP (Coefficient of Performance) beschrieben.

\[
COP=\frac{Q_H}{W}
\]

mit

- \(Q_H\) abgegebene Heizleistung
- \(W\) elektrische Verdichterleistung

Typische industrielle NH₃-Wärmepumpen erreichen bei moderaten Temperaturhüben

COP-Werte zwischen 3 und 5.

Mit zunehmendem Temperaturhub sinkt der COP.

---

# 8 Kreisprozesse

Kreisprozesse dienen der Umwandlung thermischer Energie in mechanische Arbeit.

Typische Vertreter sind

- Clausius-Rankine-Prozess
- Organic Rankine Cycle (ORC)
- Kalina-Prozess
- superkritischer CO₂-Kreisprozess

Im Projekt wird zunächst ein NH₃-Kreisprozess betrachtet.

Der prinzipielle Ablauf besteht aus

1. Verdampfung
2. Expansion in der Turbine
3. Kondensation
4. Förderung durch eine Pumpe

Danach beginnt der Kreisprozess erneut.

---

# 9 Wirkungsgrad

Der Wirkungsgrad beschreibt das Verhältnis zwischen nutzbarer und eingesetzter Energie.

\[
\eta=\frac{P_{ab}}{P_{zu}}
\]

Der Gesamtwirkungsgrad ergibt sich aus den Wirkungsgraden aller Einzelkomponenten.

Bereits geringe Verluste einzelner Komponenten können den Gesamtwirkungsgrad deutlich reduzieren.

Deshalb genügt es nicht, ausschließlich die Turbine zu optimieren.

Auch

- Wärmeübertrager,
- Pumpen,
- Rohrleitungen,
- Generator,
- Verdichter

beeinflussen das Gesamtergebnis.

---

# 10 Exergie

Während Energie immer erhalten bleibt, gilt dies für Exergie nicht.

Exergie beschreibt den maximal nutzbaren Anteil einer Energieform.

Sie kann durch irreversible Prozesse vernichtet werden.

Für Wärme gilt

\[
Ex = Q\left(1-\frac{T_0}{T}\right)
\]

mit

- \(T\) Temperatur der Wärme
- \(T_0\) Umgebungstemperatur

Hieraus folgt unmittelbar:

Wärme bei Umgebungstemperatur besitzt nahezu keine Exergie.

Sie enthält zwar Energie,

kann jedoch praktisch keine mechanische Arbeit mehr leisten.

Die Exergieanalyse wird deshalb im weiteren Verlauf des Projekts das wichtigste Werkzeug zur Bewertung verschiedener Anlagenvarianten sein.

---

# 11 Irreversibilität

Jeder reale Prozess erzeugt Entropie.

Dadurch geht Exergie verloren.

Typische Ursachen sind

- Reibung,
- Drosselung,
- endliche Temperaturdifferenzen,
- Turbulenzen,
- Wärmeübertragung.

Die Reduzierung dieser Irreversibilitäten bildet den eigentlichen Ansatz moderner Kraftwerksentwicklung.

Nicht die Energie geht verloren,

sondern ihre Fähigkeit,

Arbeit zu verrichten.

---

# 12 Bedeutung für dieses Projekt

Die Kombination aus Wärmepumpe und NH₃-Kreisprozess besitzt zwei Besonderheiten.

Zum einen wird Umweltwärme auf ein höheres Temperaturniveau angehoben.

Zum anderen soll die Kondensationswärme möglichst vollständig innerhalb des Gesamtsystems genutzt werden.

Die eigentliche Fragestellung lautet deshalb nicht, ob Energie erhalten bleibt – dies folgt bereits aus dem ersten Hauptsatz.

Entscheidend ist vielmehr,

- welche Exergieverluste innerhalb der Anlage auftreten,
- welche Komponenten diese Verluste verursachen,
- und wie sich die thermische Kopplung so gestalten lässt, dass möglichst wenig Exergie vernichtet wird.

Die spätere Optimierung des Systems konzentriert sich daher auf die Reduzierung irreversibler Prozesse und nicht ausschließlich auf die Verbesserung einzelner Wirkungsgrade.

---

# 13 Zusammenfassung

Für die Bewertung der vorgeschlagenen Anlagenarchitektur reichen klassische Energiebilanzen nicht aus.

Erst die gemeinsame Betrachtung von

- Energie,
- Exergie,
- Entropie,
- Temperatur
- und Wirkungsgrad

ermöglicht eine fundierte Bewertung des Gesamtsystems.

Aus diesem Grund werden alle späteren Berechnungen sowohl als Energiebilanz als auch als Exergiebilanz durchgeführt.

Die Exergieanalyse bildet dabei den zentralen Bewertungsmaßstab der gesamten Untersuchung.
