import os
import re

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove all instances of <link href="style.css" rel="stylesheet"> or similar
        # Be careful to catch variations
        new_content, count = re.subn(r'<link\s+href="style\.css"\s+rel="stylesheet"\s*>\s*', '', content)
        
        if count > 0:
            # It was removed, now insert it before </head>
            new_content = re.sub(r'(</head>)', r'  <link href="style.css" rel="stylesheet">\n\1', new_content, flags=re.IGNORECASE)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed CSS order in {file}')
