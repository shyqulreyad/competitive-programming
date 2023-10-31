//card deck 
cardDeck = ({
   suits: ['♠', '♥', '♦', '♣'],
   court: ['J', 'Q', 'K', 'A'],
   [Symbol.iterator]: function* () {
      for (const suit of this.suits) {
        for (let i = 2; i<=10;i++) yield suit + i;
         for (let c of this.court) yield suit + c;
      }
   }
})
console.log([...cardDeck]);
return cardDeck;



// generator function

function* generator() {
  yield 1;
  yield 2;
  yield 3;
}

// var gen = generator();
// console.log(gen.next().value); // 1
// console.log(gen.next().value); // 2
// console.log(gen.next().value); // 3

return false;


// to get all the check box value
$('.checkboxclass:checked').each(function() {
    if ($(this).is(':checked')) {
        var checked = ($(this).val());
        session_id.push(checked);
    }
})

// to mark all check box
$(document).on('click', '.check_all', function() {
    if ($(this).prop('checked') == true) {
        $('.data_checkbox').each(function() {
            if ($(this).prop('disabled')) {
                $(this).prop('checked', false);
            } else {
                $(this).prop('checked', true);
            }

        })
    }


    if ($(this).prop('checked') == false) {
        $('.data_checkbox').each(function() {
            if ($(this).prop('disabled')) {
                $(this).prop('checked', false);
            } else {
                $(this).prop('checked', false);
            }
        })
    }

});

// remove element from dom
if ($(this).is(':checked')) {
    var closestfield = $(this).closest('tr');
    closestfield.remove();
}






// checking if input field name unique or not
const inputFields = document.querySelectorAll('#session_form input');
const inputNames = [];
let isUnique = true;

// Loop through all input elements and store their names in the array
inputFields.forEach((input) => {
  const name = input.getAttribute('name');
  console.log(name)
  if (!name || name.trim() === '') {
    console.error('Input field without name found!');
    isUnique = false;
  } else {
    if (inputNames.includes(name)) {
      console.error(`Input field name "${name}" is not unique!`);
      isUnique = false;
    } else {
      inputNames.push(name);
    }
  }
});

if (isUnique) {
  console.log('All input field names are unique and have valid names test.');
}else{
  console.log('not unique')
}


//observer for dom change
const observer = new MutationObserver(function(mutationsList, observer) {
  for (const mutation of mutationsList) {
      if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
      for (const addedNode of mutation.addedNodes) {
          if (addedNode.nodeType === Node.ELEMENT_NODE) {
              $('.fr-wrapper').find('a').remove();
              $('.fr-second-toolbar').find('a').remove();
          }
      }
      }
  }
});
const config = { childList: true, subtree: true };
observer.observe(document.body, config);




