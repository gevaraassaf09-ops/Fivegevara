# الديوان العسكري — Military Admin System
## Diwan Al-Askari - Replit + GitHub Edition

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-Private-red)

---

## 📋 العربية

### نظام متقدم لإدارة البيانات العسكرية

تطبيق ويب عربي متكامل لإدارة العمليات الإدارية في الوحدات العسكرية، مع مميزات متقدمة للنسخ الاحتياطية والمزامنة التلقائية.

### ✨ المميزات الرئيسية

- 🌐 **واجهة ويب عربية كاملة** - دعم النصوص العربية والتنسيق من اليمين لليسار
- 💾 **نسخ احتياطية تلقائية** - حفظ تلقائي للنسخ مع إمكانية الاسترجاع
- 🔄 **مزامنة GitHub** - رفع وجلب التحديثات تلقائياً
- 📱 **متوافق مع الهواتف الذكية** - Progressive Web App (PWA)
- 👥 **مشاركة فورية** - رابط واحد لجميع المستخدمين
- 🔐 **أمان عالي** - نسخ احتياطية آمنة وحفظ البيانات

### 🚀 البدء السريع

```bash
# 1. استنساخ المشروع
git clone https://github.com/YOUR_USERNAME/diwan-military-app.git
cd diwan-military-app

# 2. تثبيت المكتبات
pip install -r requirements.txt

# 3. التشغيل
python main.py

# 4. افتح المتصفح على
http://localhost:5000
```

### 📁 بنية المشروع

```
diwan-military-app/
├── main.py                 # خادم Python الرئيسي
├── requirements.txt        # المكتبات المطلوبة
├── .gitignore             # ملفات مستبعدة من Git
├── .replit                # تكوين Replit
├── public/
│   └── index.html         # التطبيق الرئيسي
├── admin.html             # لوحة التحكم
├── backups/               # مجلد النسخ الاحتياطية
└── دليل_الإعداد.md       # دليل شامل
```

### 🔧 الـ API المتاحة

| الطلب | الغرض |
|------|-------|
| `GET /` | تحميل التطبيق الرئيسي |
| `GET /admin.html` | لوحة التحكم |
| `GET /api/status` | حالة الخادم |
| `POST /api/create-backup` | إنشاء نسخة احتياطية |
| `POST /api/restore-backup/<id>` | استرجاع نسخة |
| `GET /api/list-backups` | قائمة النسخ |
| `POST /api/git-sync` | مزامنة مع GitHub |
| `POST /api/sync-from-github` | جلب من GitHub |

### 📊 لوحة التحكم

ادخل إلى `http://your-app/admin.html` لـ:
- عرض حالة الخادم
- إنشاء نسخ احتياطية
- استعادة النسخ القديمة
- مزامنة مع GitHub يدويًا

### 🔐 الأمان

- الملفات الحساسة موجودة في `.gitignore`
- استخدم `Environment Variables` للبيانات الحساسة
- النسخ الاحتياطية محفوظة محلياً
- يمكن استخدام Private Repository على GitHub

### 📖 موارد إضافية

- [دليل الإعداد الكامل](./دليل_الإعداد.md)
- [توثيق Flask](https://flask.palletsprojects.com)
- [توثيق Replit](https://docs.replit.com)
- [توثيق GitHub](https://docs.github.com)

---

## 🇬🇧 English

### Advanced Military Administration System

A comprehensive Arabic web application for managing administrative processes in military units, with advanced backup and automatic synchronization features.

### ✨ Key Features

- 🌐 **Full Arabic Interface** - Complete RTL support with Arabic fonts
- 💾 **Automatic Backups** - Save and restore versions instantly
- 🔄 **GitHub Sync** - Push and pull updates automatically
- 📱 **Mobile Ready** - Progressive Web App (PWA) support
- 👥 **Real-time Sharing** - Single link for all users
- 🔐 **High Security** - Encrypted backups and data persistence

### 🚀 Quick Start

```bash
# 1. Clone the project
git clone https://github.com/YOUR_USERNAME/diwan-military-app.git
cd diwan-military-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py

# 4. Open browser at
http://localhost:5000
```

### 📁 Project Structure

```
diwan-military-app/
├── main.py                 # Main Python server
├── requirements.txt        # Required packages
├── .gitignore             # Ignored files
├── .replit                # Replit configuration
├── public/
│   └── index.html         # Main application
├── admin.html             # Admin dashboard
├── backups/               # Backup directory
└── دليل_الإعداد.md       # Full setup guide
```

### 🔧 Available APIs

| Method | Purpose |
|--------|---------|
| `GET /` | Load main app |
| `GET /admin.html` | Admin dashboard |
| `GET /api/status` | Server status |
| `POST /api/create-backup` | Create backup |
| `POST /api/restore-backup/<id>` | Restore backup |
| `GET /api/list-backups` | List backups |
| `POST /api/git-sync` | Sync to GitHub |
| `POST /api/sync-from-github` | Pull from GitHub |

### 🔐 Security

- Sensitive files in `.gitignore`
- Use `Environment Variables` for secrets
- Local backup storage
- Support for Private GitHub repositories

### 📊 Admin Dashboard

Visit `http://your-app/admin.html` to:
- View server status
- Create manual backups
- Restore old versions
- Manual GitHub sync

### 📖 Additional Resources

- [Full Setup Guide](./دليل_الإعداد.md)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Replit Docs](https://docs.replit.com)
- [GitHub Docs](https://docs.github.com)

---

## 💬 Support

للدعم والمساعدة، راجع ملف دليل الإعداد أو تواصل مع فريق الدعم.

For support and help, refer to the setup guide or contact the support team.

---

## 📄 License

Private - All rights reserved

---

**Made with ❤️ for Syrian Military Administration**
