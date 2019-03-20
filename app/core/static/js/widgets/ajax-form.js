(($) => {

    'use strict';

    /*
     * Contact form
     */

    $.initAjaxForms = () => {
        $('form.ajax').on('submit', (e, callback) => {
            e.preventDefault();

            let form = $(e.currentTarget),
                data = {};

            $.each(form.find('.form-control'), (i, input) => {
                data[input.name] = input.value;
            });

            $.post(form.attr('action'), data, (response) => {
                if (callback !== undefined) {
                    callback(response);
                } else {
                    alert(response['message']);
                }
            });
        });
    };

})(jQuery);