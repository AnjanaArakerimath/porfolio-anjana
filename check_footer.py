import re

files = ['index.html', 'gallery.html', 'sig.html', 'contact.html', 'outside_interaction.html', 'rangoli.html', 'project.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_footer_div = 'id="footer"' in content
    has_footer_fetch = "fetch('footer.html')" in content or 'fetch("footer.html")' in content
    has_inline_footer = '<footer' in content
    
    print(f'{file}: div_placeholder={has_footer_div}, fetch_footer={has_footer_fetch}, inline_footer={has_inline_footer}')
