(($) => {

    'use strict';

    /*
     * Contact form
     */

    $.initContact = () => {
        $('#send').on('click', () => {
            let data = {
                'name': $('#name').val(),
                'contact': $('#contact').val(),
                'message': $('#message').val(),
            };

            $.post('/api/contact', data, (response) => {
                $('#contactModal').modal('hide');
                alert(response['message']);
            });
        });
    };

})(jQuery);