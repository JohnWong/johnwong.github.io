$(document).on("scroll", function() {
    $(this).scrollTop() > 25 ? $("#top").addClass("scrolled") : $("#top").removeClass("scrolled");
});