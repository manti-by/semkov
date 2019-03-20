(($) => {

    'use strict';

    /*
     * Contact form
     */

    $.initAjaxForms = () => {
        $('form.ajax').on('submit', (e) => {
            e.preventDefault();

            let form = $(e.currentTarget),
                data = {};

            $.each(form.find('.form-control'), (i, input) => {
                data[input.name] = input.value;
            });

            $.post(form.attr('action'), data, (response) => {
                alert(response['message']);
            });
        });
    };

})(jQuery);