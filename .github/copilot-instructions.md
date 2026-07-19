# Copilot-Instructions für NH3-PowerPlant

## Git Remotes

Abweichend von der generellen Nutzerpräferenz gilt für dieses Projekt:

- Es gibt zwei Remotes: `origin` (lokaler Mirror) und `github` (öffentliches GitHub-Repo).
- Bei jedem Push soll **immer zu beiden Remotes** gepusht werden (`origin` und `github`), nicht nur zu `origin`.

## Git Branches

- Das Repository auf GitHub ist öffentlich.
- Die regulären Branches sind `dev` und `main`.
- Die aktive Entwicklung erfolgt auf `dev`.
- `main` ist durch Branch Protection geschützt.
- Niemand pusht direkt nach `main`; Änderungen gelangen ausschließlich per Pull Request von `dev` nach `main`.
