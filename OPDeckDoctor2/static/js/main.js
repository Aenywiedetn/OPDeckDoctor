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
  
  const zoomElementsWithTooltip = document.querySelectorAll('.for_zoom_with_tooltip');
  const zoomElementsWithoutTooltip = document.querySelectorAll('.for_zoom');
  
  let currentZoomedElement = null;

  function toggleZoomedState(element, isWithTooltip) {
    // Check if there's a currently zoomed element
    if (currentZoomedElement === element) {
      // If yes, toggle off the zoomed class and tooltip-zoomed class
      element.classList.remove(isWithTooltip ? 'zoomed_with_tooltip' : 'zoomed');
      const tooltip = element.parentElement.querySelector('.tooltip-content');
      if (tooltip) {
        tooltip.classList.remove('tooltip-zoomed');
      }
      // Reset the currently zoomed element
      currentZoomedElement = null;
    } else {
      // If no, toggle the zoomed class on the clicked element
      // and toggle the tooltip class as well
      if (currentZoomedElement) {
        currentZoomedElement.classList.remove(isWithTooltip ? 'zoomed_with_tooltip' : 'zoomed');
        const currentTooltip = currentZoomedElement.parentElement.querySelector('.tooltip-content');
        if (currentTooltip) {
          currentTooltip.classList.remove('tooltip-zoomed');
        }
      }

      element.classList.add(isWithTooltip ? 'zoomed_with_tooltip' : 'zoomed');
      const tooltip = element.parentElement.querySelector('.tooltip-content');
      if (tooltip) {
        tooltip.classList.add('tooltip-zoomed');
      }

      // Update the currently zoomed element
      currentZoomedElement = element;
    }
  }

  zoomElementsWithTooltip.forEach(function(element) {
    element.addEventListener('click', function(event) {
      toggleZoomedState(this, true);
      // Prevent the click event from propagating to the document
      event.stopPropagation();
    });
  });

  zoomElementsWithoutTooltip.forEach(function(element) {
    element.addEventListener('click', function(event) {
      toggleZoomedState(this, false);
      // Prevent the click event from propagating to the document
      event.stopPropagation();
    });
  });

  document.addEventListener('click', function() {
    // Remove 'zoomed' class from all zoomed elements
    zoomElementsWithTooltip.forEach(function(element) {
      element.classList.remove('zoomed_with_tooltip');
      // Remove 'tooltip-zoomed' class as well
      const tooltip = element.parentElement.querySelector('.tooltip-content');
      if (tooltip) {
        tooltip.classList.remove('tooltip-zoomed');
      }
    });

    zoomElementsWithoutTooltip.forEach(function(element) {
      element.classList.remove('zoomed');
    });

    // Reset the currently zoomed element
    currentZoomedElement = null;
  });
});