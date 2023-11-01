$(document).ready(function () {
  // Function to apply filters
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

		const costFilters = $("input[data-filter='cost']:checked").map(function () {
      return $(this).val();
    }).get();

		const rarityFilters = $("input[data-filter='rarity']:checked").map(function () {
      return $(this).val();
    }).get();

		const setFilters = $("input[data-filter='set']:checked").map(function () {
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
			const cardCost = $card.data("cost");
			const cardRarity = $card.data("rarity");
			const cardSet = $card.data("set");
      const cardName = $card.find(".cardName").text().toLowerCase();

      const colorMatch = colorFilters.length === 0 || colorFilters.includes(cardColor);
      const typeMatch = typeFilters.length === 0 || typeFilters.includes(cardType);
      const counterMatch = counterFilters.length === 0 || counterFilters.includes(cardCounter);
			const counter2kMatch = counter2kFilters.length === 0 || counter2kFilters.includes(cardCounter2k);
      const triggerMatch = triggerFilters.length === 0 || triggerFilters.includes(cardTrigger);
      const blockerMatch = blockerFilters.length === 0 || blockerFilters.includes(cardBlocker);
			const costMatch = costFilters.length === 0 || costFilters.includes(cardCost.toString());
			const rarityMatch = rarityFilters.length === 0 || rarityFilters.includes(cardRarity);
			const setMatch = setFilters.length === 0 || setFilters.includes(cardSet);
      const nameMatch = cardName.includes(cardNameFilter);

      const shouldShow = colorMatch && typeMatch && counterMatch && triggerMatch && blockerMatch && nameMatch && counter2kMatch && costMatch && rarityMatch && setMatch;
      $card.toggle(shouldShow);
    });
  }

  var numberbox = document.querySelector('.collection-hiding-checkbox');
  var numberOwnedInputs = document.querySelectorAll('.number-owned');
  numberbox.addEventListener('change', function() {
    var displayValue = numberbox.checked ? 'none' : 'block';
    numberOwnedInputs.forEach(function(input) {
      input.style.display = displayValue;
    });
  });
  
  var namebox = document.querySelector('.names-hiding-checkbox');
  var cardNameElements = document.querySelectorAll('.cardName');
  namebox.addEventListener('change', function() {
    var displayValue = namebox.checked ? 'none' : 'block';
    cardNameElements.forEach(function(cardName) {
      cardName.style.display = displayValue;
    });
  });

  // Initial filter
  applyFilters();

  // Checkbox change event
  $("input[type='checkbox'], #cardSearch").on("change input", applyFilters);
});