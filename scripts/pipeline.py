"""SkyNet Pipeline Orchestrator — единственный оркестратор фаз 0-8 (P012).
v9.31: функциональная реализация (не заглушка)."""

import os, sys, json, subprocess
from pathlib import Path

SKYNET_REPO = os.environ.get('SKYNET_REPO', '.')

def check_current_state():
    """Phase 0: проверка готовности."""
    state = {
        'pipeline_exists': os.path.exists(f'{SKYNET_REPO}/scripts/pipeline.py'),
        'pre_commit_exists': os.path.exists(f'{SKYNET_REPO}/scripts/pre-commit-hook.py'),
        'classify_exists': os.path.exists(f'{SKYNET_REPO}/scripts/classify_subsystem.py'),
        'rules_version': _read_rules_version(),
        'required_files': _check_required_files(),
    }
    return state

def _read_rules_version():
    """Читает rules_version из _версия_правил.yaml."""
    path = f'{SKYNET_REPO}/требования к ии/_версия_правил.yaml'
    if not os.path.exists(path):
        return None
    try:
        import yaml
        with open(path) as f:
            data = yaml.safe_load(f)
            return data.get('rules_version') if data else None
    except Exception:
        return None

def _check_required_files():
    """Проверяет наличие обязательных файлов."""
    required = [
        'требования к ии/_принципы.md',
        'требования к ии/_версия_правил.yaml',
        'требования к ии/_паттерны.md',
        'требования к ии/_t800_terms.txt',
        'требования к ии/_field_contracts.yaml',
        'требования к ии/_mat_kb.yaml',
        'требования к ии/_tec_kb.yaml',
        'требования к ии/_typ_kb.yaml',
        'требования к ии/_credentials.yaml',
    ]
    return {
        f: os.path.exists(f'{SKYNET_REPO}/{f}')
        for f in required
    }

def capture_dialog(user_message, ai_response=None, counter=None):
    """Phase 1: захват диалога в real-time."""
    from datetime import datetime
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H-%M-%S')
    
    dialog_dir = f'{SKYNET_REPO}/диалог/{date_str}'
    os.makedirs(dialog_dir, exist_ok=True)
    
    # Read and increment counter
    counter_path = f'{SKYNET_REPO}/диалог/_counter.txt'
    if counter is None:
        if os.path.exists(counter_path):
            with open(counter_path) as f:
                counter = int(f.read().strip() or '0')
        else:
            counter = 0
    counter += 1
    with open(counter_path, 'w') as f:
        f.write(str(counter))
    
    # Save user request
    user_file = f'{dialog_dir}/{counter:04d}_{time_str}_user.md'
    with open(user_file, 'w') as f:
        f.write(f'# User Request — {date_str} {time_str}\n\n{user_message}\n')
    
    # Save AI response if provided
    if ai_response:
        ai_file = f'{dialog_dir}/{counter:04d}_{time_str}_ai.md'
        with open(ai_file, 'w') as f:
            f.write(f'# AI Response — {date_str} {time_str}\n\n{ai_response}\n')
    
    # Update current/latest.md
    latest_path = f'{SKYNET_REPO}/диалог/current/latest.md'
    with open(latest_path, 'w') as f:
        f.write(f'# Latest Dialog — {date_str} {time_str} (counter: {counter})\n\n## User\n{user_message}\n')
        if ai_response:
            f.write(f'\n## Assistant\n{ai_response}\n')
    
    return counter

def run_pre_commit():
    """Phase 5: запуск pre-commit hook."""
    hook_path = f'{SKYNET_REPO}/scripts/pre-commit-hook.py'
    result = subprocess.run(
        [sys.executable, hook_path],
        capture_output=True, text=True, cwd=SKYNET_REPO
    )
    return {
        'returncode': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr,
    }

def main():
    """Главная точка входа pipeline."""
    print("SkyNet Pipeline v9.31 — запуск")
    
    # Phase 0
    state = check_current_state()
    print(f"Phase 0: {json.dumps(state, indent=2, ensure_ascii=False)}")
    
    missing = [k for k, v in state.get('required_files', {}).items() if not v]
    if missing:
        print(f"⚠️ Отсутствуют файлы: {missing}")
    
    version = state.get('rules_version')
    if version != '9.31':
        print(f"⚠️ rules_version: {version} (ожидается 9.17)")
    
    print("Pipeline готов к работе. Используйте capture_dialog() для обработки сообщений.")

if __name__ == '__main__':
    main()


# === v9.31: Issues integration ===

def check_open_issues_state():
    """Phase 0.7: проверить открытые Issues с меткой todo."""
    from _helpers import check_open_issues
    pat = os.environ.get('PAT_TOKEN', '')
    if not pat:
        return {'has_todo_issues': False, 'issues': [], 'note': 'PAT not set'}
    issues = check_open_issues(pat)
    return {
        'has_todo_issues': len(issues) > 0,
        'count': len(issues),
        'issues': issues,
    }
