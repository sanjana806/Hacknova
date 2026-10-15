with open(r'C:\Users\Dell\.gemini\antigravity\scratch\hacknova-2026\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('Video file src WhatsApp Video 2026-09-13 at 16.17.42_2.mp4', 'WhatsApp Video 2026-09-13 at 16.17.42_2.mp4' in html),
    ('sessionStorage check', 'sessionStorage.getItem' in html),
    ('Registration button on video', 'id="videoRegisterBtn"' in html),
    ('HACKNOVA 2026', 'HACKNOVA' in html and '2026' in html),
    ('Ambala College of Engineering and Applied Research', 'Ambala College of Engineering and Applied Research' in html),
    ('Where Education Is A Passion, Not A Business...', 'Where Education Is A Passion, Not A Business...' in html),
    ('Built by Sanjana', 'Built by' in html and 'Sanjana' in html),
    ('Instagram link', 'instagram.com/ambalacollegeofengineering' in html),
    ('LinkedIn link', 'linkedin.com/school/ambala-college-of-engineering-and-applied-research' in html),
    ('Google Maps link', 'google.com/maps' in html),
    ('CodroidHub sponsor present', 'CodroidHub' in html or 'codroidhub' in html),
    ('CodroidHub logo included', 'images/codroidhub_logo.png' in html),
    ('Short description of sponsor organization', 'CodroidHub Pvt Ltd' in html and 'premier technology innovation ecosystem' in html),
    ('Prizes section removed', 'id="prizes"' not in html and 'Spoils of Victory' not in html),
    ('OPERATIONS GUILD removed', 'OPERATIONS GUILD' not in html),
    ('COUNCIL OF ARCH-MAGES present', 'COUNCIL OF ARCH-MAGES' in html),
    ('ORDER OF THE PHOENIX present', 'ORDER OF THE PHOENIX' in html),
    ('Faculty photos used', 'faculty_dean_sk_jain.png' in html and 'faculty_gagandeep_kaur.png' in html and 'faculty_anuja.png' in html),
    ('Registration link updated', 'forms.gle/dTjX5Ks7AvPNaRxMA' in html),
    ('Day-time schedule 10:00 AM to 4:00 PM', '10:00 AM' in html and '4:00 PM' in html),
    ('Glimpses of ACE gallery', 'Glimpses of Ambala College of Engineering' in html)
]

all_pass = True
for name, res in checks:
    tag = 'PASS' if res else 'FAIL'
    print(f'[{tag}] {name}')
    if not res:
        all_pass = False

print('\nALL CHECKS PASSED:', all_pass)
