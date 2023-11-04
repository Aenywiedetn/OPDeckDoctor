$(document).ready(function () {
  
  function applyFilters() {
    const colorFilters = $("input[data-filter='color']:checked").map(function () {
      return $(this).val();
    }).get();

    const setFilters = $("input[data-filter='set']:checked").map(function () {
      return $(this).val();
    }).get();

    const cardNameFilter = $("#cardSearch").val().toLowerCase();

    $(".grid-item").each(function () {
      const $card = $(this);
      const cardColor1 = $card.data("color1");
      const cardColor2 = $card.data("color2");
      const cardSet = $card.data("set");
      const cardName = $card.find(".leaderName").text().toLowerCase();

      const colorMatch = colorFilters.length === 0 || colorFilters.includes(cardColor1) || colorFilters.includes(cardColor2);
      const setMatch = setFilters.length === 0 || setFilters.includes(cardSet);
      const nameMatch = cardName.includes(cardNameFilter);

      const shouldShow = colorMatch && nameMatch && setMatch;
      $card.toggle(shouldShow);
    });
  }

  // Initial filter
  applyFilters();

  // Checkbox change event
  $("input[type='checkbox'], #cardSearch").on("change input", applyFilters);

  $('.resetBTN').on('click', function () {
    // Uncheck all checkboxes
    $('.filter-checkbox').prop('checked', false);

    // Trigger a change event on the checkboxes to apply filters
    $('.filter-checkbox').change();
});

});

