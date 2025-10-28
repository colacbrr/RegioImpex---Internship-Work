# Django Practica 2024

# Sistem de Ticheting pentru Suportul Șoferilor de Cisternă

## Descrierea Generală a Proiectului
Scopul proiectului este de a dezvolta o aplicație web pentru gestionarea tichetelor și rapoartelor legate de suportul șoferilor de cisterne. Aplicația va permite operatorilor să creeze, editeze și să șteargă tichete în funcție de problemele raportate de șoferi. Un administrator va gestiona utilizatorii, cisternele și motivele de bypass.

Aplicația va fi realizată folosind:
- **Backend:** Django
- **Bază de date:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Funcționalități

### Funcționalități pentru Operator
- Crearea de tichete.
- Editarea tichetelor.
- Ștergerea tichetelor.
- Vizualizarea tichetelor existente.

### Funcționalități pentru Administrator
- Crearea, editarea și ștergerea utilizatorilor.
- Adăugarea, editarea și ștergerea cisternelor.
- Gestionarea motivelor de bypass (adăugare, editare, ștergere).

### Funcționalități Raportare
- Generarea de rapoarte bazate pe tichetele înregistrate.
- Filtrarea și sortarea rapoartelor pe baza diferitelor criterii (data, număr cisternă, nume șofer, etc).

## Structura Tichetelor
Fiecare tichet va conține următoarele informații:
- Data și ora creării
- Dotat cu senzori
- Transportator
- Număr cisternă
- Nume șofer
- Tip
- Nume stație
- Info stație
- Cod stație
- Tip stație
- Bypass (Da/Nu)
- Motiv bypass
- GPS
- Observații
- Utilizator (operatorul care creează tichetul)

  
##DOCUMENTATIE

- [Documentație Django](https://docs.djangoproject.com/)
- [Documentație HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Documentație CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Documentație JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Structura Proiectului

### Aplicația Django
- `tichet_app/` - Aplicația principală
- `tichet_app/models.py` - Modelele pentru tichete, utilizatori, cisterne, etc.
- `tichet_app/views.py` - Vizualizările pentru operarea tichetelor și gestionarea utilizatorilor
- `tichet_app/forms.py` - Formularele pentru crearea și editarea tichetelor

### Frontend
- `tichet_app/templates/` - Șabloanele HTML pentru paginile aplicației
- `tichet_app/static/` - Fișierele CSS și JavaScript

## Cerințe 
- Clonarea repository-ului și configurarea mediului de dezvoltare.
- Familiarizarea cu structura proiectului și codul existent.
- Implementarea funcționalităților conform cerințelor.
- Respectarea standardelor de codare și utilizarea controlului de versiuni prin Git.

## Fluxul de Lucru
- Fiecare student va lucra pe un branch separat.
- După implementarea unei funcționalități, se va crea un Pull Request pentru revizuire.
- După aprobare, funcționalitatea va fi integrată în branch-ul principal.

## Termene Limită
Finalizarea practicii


### Clonează Repository-ul de pe GitHub

git clone <repository_url>
cd <repository_directory>

### Instalare Dependințe
```bash
pip install -r requirements.txt


