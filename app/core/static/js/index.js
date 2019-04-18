(($) => {

    'use strict';

    $(document).ready(() => {
        $.initHeader();

        $.initAjaxForms();

        $('#contact-button').on('click', () => {
            $('#contact-form').trigger('submit', (response) => {
                $('#contact-modal').modal('hide');
                alert(response['message']);
            });
        });

        $('#login-button').on('click', () => {
            $('#login-form').trigger('submit', (response) => {
                $('#login-modal').modal('hide');
                $('.login-alert').remove();
                $('.login-button').addClass('d-none');
                alert(response['message']);
            });
        });
    });

})(jQuery);