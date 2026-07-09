import glob
import re

new_script = """fetch('navbar.html')
      .then(response => response.text())
      .then(data => {
          document.getElementById('navbar').innerHTML = data;
      });

      // Global event delegation for navbar
      document.addEventListener('click', function(e) {
          const toggle = e.target.closest('#nav-toggle');
          if (toggle) {
              const nav = document.getElementById('nav-menu');
              if (nav) {
                  nav.classList.toggle('show-menu');
                  toggle.classList.toggle('show-icon');
              }
          }
          
          const dropdownBtn = e.target.closest('.dropdown__button');
          if (dropdownBtn) {
              const item = dropdownBtn.closest('.dropdown__item');
              if (item) {
                  const showDropdown = document.querySelector('.show-dropdown');
                  const dropdownContainer = item.querySelector('.dropdown__container');
                  if(item.classList.contains('show-dropdown')){
                      dropdownContainer.removeAttribute('style');
                      item.classList.remove('show-dropdown');
                  } else {
                      dropdownContainer.style.height = dropdownContainer.scrollHeight + 'px';
                      item.classList.add('show-dropdown');
                  }
                  
                  if(showDropdown && showDropdown !== item){
                      const oldContainer = showDropdown.querySelector('.dropdown__container');
                      if(oldContainer) oldContainer.removeAttribute('style');
                      showDropdown.classList.remove('show-dropdown');
                  }
              }
          }
      });"""

def process_file(filename):
    if filename in ['navbar.html', 'footer.html']: return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace everything from fetch('navbar.html') up to the closing }); 
    # of the previous block we added.
    
    # We will match the old advanced_fetch block
    pattern = re.compile(r"fetch\('navbar\.html'\)[\s\S]*?oldContainer\.removeAttribute\('style'\);\s*showDropdown\.classList\.remove\('show-dropdown'\);\s*\}\s*\}\);\s*\}\s*\}\);\s*\}\);\s*", re.MULTILINE)
    
    # Also match the basic fetch block just in case
    pattern_basic = re.compile(r"fetch\('navbar\.html'\)\s*\.then\([^)]+\)\s*\.then\([^{]+\{\s*document\.getElementById\('navbar'\)\.innerHTML\s*=\s*[a-zA-Z]+;\s*\}\);", re.MULTILINE)

    new_content = pattern.sub(new_script + "\n", content)
    new_content = pattern_basic.sub(new_script + "\n", new_content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}")

for filename in glob.glob('*.html'):
    process_file(filename)
