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
    }
    cat = decodeURI(cat);
    var articles;
    $(".category-header-title").html(cat);
    $.get("data/list.json", function(data) {
        articles = data[cat];
        if (articles) {
            var monthly = 0,
                total = 0;
            var current_date = new Date();
            for (var i in articles) {
                var article = articles[i];
                total++;
                var article_date = new Date(article['time']);
                if (current_date - article_date <= 1000 * 60 * 60 * 24 * 31) {
                    monthly++;
                }
            }
            $(".total span").html(total);
            $(".month span").html(monthly);
            goPage(1);
        }
    });
    var pageSize = 4;

    function goPage(num) {
        var start = (num - 1) * pageSize;
        var to = num * pageSize;
        var template = $("#article-template").html();
        var content = '';
        var sub_articles = articles.slice(start, to);
        for (var i in sub_articles) {
            var article = sub_articles[i];
            content += template.replace("@{article-author}", article.author)
                .replace("@{article-time}", article.time)
                .replace("@{article-link}", "link") //todo
                .replace("@{article-title}", article.title)
                .replace("@{article-description}", article.description)
                .replace("@{article-cover}", article.cover_url);
        }
        $(".articles").html(content);
    }
});