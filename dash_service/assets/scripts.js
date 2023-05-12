jQuery(".theme").click(function () {
    jQuery(".theme").removeClass("active");
    jQuery(this).addClass("active");
});

jQuery(document).ready(function () {
    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 300) {
            jQuery('.scroll-top').fadeIn();
        } else {
            jQuery('.scroll-top').fadeOut();
        }
    });
    jQuery(document).on('click', '#btnScroll', function () {
        jQuery("html, body").animate({
            scrollTop: 0
        }, 300);
        return false;
    });
});