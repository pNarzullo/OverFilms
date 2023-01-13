var accordion = function () {
    var data = $(".accordion").attr("data_accordion");

    $(".accordion_header").on("click", function() {
        if (data = "close") {
            $(".accordion_body").slideUp();
            if ($(this).hasClass("active")){
                $(this).toggleClass("active");
            }
            else{
                $(".accordion_header").removeClass("active");
                $(this).toggleClass("active");
            }
        }
        else {
            $(this).toggleClass("active");
        }
        $(this).next(".accordion_body").not(":animated").slideToggle();
    });
}

accordion();

$(document).ready(function() {
    $('.burger_bg').click(function(event) {
        $('.burger,.nav').toggleClass('active');
        $('body').toggleClass('lock');
    })
})