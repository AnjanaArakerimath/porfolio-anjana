import os
import re

new_footer = """<footer class="py-5" style="background-color: #101b38; color: white; border-top: 2px solid #c2c1ff;">
      <div class="container">
        <div class="row align-items-center">
          
          <!-- Contact Info Column -->
          <div class="col-md-6 mb-4 mb-md-0 text-center text-md-start">
            <h5 style="color: #c2c1ff; font-weight: 600; margin-bottom: 1rem;">Contact Details</h5>
            <p class="mb-2" style="color: #d9d9eb;"><i class="fa-solid fa-envelope me-2"></i> a.anjana@pccoepune.org</p>
            <p class="mb-0" style="color: #d9d9eb;"><i class="fa-solid fa-location-dot me-2"></i> Pimpri Chinchwad College of Engineering, Pune</p>
          </div>

          <!-- Social Icons Column -->
          <div class="col-md-6 text-center text-md-end">
           
            <div class="effect varrius" style="background-color: transparent;">
              <!-- Used flex-wrap and gap to keep buttons consistent and responsive -->
              <div class="buttons d-flex justify-content-center justify-content-md-end flex-wrap gap-2" style="margin: 0; padding: 0;">
                <a href="https://www.instagram.com/arakerimathanjana?igsh=MXA4d2plMG4xY3Y5cw==" class="insta" title="Join us on Instagram" style="border-color: #fff; margin: 0;"><i class="fab fa-instagram" aria-hidden="true"></i></a>
                <a href="https://www.linkedin.com/in/anjana-arakerimath-47a606147/" class="in" title="Join us on Linked In" style="border-color: #fff; margin: 0;"><i class="fab fa-linkedin" aria-hidden="true"></i></a>
                <a href="https://scholar.google.co.in/citations?user=Sgd9lfcAAAAJ&hl=en" class="g-plus" title=" google scholor" style="border-color: #fff; margin: 0;">      
                  <img src="image/google_scholor_logo.png" width="30px" height="30px" style="border-radius: 50%;">
                </a>
                <a href="mailto:a.anjana@pccoepune.org" class="fb" title="G-MAIL" style="border-color: #fff; margin: 0;">
                  <i class="fa fa-envelope-open-text"></i>
                </a>
                <a href="resume/Anjana Resume 250624 updated.docx" download="Anjana Arakerimath Resume" title="download resume" style="border-color: #fff; margin: 0;">
                  <i class="fa fa-download"></i>
                </a>
              </div>
            </div>
            <!-- Copyright placed directly under icons -->
            <div class="copyright mt-3" style="color: #d9d9eb; font-size: 0.9rem;">&copy; Anjana Arakerimath. All Rights Reserved</div>
          </div>

        </div>
      </div>
    </footer>"""

for file in os.listdir('.'):
    if file.endswith('.html') and file != 'navbar.html':
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the footer block
        updated_content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)
        
        if updated_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated footer in {file}")

print("Done updating footers to grid layout.")
