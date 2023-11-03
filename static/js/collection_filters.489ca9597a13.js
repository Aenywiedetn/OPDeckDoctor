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

		const costFilters = $("input[data-filter='cost']:checked").map(function () {
      return $(this).val();
    }).get();

		const rarityFilters = $("input[data-filter='rarity']:checked").map(function () {
      return $(this).val();
    }).get();

		const setFilters = $("input[data-filter='set']:checked").map(function () {
      return $(this).val();
    }).get();

    const collectionFilters = $("input[data-filter='collection']:checked").map(function () {
      return $(this).val();
    }).get();
    $("input[data-filter='collection']").on("change", function () {
      // Uncheck all checkboxes within the same group except the current one
      $("input[data-filter='collection']").not(this).prop("checked", false);
    });
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
      const numberOwned = parseInt($card.find(".number-owned").val());
        let collectionMatch = true;

        if (collectionFilters.includes("owned") && numberOwned !== 4) {
          collectionMatch = false;
        }
        if (collectionFilters.includes("missing") && (numberOwned < 1 || numberOwned > 3)) {
          collectionMatch = false;
        }
        if (collectionFilters.includes("notowned") && numberOwned > 0) {
          collectionMatch = false;
        }

      const shouldShow = colorMatch && typeMatch && counterMatch && triggerMatch && blockerMatch && nameMatch && counter2kMatch && costMatch && rarityMatch && setMatch &&collectionMatch;
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
$('.resetBTN').on('click', function () {
        // Uncheck all checkboxes
        $('.filter-checkbox').prop('checked', false);

        // Trigger a change event on the checkboxes to apply filters
        $('.filter-checkbox').change();
    });

  $(document).ready(function () {
  $('.number-owned').change(function () {
    var cardId = $(this).data('card-id');
    var numberOwned = $(this).val();

    $.ajax({
    type: 'POST',
    url: '/collector/update_user_input/' + cardId + '/',
    data: {
        csrfmiddlewaretoken: csrfToken,
        number_owned: numberOwned
    },
    beforeSend: function (xhr) {
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    },
    success: function (data) {
        if (data.success) {
          var cardId = data.card_id;  // You need to send card_id in the AJAX response
        var newNumberOwned = data.new_number_owned;
        var numberOwnedInput = $('.number-owned[data-card-id="' + cardId + '"]');
        numberOwnedInput.val(newNumberOwned);
        } else {
            // Handle failure (e.g., show error message)
        }
    },
    error: function () {
        // Handle AJAX error
    }
});

   
  });
});

});