var params = function() {
    for (var t, e = [], o = window.location.search.slice(window.location.search.indexOf("?") + 1).split("&"), r = 0; r < o.length; r++)
        t = o[r].split("="), e.push(t[0]), e[t[0]] = t[1];
    return e;
}();

$(document).on("scroll", function() {
    $(this).scrollTop() > 25 ? $("#top").addClass("scrolled") : $("#top").removeClass("scrolled");
});

function iconFromCategory(cat) {
    switch (cat) {
        case "Mobile":
            return 'glyphicon-phone';
        case "Life":
            return 'glyphicon-home';
            // case "Bookmarks": icon = 'glyphicon-bookmark'; break;
        case "Travel":
            return 'glyphicon-road';
            // case "White Hat": icon = 'glyphicon-lock';break;
        case "Front End":
            return 'glyphicon-link';
    }
}

function colorFromCategory(cat){
    var icon;
    switch (cat) {
        case "Mobile":
            return '#62bb47';
        case "Life":
            return '#fbb726';
        case "Travel":
            return '#e03a3e';
        case "Front End":
            return '#943b95';
    }
    return icon;
}