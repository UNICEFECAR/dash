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

    var intro = introJs('body');
    $(document).on('click', '#btnInfo', function () {
        intro.setOptions({
            steps: [{
                title: "Welcome!",
                intro: "Welcome to the Transmonee Dashboard!"
            }, {
                title: "Header",
                element: document.querySelector('.header__top'),
                intro: "This is the header of the dashboard!",
                position: 'left'
            },
            {
                title: "Navigation",
                element: document.querySelector('.header__navigation'),
                intro: "This is the navigation of the dashboard!",
                position: 'top'
            },
            {
                title: "Page Title",
                element: document.querySelector('.heading-title'),
                intro: "This is the Title of the page!",
                position: 'top'
            },
            {
                title: "Home Body",
                element: document.querySelector('#home-image'),
                intro: "This is the Image of the home page!",
                position: 'right'
            }]
        });
        intro.start();
        return false;
    });
});