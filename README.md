# 💼 Sayfulloh Mamatqulov — Portfolio

> Shaxsiy portfolio veb-sayti. Django 6.0 asosida qurilgan, vCard dizayn uslubida.

---

## 🌐 Live Demo

🔗 **[sayfulloh.dev](https://sayfulloh.dev)** *(tez orada)*

---

## ✨ Imkoniyatlar

- 👤 **Men haqimda** — bio, hizmatlar va ijtimoiy tarmoqlar
- 📄 **Rezume** — ish tajribasi, ta'lim va ko'nikmalar (progress bar)
- 🗂️ **Loyihalar** — filter bilan loyihalar galereyasi
- 📝 **Blog** — maqolalar
- 📬 **Xabar** — contact forma (email bildirishnoma bilan)
- 🌙 **Dark dizayn** — vCard Personal Portfolio uslubi
- 📱 **Responsive** — mobil, planshet va desktop
- ⚡ **Admin panel** — barcha ma'lumotlar Django admin orqali boshqariladi

---

## 🛠️ Texnologiyalar

| Qatlam | Texnologiya |
|--------|-------------|
| Backend | Django 6.0 |
| Database | PostgreSQL |
| Frontend | HTML, CSS (vCard), Ionicons |
| Media | Pillow |
| Static files | WhiteNoise |
| Server | Gunicorn + Nginx |
| Deploy | Ubuntu VPS (Contabo) |

---

## 🚀 Lokal ishga tushirish

### Talablar
- Python 3.11+
- PostgreSQL

### O'rnatish

```bash
# 1. Reponi klonlash
git clone https://github.com/sayfulloh77/portfolio.git
cd portfolio

# 2. Virtual muhit
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 3. Kutubxonalar
pip install -r requirements.txt

# 4. .env fayl
cp .env.example .env
# .env faylni o'z ma'lumotlaringiz bilan to'ldiring

# 5. Ma'lumotlar bazasi
python manage.py migrate

# 6. Superuser yaratish
python manage.py createsuperuser

# 7. Ishga tushirish
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000**  
Admin panel: **http://127.0.0.1:8000/admin**

---

## ⚙️ .env sozlamalari

```env
SECRET_KEY=django-insecure-...
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=portfolio_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

> ⚠️ `.env` faylni hech qachon GitHubga yuklamang!

---

## 📁 Loyiha tuzilmasi

```
portfolio/
├── account/          # Foydalanuvchi, kontakt
├── blog/             # Maqolalar
├── work/             # Loyihalar, tajriba, ko'nikmalar, hizmatlar
├── common/           # Media model
├── core/             # settings.py, urls.py
├── templates/        # HTML shablonlar
├── static/           # CSS, JS, rasmlar
├── deploy/           # Nginx, Gunicorn, setup skripti
├── .env.example      # Muhit o'zgaruvchilari namunasi
└── requirements.txt
```

---

## 🖥️ Deploy (Ubuntu VPS)

```bash
# Server sozlash
bash deploy/setup.sh

# Servis holati
systemctl status portfolio
systemctl status nginx
```

Batafsil: [`deploy/setup.sh`](deploy/setup.sh)

---

## 📬 Aloqa

| | |
|---|---|
| 📧 Email | [sayfulloh.dev@gmail.com](mailto:sayfulloh.dev@gmail.com) |
| 💬 Telegram | [@sayfulloh__Mamatqulov](https://t.me/sayfulloh__Mamatqulov) |
| 🐙 GitHub | [@sayfulloh77](https://github.com/sayfulloh77) |

---

<p align="center">
  <img src="https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-16-blue?style=flat-square&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>
