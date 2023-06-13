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
