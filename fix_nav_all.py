import glob
import re

advanced_fetch = """fetch('navbar.html')
      .then(response => response.text())
      .then(data => {
          document.getElementById('navbar').innerHTML = data;
          
          // Initialize navbar menu and dropdowns after injection
          const toggle = document.getElementById('nav-toggle');
          const nav = document.getElementById('nav-menu');
          if(toggle && nav) {
             toggle.addEventListener('click', () =>{
                nav.classList.toggle('show-menu');
                toggle.classList.toggle('show-icon');
             });
          }
          
          const dropdownItems = document.querySelectorAll('.dropdown__item');
          dropdownItems.forEach((item) =>{
              const dropdownButton = item.querySelector('.dropdown__button'); 
              if(dropdownButton) {
                  dropdownButton.addEventListener('click', () =>{
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
                  });
              }
          });
      });"""

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if "// Initialize navbar menu and dropdowns after injection" in content:
        print(f"Skipping {filename} (already updated)")
        return
        
    # Find any fetch('navbar.html') block and replace it
    pattern = re.compile(r"fetch\('navbar\.html'\)[\s\S]*?\.innerHTML\s*=\s*[a-zA-Z]+;\s*\}\);", re.MULTILINE)

    new_content = pattern.sub(advanced_fetch, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}, looking for other variants...")

for filename in glob.glob('*.html'):
    if filename not in ['navbar.html', 'footer.html']:
        process_file(filename)
