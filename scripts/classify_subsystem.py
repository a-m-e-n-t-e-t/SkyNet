"""SkyNet Classify Subsystem — классификация по 13 подсистемам (F3).
v9.25: полная реализация с ключевыми словами для всех 14 подсистем."""

SUBSYSTEMS = [
    'вычислительная', 'энергетическая', 'каркас', 'броня',
    'маскировка', 'встроенное_оружие', 'сенсоры', 'приводная_система',
    'система_связи', 'навигация', 'система_охлаждения',
    'система_питания', 'система_передвижения', 'прочее'
]

KEYWORDS = {
    'каркас': ['позвоночник', 'каркас', 'кост', 'сустав', 'таз', 'череп', 'грудная', 'бедренная',
               'спинной', 'плечевой', 'framework', 'chassis', 'skeleton', 'spine', 'rib'],
    'энергетическая': ['RTG', 'реактор', 'стирлинг', 'батарея', 'генератор', 'Pu-238', 'Am-241',
                       'SOFC', 'PEM', 'fuel cell', 'power source', 'reactor', 'battery', 'generator'],
    'вычислительная': ['CPU', 'GPU', 'NPU', 'процессор', 'память', 'memory', 'compute', 'neural',
                       'чип', 'chip', 'processor', 'RAM', 'SSD', 'FPGA', 'ASIC'],
    'броня': ['броня', 'armor', 'plate', 'керамика', 'ceramic', 'B4C', 'UHMWPE', 'kevlar',
              'защит', 'protect', 'NIJ', 'STANAG', 'ballistic'],
    'маскировка': ['маскиров', 'camouflag', 'stealth', 'хамелеон', 'chameleon', 'IR', 'thermal',
                   'radar', 'signature', 'infiltrat', 'RF', 'emcon'],
    'встроенное_оружие': ['оружие', 'weapon', 'плазма', 'plasma', 'laser', 'лазер', 'gatling',
                          'винтовка', 'rifle', 'EMP', 'railgun', 'рельсотрон'],
    'сенсоры': ['сенсор', 'sensor', 'камера', 'camera', 'LiDAR', 'лидар', 'радар', 'radar',
                'микрофон', 'microphone', 'тепловизор', 'thermal', 'IMU', 'MEMS', 'event camera'],
    'приводная_система': ['привод', 'actuator', 'серво', 'servo', 'гидравлик', 'hydraulic',
                          'мотор', 'motor', 'пневмо', 'pneumatic', 'muscle', 'McKibben'],
    'система_связи': ['связь', 'communication', 'радио', 'radio', 'антенн', 'antenna',
                      'WiFi', 'Bluetooth', 'satellite', 'Starlink', 'mesh', '5G', '6G'],
    'навигация': ['навигац', 'navigation', 'GPS', 'GNSS', 'IMU', 'инерциаль', 'inertial',
                  'SLAM', 'одометр', 'odometer', 'compass', 'компас'],
    'система_охлаждения': ['охлажд', 'cooling', 'радиатор', 'radiator', 'тепло', 'thermal',
                           'heat pipe', 'тепловая трубка', 'вентилятор', 'fan', 'cryo', 'Peltier'],
    'система_питания': ['питан', 'power', 'батарея', 'battery', 'конденсатор', 'capacitor',
                        'суперконденсатор', 'supercap', 'накопитель', 'buffer', 'Li-ion', 'Li-S'],
    'система_передвижения': ['передвиж', 'locomotion', 'колесо', 'wheel', 'гусениц', 'track',
                             'нога', 'leg', 'крыло', 'wing', 'винт', 'propeller', 'ротор', 'rotor'],
}


def classify(description: str) -> str:
    """Plan A: классификация по ключевым словам.
    
    Args:
        description: текст описания изделия
        
    Returns:
        имя подсистемы (одна из 13 + 'прочее')
    """
    if not description:
        return 'прочее'
    
    desc_lower = description.lower()
    scores = {}
    
    for subsystem, keywords in KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in desc_lower)
        if score > 0:
            scores[subsystem] = score
    
    if scores:
        return max(scores, key=scores.get)
    
    # Plan B: по аналогии (не реализовано — требует контекста существующих изделий)
    # Plan C: fallback
    return 'прочее'


def plan_A(description: str) -> str:
    """Псевдоним для classify (совместимость с field_contracts)."""
    return classify(description)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        result = classify(' '.join(sys.argv[1:]))
        print(result)
    else:
        print(f"Usage: {sys.argv[0]} <description>")
        print(f"Available subsystems: {', '.join(SUBSYSTEMS)}")
