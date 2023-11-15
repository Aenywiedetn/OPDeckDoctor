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
      $("input[data-filter='collection']").not(this).prop("checked", false);
    });

    const noteFilters = $("input[data-filter='note']:checked").map(function () {
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
      const placeholderValue = '  ?'
      const numberOwned = $card.find(".number-owned").val();
      const noteAdded = $card.find(".short_note").val();
      console.log("noteAdded:", noteAdded);
  

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
      const noteMatch = noteFilters.length === 0 || (noteFilters.includes('noteadded') && noteAdded !== '');
      console.log("noteFilters:", noteFilters);
      console.log("noteMatch:", noteMatch);
      let collectionMatch = true;

        if (collectionFilters.includes("owned") && (numberOwned === placeholderValue || numberOwned < 4)) {
          collectionMatch = false;
        }
      
        if (collectionFilters.includes("missing") && numberOwned > 3) {
          collectionMatch = false;
        }
        if (collectionFilters.includes("more") && (numberOwned === placeholderValue || numberOwned < 5)) {
          collectionMatch = false;
        }
      
      const shouldShow = colorMatch && typeMatch && counterMatch && triggerMatch && blockerMatch && nameMatch && counter2kMatch && costMatch && rarityMatch && setMatch &&collectionMatch &&noteMatch;
      $card.toggle(shouldShow);
      console.log(`Card ID: ${$card.data("card-id")}, noteAdded: "${noteAdded}", noteMatch: ${noteMatch}, noteFilters: ${JSON.stringify(noteFilters)}`);



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
  var labelText = document.querySelector('.label-text');
  var cardNameElements = document.querySelectorAll('.cardName');
  var cardNoteElements = document.querySelectorAll('.short_note');
  namebox.addEventListener('change', function() {
    var displayValue = namebox.checked ? 'none' : 'block';
    labelText.textContent = (namebox.checked ? '\u00A0\u00A0\u00A0 Show Names' : '\u00A0\u00A0\u00A0 Show Notes');
    cardNameElements.forEach(function(cardName) {
      cardName.style.display = displayValue;
    });
    cardNoteElements.forEach(function(cardNote) {
      cardNote.style.display = namebox.checked ? 'block' : 'none';
    });
  });

  // Initial filter
  applyFilters();

  // Checkbox change event
  $("input[type='checkbox'], #cardSearch").on("change input", applyFilters);
$('.resetBTN').on('click', function () {
        
        $('.filter-checkbox').prop('checked', false);
        $('.filter-checkbox').change();
    });

const cardElements = document.querySelectorAll('.for_zoom');

  cardElements.forEach(cardElement => {
    cardElement.addEventListener('click', function() {
      if (cardElement.classList.contains('for_zoom')) {
        cardElement.classList.remove('for_zoom');
      } else {
        cardElement.classList.add('for_zoom');
      }
    });
  });

  $(document).ready(function () {
    $('.number-owned').change(function () {
      var cardId = $(this).data('card-id');
      var numberOwned = $(this).val();
  
      $.ajax({
        type: 'POST',
        url: '/collector/update_number_owned/' + cardId + '/',
        data: {
          csrfmiddlewaretoken: csrfToken,
          number_owned: numberOwned
        },
        beforeSend: function (xhr) {
          xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        },
        success: function (data) {
          if (data.success) {
            var cardId = data.card_id;
            var newNumberOwned = data.new_number_owned;
            var numberOwnedInput = $('.number-owned[data-card-id="' + cardId + '"]');
            numberOwnedInput.val(newNumberOwned);
          } else {
            alert('Error: Unable to update the number owned.');
          }
        },
        error: function (xhr, status, error) {
          console.error("AJAX request failed:", status, error);
        }
      });
    });
    
    $('.short_note').change(function () {
      var cardId = $(this).data('card-id');
      var shortNote = $(this).val();
  
      $.ajax({
        type: 'POST',
        url: '/collector/update_short_note/' + cardId + '/',
        data: {
          csrfmiddlewaretoken: csrfToken,
          short_note: shortNote
        },
        beforeSend: function (xhr) {
          xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        },
        success: function (data) {
          if (data.success) {
            var cardId = data.card_id;
            var newShortNote = data.new_short_note;
            var shortNoteInput = $('.short-note[data-card-id="' + cardId + '"]');
            shortNoteInput.val(newShortNote);
            console.log("AJAX success. Data received:", data);
          } else {
            alert('Error: Unable to update the note.');
            console.error("AJAX request failed:", error);
          }
        },
        error: function (xhr, status, error) {
          console.error("AJAX request failed:", status, error);
        }
      });
    });


      

  });

   
  });
