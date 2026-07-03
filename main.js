document.addEventListener('DOMContentLoaded', () => {
  // 1. Header scroll effect
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }
    });
  }

  // 2. Mobile navigation menu toggle
  const mobileToggle = document.querySelector('.mobile-nav-toggle');
  const nav = document.querySelector('.nav');
  if (mobileToggle && nav) {
    mobileToggle.addEventListener('click', () => {
      nav.classList.toggle('nav-active');
      mobileToggle.classList.toggle('open');
    });
  }

  // Close mobile nav when clicking outside or on a link
  document.addEventListener('click', (e) => {
    if (nav && nav.classList.contains('nav-active') && !nav.contains(e.target) && !mobileToggle.contains(e.target)) {
      nav.classList.remove('nav-active');
      mobileToggle.classList.remove('open');
    }
  });

  // 3. Highlight active nav link based on current path
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-link');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href) {
      const linkPath = new URL(href, window.location.origin).pathname;
      if (currentPath === linkPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
        link.classList.add('active');
        // If it's a dropdown link, also highlight its parent link
        const parentDropdown = link.closest('.nav-item-dropdown');
        if (parentDropdown) {
          const parentLink = parentDropdown.querySelector('.nav-link');
          if (parentLink) parentLink.classList.add('active');
        }
      }
    }
  });

  // 4. Contact Form Submission handler
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending...';

      // Simulate sending
      setTimeout(() => {
        // Show success alert
        alert('Thank you for contacting Ash & Sims Advertising LLC. We have received your inquiry and will get back to you shortly.');
        contactForm.reset();
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }, 1500);
    });
  }
});
