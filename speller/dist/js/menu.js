(function () {
    $('#testee li').bind('click', function (e) {
        var el = $(this),
            list = $('#testee').find('li');
        list.removeClass('active_item');
        el.addClass('active_item');
    });
}());