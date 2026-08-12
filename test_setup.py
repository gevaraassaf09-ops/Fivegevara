#!/usr/bin/env python3
"""
سكريبت اختبار الإعداد
يتحقق من أن جميع الملفات والإعدادات صحيحة
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}")

def print_success(text):
    print(f"✅ {text}")

def print_error(text):
    print(f"❌ {text}")

def print_warning(text):
    print(f"⚠️  {text}")

def print_info(text):
    print(f"ℹ️  {text}")

def check_python_version():
    print_header("فحص إصدار Python")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print_success(f"Python {version.major}.{version.minor} مثبت")
        return True
    else:
        print_error(f"Python {version.major}.{version.minor} قديم جداً (يجب 3.7+)")
        return False

def check_required_files():
    print_header("فحص الملفات المطلوبة")
    required_files = [
        'main.py',
        'requirements.txt',
        '.replit',
        '.gitignore',
        'README.md',
        'public/index.html',
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print_success(f"موجود: {file}")
        else:
            print_error(f"مفقود: {file}")
            all_exist = False
    
    return all_exist

def check_git_config():
    print_header("فحص إعدادات Git")
    try:
        user_name = subprocess.check_output(
            ['git', 'config', '--global', 'user.name'],
            text=True
        ).strip()
        
        user_email = subprocess.check_output(
            ['git', 'config', '--global', 'user.email'],
            text=True
        ).strip()
        
        if user_name and user_email:
            print_success(f"Git مُعدّ: {user_name} <{user_email}>")
            return True
        else:
            print_warning("Git مثبت لكن بدون بيانات هوية")
            print_info("اكتب:")
            print_info("  git config --global user.name 'اسمك'")
            print_info("  git config --global user.email 'email@example.com'")
            return False
    except FileNotFoundError:
        print_error("Git غير مثبت!")
        return False

def check_git_repo():
    print_header("فحص مستودع Git")
    try:
        result = subprocess.run(
            ['git', 'status'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success("هذا مجلد Git صحيح")
            
            # عرض الفرع الحالي
            branch = subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                text=True
            ).strip()
            print_info(f"الفرع الحالي: {branch}")
            
            return True
        else:
            print_warning("هذا المجلد ليس مستودع Git")
            print_info("اكتب: git init")
            return False
    except FileNotFoundError:
        print_error("Git غير مثبت!")
        return False

def check_python_packages():
    print_header("فحص مكتبات Python")
    try:
        with open('requirements.txt', 'r') as f:
            required = [line.split('==')[0].strip() for line in f if line.strip()]
        
        missing = []
        for package in required:
            try:
                __import__(package.replace('-', '_'))
                print_success(f"مثبت: {package}")
            except ImportError:
                print_warning(f"غير مثبت: {package}")
                missing.append(package)
        
        if missing:
            print_warning(f"المكتبات المفقودة: {', '.join(missing)}")
            print_info("اكتب: pip install -r requirements.txt")
            return False
        return True
    except FileNotFoundError:
        print_error("ملف requirements.txt غير موجود")
        return False

def check_html_file():
    print_header("فحص ملف HTML")
    html_file = Path('public/index.html')
    
    if html_file.exists():
        size_mb = html_file.stat().st_size / (1024 * 1024)
        print_success(f"موجود: public/index.html ({size_mb:.1f} MB)")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'الديوان' in content or 'military' in content.lower():
            print_success("محتوى صحيح (يحتوي على كلمات عربية)")
            return True
        else:
            print_warning("قد لا يكون ملف المشروع الصحيح")
            return True
    else:
        print_error("ملف public/index.html غير موجود")
        return False

def check_directories():
    print_header("فحص المجلدات")
    directories = [
        'public',
        'backups',
    ]
    
    all_exist = True
    for dir_name in directories:
        dir_path = Path(dir_name)
        if dir_path.exists():
            print_success(f"موجود: {dir_name}/")
        else:
            print_warning(f"غير موجود: {dir_name}/")
            print_info(f"سيتم إنشاؤه تلقائياً عند التشغيل")
    
    return True

def check_can_run_server():
    print_header("فحص صحة الخادم")
    try:
        import flask
        print_success("Flask مثبت ويعمل")
        
        # محاولة استيراد main.py
        try:
            import main
            print_success("main.py يمكن استيراده بنجاح")
            return True
        except Exception as e:
            print_error(f"خطأ في main.py: {e}")
            return False
    except ImportError:
        print_error("Flask غير مثبت")
        print_info("اكتب: pip install Flask")
        return False

def main():
    print("\n" + "="*50)
    print("🔍 اختبار إعداد الديوان العسكري")
    print("="*50)
    
    results = {}
    
    results['Python'] = check_python_version()
    results['الملفات'] = check_required_files()
    results['Git Config'] = check_git_config()
    results['Git Repo'] = check_git_repo()
    results['مكتبات Python'] = check_python_packages()
    results['ملف HTML'] = check_html_file()
    results['المجلدات'] = check_directories()
    results['الخادم'] = check_can_run_server()
    
    # ملخص النتائج
    print_header("📊 ملخص النتائج")
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        symbol = "✅" if result else "❌"
        print(f"{symbol} {check}")
    
    print(f"\nالنتيجة: {passed}/{total} ✅")
    
    if passed == total:
        print_success("\n🎉 جميع الاختبارات نجحت! أنت جاهز للبدء!")
        print_info("لتشغيل الخادم، اكتب:")
        print_info("  python main.py")
        return 0
    else:
        print_warning(f"\n⚠️  {total - passed} اختبار لم ينجح")
        print_info("راجع الأخطاء أعلاه وحاول إصلاحها")
        return 1

if __name__ == '__main__':
    sys.exit(main())
