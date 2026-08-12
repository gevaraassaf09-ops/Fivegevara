# ⚡ بطاقة مرجعية سريعة

## 🎯 أول استخدام؟ ابدأ هنا!

```bash
# 1. إعداد Git
git config --global user.name "اسمك"
git config --global user.email "email@example.com"

# 2. انسخ المشروع
git clone https://github.com/YOUR/diwan-military-app.git
cd diwan-military-app

# 3. ادخل Replit وشغل الخادم
pip install -r requirements.txt
python main.py

# 4. الرابط:
# https://diwan-military-app.replit.dev
```

---

## 📝 سير عملك اليومي

```bash
# الصباح: جلب آخر التحديثات
git pull

# طوال اليوم: تعديلات وحفظ
nano public/index.html
git add .
git commit -m "وصف التعديل"
git push

# المساء: نسخة احتياطية
# ادخل /admin.html وأنشئ نسخة
```

---

## 🔧 الأوامر الأساسية

| العملية | الأمر |
|--------|-------|
| عرض الحالة | `git status` |
| إضافة ملف | `git add filename` |
| إضافة الكل | `git add .` |
| حفظ محلي | `git commit -m "رسالة"` |
| رفع إلى GitHub | `git push` |
| جلب من GitHub | `git pull` |
| عرض السجل | `git log --oneline` |
| الرجوع لنسخة | `git checkout commit-id` |

---

## 🎯 رسائل Commit جيدة

```bash
❌ سيء:
git commit -m "update"

✅ جيد:
git commit -m "إضافة: ميزة الحفظ التلقائي"
git commit -m "إصلاح: خطأ في الحساب"
git commit -m "تحسين: سرعة التحميل 40%"
```

---

## 📊 رموز الحالة

| الرمز | المعنى |
|------|--------|
| `??` | ملف جديد لم يُضف |
| `M` | ملف معدل |
| `A` | ملف مضاف |
| `D` | ملف محذوف |

---

## 🌐 الروابط الرئيسية

```
التطبيق:     https://diwan-military-app.replit.dev
لوحة التحكم: https://diwan-military-app.replit.dev/admin.html
GitHub:     https://github.com/YOUR/diwan-military-app
```

---

## 💾 النسخ الاحتياطية

```javascript
// في Console (F12)

// إنشاء نسخة
fetch('/api/create-backup', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({name: 'نسختي', author: 'أنا'})
}).then(r => r.json()).then(d => alert(d.message));

// عرض النسخ
fetch('/api/list-backups')
  .then(r => r.json())
  .then(d => console.table(d.backups));

// استعادة نسخة
fetch('/api/restore-backup/BACKUP_ID', {method: 'POST'})
  .then(r => r.json())
  .then(d => location.reload());
```

---

## 🔄 المزامنة

```javascript
// في Console

// رفع إلى GitHub
fetch('/api/git-sync', {method: 'POST'})
  .then(r => r.json())
  .then(d => alert(d.message));

// جلب من GitHub
fetch('/api/sync-from-github', {method: 'POST'})
  .then(r => r.json())
  .then(d => location.reload());
```

---

## 🆘 حل سريع للمشاكل

| المشكلة | الحل |
|--------|------|
| الخادم لا يشتغل | `pip install -r requirements.txt` ثم `python main.py` |
| Git لا يعمل | `git config --global user.email "email@..."` |
| Push رفع | `git pull` أولاً ثم `git push` |
| التطبيق لا يحمل | `Ctrl+F5` لتحديث المتصفح |
| نسخة قديمة ظاهرة | انتظر دقيقة أو اضغط Ctrl+Shift+S |

---

## 📱 على الهاتف

```
1. افتح الرابط
2. اضغط ⋮ (القائمة)
3. "إضافة إلى الشاشة الرئيسية"
4. استخدمه كتطبيق عادي!
```

---

## ✅ قائمة تدقيق يومية

- [ ] جلبت آخر التحديثات (`git pull`)
- [ ] عملت نسخة احتياطية قبل تعديلات كبيرة
- [ ] اختبرت التعديلات محلياً
- [ ] أضفت الملفات (`git add .`)
- [ ] حفظت محلياً (`git commit`)
- [ ] رفعت التحديثات (`git push`)
- [ ] تحققت من الرابط (`https://...`)

---

## 📚 للمزيد من المساعدة

- الشرح الكامل: اقرأ `دليل_الإعداد.md`
- أوامر Git: اقرأ `GIT_GUIDE.md`
- شرح الملفات: اقرأ `FILES_GUIDE.md`
- البدء السريع: اقرأ `QUICK_START.md`

---

## 🎉 أنت جاهز!

ابدأ الآن:
```bash
git pull
nano public/index.html
# عدّل ما تريد
git add .
git commit -m "تعديل جديد"
git push
```

**التطبيق سيتحدث تلقائياً خلال دقيقة! 🚀**
