import glob
import re

def verify_and_fix(filename):
    if filename in ['navbar.html', 'footer.html']:
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.strip()

    # Check for missing closing tags
    if not content.endswith('</html>'):
        if not content.endswith('</body>'):
            content += '\n</body>'
        content += '\n</html>'

    # Ensure there's a newline at the end
    content += '\n'

    # Verify if navbar fetch block exists
    if "fetch('navbar.html')" not in content:
        print(f"[WARNING] {filename} is missing fetch('navbar.html')!")
    elif "// Initialize navbar menu and dropdowns after injection" not in content:
         print(f"[WARNING] {filename} has OLD fetch('navbar.html') block!")
         
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[FIXED] Added missing closing tags to {filename}")
    else:
        print(f"[OK] {filename}")

for file in glob.glob('*.html'):
    verify_and_fix(file)
