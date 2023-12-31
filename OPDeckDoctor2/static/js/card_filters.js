$(document).ready(function () {
  
  function applyFilters() {
    const colorFilters = $("input[data-filter='color']:checked").map(function () {
      return $(this).val();
    }).get();

    const typeFilters = $("input[data-filter='type']:checked").map(function () {
      return $(this).val();
    }).get();

    const counterFilters = $("input[data-filter='counter']:checked").map(function () {
      return $(this).val();
    }).get();

		const counter2kFilters = $("input[data-filter='counter2k']:checked").map(function () {
      return $(this).val();
    }).get();

    const triggerFilters = $("input[data-filter='trigger']:checked").map(function () {
      return $(this).val();
    }).get();

    const blockerFilters = $("input[data-filter='blocker']:checked").map(function () {
      return $(this).val();
    }).get();

    const cardNameFilter = $("#cardSearch").val().toLowerCase();

    $(".grid-item").each(function () {
      const $card = $(this);
      const cardColor = $card.data("color");
      const cardType = $card.data("type");
      const cardCounter = $card.data("counter");
			const cardCounter2k = $card.data("counter2k");
      const cardTrigger = $card.data("trigger");
      const cardBlocker = $card.data("blocker");
      const cardName = $card.find(".cardName").text().toLowerCase();

      const colorMatch = colorFilters.length === 0 || colorFilters.includes(cardColor);
      const typeMatch = typeFilters.length === 0 || typeFilters.includes(cardType);
      const counterMatch = counterFilters.length === 0 || counterFilters.includes(cardCounter);
			const counter2kMatch = counter2kFilters.length === 0 || counter2kFilters.includes(cardCounter2k);
      const triggerMatch = triggerFilters.length === 0 || triggerFilters.includes(cardTrigger);
      const blockerMatch = blockerFilters.length === 0 || blockerFilters.includes(cardBlocker);
      const nameMatch = cardName.includes(cardNameFilter);

      const shouldShow = colorMatch && typeMatch && counterMatch && triggerMatch && blockerMatch && nameMatch && counter2kMatch;
      $card.toggle(shouldShow);
    });
  }

  // Initial filter
  applyFilters();

  // Checkbox change event
  $("input[type='checkbox'], #cardSearch").on("change input", applyFilters);

// List visibility toggling on click
const cards = document.querySelectorAll('.card');

cards.forEach(function(card) {
  const toggleBtn = card.querySelector('.card-header');
  const listGroup = card.querySelector('.list-group');

  toggleBtn.addEventListener('click', function(event) {
    event.stopPropagation(); 
    
    document.querySelectorAll('.list-group.visible').forEach(function(group) {
      if (group !== listGroup) {
        group.classList.remove('visible');
      }
    });
    listGroup.classList.toggle('visible');
  });
});

document.addEventListener('click', function(event) {
  cards.forEach(function(card) {
    const listGroup = card.querySelector('.list-group');

    if (!card.contains(event.target)) {
      listGroup.classList.remove('visible');
    }
  });
});

});

