# 🏟️ Backend Il Mio Calcio

Backend realizzato in **Django + Django REST Framework**, con autenticazione tramite **JWT (JSON Web Token)** e gestione utenti personalizzata.  
Questo backend serve come API per l'applicazione **Il Mio Calcio**, che permette di registrarsi, autenticarsi e salvare la propria squadra preferita.

---

## ⚙️ Funzionalità principali
- Registrazione e login con **CustomUser**
- Autenticazione sicura tramite **JWT**
- Endpoint per aggiornare e recuperare la **squadra preferita**
- Endpoint `/auth/me/` per ottenere i dati dell’utente loggato
- API REST strutturate con Django REST Framework

---

## 📡 Endpoints principali
| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/auth/register/` | POST | Registrazione nuovo utente |
| `/auth/login/` | POST | Login tradizionale (non JWT) |
| `/auth/token/` | POST | Login e rilascio token JWT |
| `/auth/token/refresh/` | POST | Refresh token JWT |
| `/auth/favorite/` | POST | Aggiornamento squadra preferita (richiede autenticazione) |
| `/auth/me/` | GET | Ritorna i dati dell’utente autenticato |

---

## 🛠️ Tecnologie utilizzate
- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **SimpleJWT**
- **SQLite / MySQL** (configurabile)

---

## 🚀 Setup progetto
Clona il repository:
```bash
git clone https://github.com/TUO-USERNAME/ilmiocalcio-backend.git
cd ilmiocalcio-backend
Crea ed attiva un virtual environment:

bash
Copia codice
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
Installa le dipendenze:

bash
Copia codice
pip install -r requirements.txt
Applica le migrazioni e avvia il server:

bash
Copia codice
python manage.py migrate
python manage.py runserver
🔑 Autenticazione
Per effettuare chiamate agli endpoint protetti:

Ottenere un access token con:

bash
Copia codice
POST /auth/token/
{
  "username": "tuo_username",
  "password": "tua_password"
}
Aggiungere l’header Authorization: Bearer <access_token> ad ogni richiesta.

📂 Struttura progetto
bash
Copia codice
/backend
 ├── auth_app/       # App per gestione utenti e autenticazione
 ├── backend/        # Configurazione Django
 ├── db.sqlite3      # Database locale (default)
 ├── manage.py       # Script di gestione
 └── requirements.txt
✨ Autore
Sviluppato da Lorenzo Paniccia per il progetto Il Mio Calcio ⚽
