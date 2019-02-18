(($) => {

    'use strict';

    /*
     * Floating header
     */
    let $window = $(window),
        $header = $('header');

    $.check = () => {
        $window.scrollTop() > 60 ?
            $header.addClass('active') : $header.removeClass('active');
    };

    $.initHeader = () => {
        $.check();
        $window.scroll($.check);
    };

})(jQuery);