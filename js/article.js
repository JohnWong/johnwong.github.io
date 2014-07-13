$(document).ready(function() {
    var params = function() {
        for (var t, e = [], o = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&"), r = 0; r < o.length; r++)
            t = o[r].split("="), e.push(t[0]), e[t[0]] = t[1];
        return e;
    }();
    var cat = params['cat'], id = params['id'];
    if (!cat || !id) {
        $(".post-big-title").html('未找到该文章');
        return;
    };
    id = decodeURI(id), cat = decodeURI(cat);
    $(".post-big-title").html(id);
    $.get('data/list.json', function(data) {
        if (data[cat] && data[cat][id]) {
            var item = data[cat][id];
            var author = item['author'];
            var time = item['time'];
            var cover_url = item['cover_url'];
            $(".post-poster").html('<img src="' + cover_url + '" alt="' + id + '">');
            var icon;
            switch (params['cat']) {
                case "Mobile":
                    icon = 'glyphicon-phone';
                    break;
                case "Life":
                    icon = 'glyphicon-home';
                    break;
                    // case "Bookmarks": icon = 'glyphicon-bookmark'; break;
                case "Travel":
                    icon = 'glyphicon-road';
                    break;
                    // case "White Hat": icon = 'glyphicon-lock';break;
                case "Front End":
                    icon = 'glyphicon-link';
                    break;
            };
            var content = '<a class="category" href="cat.html?id=' + cat + '"><span class="glyphicon ' + icon + '"></span>' + params['cat'] + '</a> | <span id="author" class="author">' + author + '</span> • ' + time;
            $(".post-author").html(content);

        };
    });
    $.get('data/' + cat + '/' + id + '.md', function(data) {
        $('#preview').html(marked(data));
        $('#preview code.highlight').each(function(i, block) {
            hljs.highlightBlock(block);
        });
    });
});