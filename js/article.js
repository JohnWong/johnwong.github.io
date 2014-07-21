$(document).ready(function() {
    var cat = params['cat'], id = params['id'];
    if (!cat || !id) {
        $(".post-big-title").html('未找到该文章');
        return;
    }
    id = decodeURI(id), cat = decodeURI(cat);
    var sep_index = cat.indexOf('/'), subcat;
    if (sep_index >= 0) {
        subcat = cat.substr(sep_index + 1);
        cat = cat.substr(0, sep_index);
    }
    $(".post-big-title").html(id);
    $.get('data/list.json', function(data) {
        if (!data[cat]) {
            return;
        }
        var articles = data[cat];
        if (subcat) {
            for (var i = 0; i < articles.length; i++) {
                var article = articles[i];
                if (articles[i]['title'] == subcat) {
                    articles = articles[i]['list'];
                    break;
                }
            }
            if (i == articles.length) {
                $(".articles").html('<h1 class="post-big-title">该分类暂无文章！</h1>');
                $(".pagination").hide();
                return;
            }
        }
        $(".navbar-nav li a").each(function(k, v) {
            v = $(v);
            if (v.html() === cat) {
                v.parent().addClass("active");
            }
        });
        var item;
        for (var i = 0; i < articles.length; i++) {
            if (articles[i]['title'] == id) {
                item = articles[i];
            }
        }
        if (item) {
            var author = item['author'];
            var time = item['time'];
            var cover_url = item['cover_url'];
            $(".post-poster").html('<img src="' + cover_url + '">');
            var icon = iconFromCategory(cat);
            var content = '<a class="category" href="category.html?cat=' + cat + '"><span class="glyphicon ' + icon + '"></span>' + cat + '</a>';
            if (subcat) {
                content += ' / <a class="category" href="category.html?cat=' + cat + (subcat? "/" + subcat : "") + '">' + subcat + '</a>';
            }
            content += ' | <span id="author" class="author">' + author + '</span> • ' + time;
            $(".post-author").html(content);
        }
    });
    $.get('data/' + cat + (subcat? "/" + subcat: "") + '/' + id + '.md', function(data) {
        $('#preview').html(marked(data));
        $('#preview code.highlight').each(function(i, block) {
            hljs.highlightBlock(block);
        });
    });
});