from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import json
import os
import shutil
from pathlib import Path
import subprocess

app = Flask(__name__, static_url_path='', static_folder='public')

# إعدادات المسارات
BACKUP_DIR = Path('backups')
CURRENT_VERSION_FILE = Path('current_version.json')
UPLOADS_DIR = Path('uploads')

# إنشاء المجلدات المطلوبة
BACKUP_DIR.mkdir(exist_ok=True)
UPLOADS_DIR.mkdir(exist_ok=True)

# تهيئة ملف النسخة الحالية
def init_version_file():
    if not CURRENT_VERSION_FILE.exists():
        version_data = {
            'created_at': datetime.now().isoformat(),
            'last_modified': datetime.now().isoformat(),
            'author': 'admin',
            'description': 'النسخة الأولية'
        }
        with open(CURRENT_VERSION_FILE, 'w', encoding='utf-8') as f:
            json.dump(version_data, f, ensure_ascii=False, indent=2)

init_version_file()

@app.route('/')
def index():
    """تقديم التطبيق الرئيسي"""
    return send_file('public/index.html', mimetype='text/html')

@app.route('/api/status', methods=['GET'])
def get_status():
    """الحصول على حالة التطبيق والنسخ الاحتياطية"""
    try:
        with open(CURRENT_VERSION_FILE, 'r', encoding='utf-8') as f:
            version_info = json.load(f)
        
        backups = []
        for backup_file in sorted(BACKUP_DIR.glob('backup_*.json'), reverse=True)[:10]:
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_info = json.load(f)
                backups.append(backup_info)
        
        return jsonify({
            'status': 'active',
            'version': version_info,
            'backups': backups,
            'server_time': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/create-backup', methods=['POST'])
def create_backup():
    """إنشاء نسخة احتياطية يدوية"""
    try:
        data = request.get_json()
        backup_name = data.get('name', 'نسخة يدوية')
        author = data.get('author', 'unknown')
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = BACKUP_DIR / f'backup_{timestamp}.json'
        
        backup_data = {
            'timestamp': datetime.now().isoformat(),
            'name': backup_name,
            'author': author,
            'description': data.get('description', ''),
            'html_size': os.path.getsize('public/index.html') if Path('public/index.html').exists() else 0
        }
        
        # حفظ بيانات النسخة الاحتياطية
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, ensure_ascii=False, indent=2)
        
        # نسخ ملف HTML الكامل
        if Path('public/index.html').exists():
            html_backup = BACKUP_DIR / f'backup_{timestamp}.html'
            shutil.copy('public/index.html', html_backup)
        
        return jsonify({
            'success': True,
            'backup_id': timestamp,
            'message': f'تم إنشاء نسخة احتياطية: {backup_name}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/restore-backup/<backup_id>', methods=['POST'])
def restore_backup(backup_id):
    """استرجاع نسخة احتياطية"""
    try:
        html_file = BACKUP_DIR / f'backup_{backup_id}.html'
        if not html_file.exists():
            return jsonify({'error': 'النسخة الاحتياطية غير موجودة'}), 404
        
        # إنشاء نسخة احتياطية من النسخة الحالية قبل الاستعادة
        current_backup = BACKUP_DIR / f'backup_before_restore_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        if Path('public/index.html').exists():
            shutil.copy('public/index.html', current_backup)
        
        # استرجاع النسخة
        shutil.copy(html_file, 'public/index.html')
        
        return jsonify({
            'success': True,
            'message': f'تم استرجاع النسخة بنجاح'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get-backup/<backup_id>', methods=['GET'])
def get_backup(backup_id):
    """تحميل نسخة احتياطية"""
    try:
        html_file = BACKUP_DIR / f'backup_{backup_id}.html'
        if html_file.exists():
            return send_file(html_file, mimetype='text/html', as_attachment=True)
        return jsonify({'error': 'النسخة غير موجودة'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/git-sync', methods=['POST'])
def git_sync():
    """مزامنة مع GitHub"""
    try:
        # تنفيذ أوامر Git
        subprocess.run(['git', 'add', '.'], check=True, cwd='.')
        subprocess.run(['git', 'commit', '-m', f'Auto sync from Replit - {datetime.now().isoformat()}'], 
                      check=True, cwd='.')
        subprocess.run(['git', 'push'], check=True, cwd='.')
        
        return jsonify({
            'success': True,
            'message': 'تم المزامنة مع GitHub بنجاح',
            'timestamp': datetime.now().isoformat()
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'خطأ في المزامنة: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sync-from-github', methods=['POST'])
def sync_from_github():
    """جلب آخر النسخ من GitHub"""
    try:
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True, cwd='.')
        
        return jsonify({
            'success': True,
            'message': 'تم جلب آخر التحديثات من GitHub',
            'timestamp': datetime.now().isoformat()
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'خطأ في الجلب: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/list-backups', methods=['GET'])
def list_backups():
    """قائمة بجميع النسخ الاحتياطية"""
    try:
        backups = []
        for backup_file in sorted(BACKUP_DIR.glob('backup_*.json'), reverse=True):
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
                backup_data['id'] = backup_file.stem.replace('backup_', '')
                backups.append(backup_data)
        
        return jsonify({
            'success': True,
            'backups': backups,
            'total': len(backups)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/manifest.json')
def manifest():
    """ملف PWA"""
    manifest_data = {
        "name": "الديوان العسكري",
        "short_name": "الديوان",
        "description": "نظام إدارة عسكري",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#243318",
        "icons": [
            {
                "src": "/icon.png",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]
    }
    return jsonify(manifest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
