document.addEventListener("DOMContentLoaded", function() {
    
    let lazyImages = document.querySelectorAll('img[loading="lazy"]');
  
    let observer = new IntersectionObserver(function(entries, observer) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          lazyImage.removeAttribute('data-src');
          lazyImage.removeAttribute('loading');
          observer.unobserve(lazyImage);
        }
      });
    });
  
    lazyImages.forEach(image => {
      observer.observe(image);
    });
  
   
    const zoomElements = document.querySelectorAll('.for_zoom');
  
    zoomElements.forEach(function(element) {
      element.addEventListener('click', function() {
        this.classList.toggle('zoomed');
      });
    });
  });