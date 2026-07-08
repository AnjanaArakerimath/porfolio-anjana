import os
import re

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'navbar.html':
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove all inline footer styles to enforce consistency
        updated = re.sub(r'footer\s*\{[^}]*\}', '', content, flags=re.DOTALL)
        
        # Reduce footer height by changing py-5 to py-3
        updated = updated.replace('<footer class="py-5"', '<footer class="py-3"')
        
        # Reduce spacing in footer elements
        updated = updated.replace('mb-4 mb-md-0', 'mb-2 mb-md-0')
        updated = updated.replace('mt-4 mb-4', 'mt-3 mb-3')
        updated = updated.replace('mt-4', 'mt-2')
        updated = updated.replace('mb-4', 'mb-2')
        updated = updated.replace('mt-3', 'mt-2')
        
        if updated != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Cleaned up {file}")

print("Done cleaning up footer heights and inline styles.")
