import os
import re

# The replacement placeholder div and fetch script
footer_placeholder = '  <div id="footer"></div>'
footer_fetch_script = """  <script>
    fetch('footer.html')
      .then(response => response.text())
      .then(data => {
          document.getElementById('footer').innerHTML = data;
      });
  </script>"""

# Pattern to match the full footer block (from <footer to </footer>)
footer_pattern = re.compile(r'\s*<footer[\s\S]*?</footer>', re.IGNORECASE)

# Also check if there's already a footer fetch script to avoid duplicating
footer_fetch_pattern = re.compile(r"fetch\(['\"]footer\.html['\"]\)", re.IGNORECASE)

files_updated = []
files_skipped = []

for file in os.listdir('.'):
    if not file.endswith('.html') or file == 'footer.html' or file == 'navbar.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already using footer.html fetch
    if footer_fetch_pattern.search(content):
        files_skipped.append(file + ' (already uses footer.html)')
        continue
    
    # Replace the inline footer with the placeholder div
    new_content, count = footer_pattern.subn(footer_placeholder, content)
    
    if count == 0:
        files_skipped.append(file + ' (no footer found)')
        continue
    
    # Insert the fetch script just before </body>
    new_content = re.sub(r'(</body>)', footer_fetch_script + '\n\\1', new_content, flags=re.IGNORECASE)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    files_updated.append(file)

print("Updated files:")
for f in files_updated:
    print(f"  [OK] {f}")

print("\nSkipped files:")
for f in files_skipped:
    print(f"  [-] {f}")
