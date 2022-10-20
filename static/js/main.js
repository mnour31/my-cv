$(function () {
    $(".progress div").each(function() {

        $(this).animate({
            'width': $(this).data("width")
        }, 1000);

    });
})



