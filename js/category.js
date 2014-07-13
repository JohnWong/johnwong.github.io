$(document).ready(function() {
    var params = function() {
        for (var t, e = [], o = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&"), r = 0; r < o.length; r++)
            t = o[r].split("="), e.push(t[0]), e[t[0]] = t[1];
        return e;
    }();
    var cat = params['cat'];
    if (!cat) {
        // $(".post-big-title").html('未找到该文章');
        return;
    };
    cat = decodeURI(cat);
});