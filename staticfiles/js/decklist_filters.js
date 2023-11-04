$(document).ready(function () {
  
  function applyFilters() {
    const formatFilters = $("input[data-filter='format']:checked").map(function () {
      return $(this).val();
    }).get();
    $("input[data-filter='format']").on("change", function () {
      $("input[data-filter='format']").not(this).prop("checked", false);
    });

    $(".decklist").each(function () {
      const $decklist = $(this);
      const decklistFormat = $decklist.data("format");
     
      const formatMatch = formatFilters.length === 0 || formatFilters.includes(decklistFormat);
      

      const shouldShow = formatMatch;
      $decklist.toggle(shouldShow);
    });
  }

  // Initial filter
  applyFilters();

  // Checkbox change event
  $("input[type='checkbox']").on("change input", applyFilters);

 
});



