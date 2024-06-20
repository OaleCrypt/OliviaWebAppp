/**
* Updated: Mar 17 2024 with Bootstrap v5.3.3
*/

(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  }

  /**
   * Easy event listener function with passive option
   */
  const on = (type, el, listener, all = false, passive = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener, { passive }));
      } else {
        selectEl.addEventListener(type, listener, { passive });
      }
    }
  }

  /**
   * Easy on scroll event listener with passive option
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener, { passive: true });
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active');
      } else {
        navbarlink.classList.remove('active');
      }
    });
  }
  window.addEventListener('load', navbarlinksActive);
  onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos,
      behavior: 'smooth'
    });
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top');
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active');
      } else {
        backtotop.classList.remove('active');
      }
    }
    window.addEventListener('load', toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('body').classList.toggle('mobile-nav-active');
    this.classList.toggle('bi-list');
    this.classList.toggle('bi-x');
  });

  /**
   * Scroll with offset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault();

      let body = select('body');
      if (body.classList.contains('mobile-nav-active')) {
        body.classList.remove('mobile-nav-active');
        let navbarToggle = select('.mobile-nav-toggle');
        navbarToggle.classList.toggle('bi-list');
        navbarToggle.classList.toggle('bi-x');
      }
      scrollto(this.hash);
    }
  }, true);

  /**
   * Scroll with offset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }

    // Scroll to contact form's hidden anchor if URL hash is #form-submission
    if (window.location.hash === '#form-submission') {
      document.getElementById('form-submission').scrollIntoView({ behavior: 'smooth' });
    }
  });

  /**
   * Hero type effect
   */
  const typed = select('.typed');
  if (typed) {
    let typed_strings = typed.getAttribute('data-typed-items');
    typed_strings = typed_strings.split(',');
    new Typed('.typed', {
      strings: typed_strings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 50,
      backDelay: 2000
    });
  }

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    })
  }

  /**
   * Portfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh();
        });
      }, true);
    }
  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

  /**
   * Handle AJAX form submission for the contact form
   */
  document.addEventListener("DOMContentLoaded", function() {
    const contactForm = document.querySelector(".contact-form");

    if (contactForm) {
      contactForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const formData = new FormData(contactForm);
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

        // Send form data via AJAX
        fetch(contactForm.action, {
          method: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
            "X-Requested-With": "XMLHttpRequest", // Signal the server that this is an AJAX request
            "Accept": "application/json" // Request a JSON response
          },
          body: formData
        })
        .then(response => {
          console.log('Response status:', response.status); // Log the response status
          console.log('Response headers:', response.headers.get('Content-Type')); // Log content type

          // Check if the response is JSON
          const contentType = response.headers.get('Content-Type');
          if (contentType && contentType.includes('application/json')) {
            return response.json(); // Parse the response as JSON
          } else {
            return response.text(); // Parse the response as text (for debugging HTML responses)
          }
        })
        .then(data => {
          if (typeof data === 'object') {
            // Handle JSON response
            console.log('Response received:', data); // Debugging: Log the response
            const formHeader = contactForm.querySelector(".here .alert");
            if (formHeader) {
              if (data.success) {
                // Display the success message
                formHeader.textContent = data.message || "Your message has been sent!";
                formHeader.classList.add("alert-success");
                formHeader.classList.remove("d-none");

                // Scroll to the form
                document.getElementById('form-submission').scrollIntoView({ behavior: 'smooth' });

                // Reset the form inputs
                contactForm.reset();
              } else {
                // Handle form submission errors
                console.error("Form submission failed", data.errors);
                // Display error messages if needed
                formHeader.textContent = data.error || "There was an error with your submission.";
                formHeader.classList.add("alert-danger");
                formHeader.classList.remove("d-none");
              }
            } else {
              console.error("Error: Cannot find the alert message container in the form.");
            }
          } else {
            // Handle non-JSON response (likely HTML for debugging)
            console.error("Response was not JSON. Received:", data);
            console.log('HTML Response:', data); // Log the HTML response for debugging
          }
        })
        .catch(error => {
          console.error("Error:", error); // Debugging: Log the error
          console.log('Response was not JSON. Check server response for errors or non-JSON output.');
        });
      });
    }
  });

})();

