$(".theme").click(function () {
    $(".theme").removeClass("active");
    $(this).addClass("active");
});

$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.scroll-top').fadeIn();
        } else {
            $('.scroll-top').fadeOut();
        }
    });
    $(document).on('click', '#btnScroll', function () {
        $("html, body").animate({
            scrollTop: 0
        }, 300);
        return false;
    });
});