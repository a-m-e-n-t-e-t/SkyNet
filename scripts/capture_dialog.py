"""SkyNet Capture Dialog — захват диалога в real-time (E1-E4).
v9.25: функциональная реализация."""

import os, json
from datetime import datetime

SKYNET_REPO = os.environ.get('SKYNET_REPO', '.')

DIALOG_DIR = os.path.join(SKYNET_REPO, 'диалог')
COUNTER_FILE = os.path.join(DIALOG_DIR, '_counter.txt')
CURRENT_DIR = os.path.join(DIALOG_DIR, 'current')
LATEST_FILE = os.path.join(CURRENT_DIR, 'latest.md')
CONTEXT_FILE = os.path.join(CURRENT_DIR, 'session_context.json')
CHANGELOG_FILE = os.path.join(DIALOG_DIR, 'CHANGELOG.md')


def get_counter() -> int:
    """Читает и инкрементирует счётчик диалога."""
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as f:
            try:
                return int(f.read().strip() or '0')
            except ValueError:
                return 0
    return 0


def increment_counter(counter: int) -> int:
    """Увеличивает счётчик и записывает в файл."""
    counter += 1
    os.makedirs(DIALOG_DIR, exist_ok=True)
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))
    return counter


def capture(user_message: str, ai_response: str = None, counter: int = None) -> dict:
    """Сохраняет диалог в диалог/YYYY-MM-DD/.
    
    Args:
        user_message: текст запроса пользователя
        ai_response: текст ответа ИИ (опционально)
        counter: номер сообщения (если None — читается из _counter.txt)
    
    Returns:
        dict с метаданными захвата
    """
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H-%M-%S')
    timestamp = now.isoformat()
    
    if counter is None:
        counter = get_counter()
    counter = increment_counter(counter)
    
    # Create date directory
    date_dir = os.path.join(DIALOG_DIR, date_str)
    os.makedirs(date_dir, exist_ok=True)
    
    # Save user request
    user_file = os.path.join(date_dir, f'{counter:04d}_{time_str}_user.md')
    with open(user_file, 'w', encoding='utf-8') as f:
        f.write(f'# User Request — {date_str} {time_str}\n\n{user_message}\n')
    
    # Save AI response if provided
    ai_file = None
    if ai_response:
        ai_file = os.path.join(date_dir, f'{counter:04d}_{time_str}_ai.md')
        with open(ai_file, 'w', encoding='utf-8') as f:
            f.write(f'# AI Response — {date_str} {time_str}\n\n{ai_response}\n')
    
    # Save summary JSON
    summary = {
        'timestamp': timestamp,
        'counter': counter,
        'date': date_str,
        'time': time_str,
        'user_file': os.path.relpath(user_file, SKYNET_REPO),
        'ai_file': os.path.relpath(ai_file, SKYNET_REPO) if ai_file else None,
    }
    summary_file = os.path.join(date_dir, f'{counter:04d}_{time_str}_summary.json')
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    # Update current/latest.md
    os.makedirs(CURRENT_DIR, exist_ok=True)
    with open(LATEST_FILE, 'w', encoding='utf-8') as f:
        f.write(f'# Latest Dialog — {date_str} {time_str} (counter: {counter})\n\n')
        f.write(f'## User\n{user_message}\n')
        if ai_response:
            f.write(f'\n## Assistant\n{ai_response}\n')
    
    # Update session_context.json
    context = {
        'version': '1.0',
        'session_id': '',
        'counter': counter,
        'last_update': timestamp,
        'current_phase': '',
        'next_action': '',
    }
    with open(CONTEXT_FILE, 'w', encoding='utf-8') as f:
        json.dump(context, f, indent=2, ensure_ascii=False)
    
    # Update CHANGELOG.md
    changelog_entry = f'| {date_str} | {counter:04d} | {time_str} | pending |\n'
    if os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, 'r', encoding='utf-8') as f:
            existing = f.read()
        # Insert after header
        lines = existing.split('\n')
        # Find the table header end
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('|---'):
                insert_idx = i + 1
                break
        lines.insert(insert_idx, changelog_entry.strip())
        with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    else:
        with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
            f.write('# Dialog Changelog\n\n| Дата | Counter | Время | Коммит |\n|---|---|---|---|\n')
            f.write(changelog_entry)
    
    return summary


if __name__ == '__main__':
    # Test
    result = capture("Test message", "Test AI response")
    print(f"Captured: counter={result['counter']}, file={result['user_file']}")
