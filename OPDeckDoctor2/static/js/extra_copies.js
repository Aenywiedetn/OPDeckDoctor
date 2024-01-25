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
      
      
      
      
      const shouldShow = colorMatch && typeMatch && counterMatch && triggerMatch && blockerMatch && nameMatch && counter2kMatch && costMatch && rarityMatch && setMatch ;
      $card.toggle(shouldShow);
      



    });
  }
  
  $(document).ready(function () {
    // Select the label element
    var labelElement = document.getElementById('extra_card_list');

    // Add a click event listener to the label
    labelElement.addEventListener('click', function () {
      // Create a range and select the text content
      var range = document.createRange();
      range.selectNode(labelElement);

      // Create a selection and add the range to it
      var selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);

      try {
        // Copy the selected text to the clipboard
        document.execCommand('copy');
        // Provide feedback to the user upon successful copy
        alert('Copied to clipboard!');
      } catch (err) {
        // Handle any errors during the copying process
        console.error('Unable to copy to clipboard', err);
      }

      // Clear the selection
      selection.removeAllRanges();
    });
  });
  
  
  
  applyFilters();

  
  $("input[type='checkbox'], #cardSearch").on("change input", applyFilters);
$('.resetBTN').on('click', function () {
        
        $('.filter-checkbox').prop('checked', false);
        $('.filter-checkbox').change();
    });
$(document).ready(function () {
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

 



  
  
      
   
});

   
 
