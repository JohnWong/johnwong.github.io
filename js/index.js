$(document).ready(function() {
    $.get("data/list.json", function(data) {
        
    });
    window.Page = {
        pageSize: 10,
        pageCount: 0,
        currentPage: 0,
        init: function(){
            var page_size = 4;
            var count = articles.length;
            var pagination = $("#pagination");
            if (count === 0){
                pagination.hide();
                return;
            }
            Page.pageCount = Math.floor((count + Page.pageSize - 1) / Page.pageSize);
            $("#pagination li:first-child").click(Page.goPrev);
            $("#pagination li:last-child").click(Page.goNext);
            for (var i = Page.pageCount; i > 0; i--) {
                var content = $('<li><a href="#" onclick="Page.goPage(' + i + ')">' + i + '</a></li>');
                content.insertAfter("#pagination li:nth-child(1)");
            }
            Page.goPage(1);
        },
        goNext: function(evt){
            evt.preventDefault();
            if (Page.currentPage + 1 <= Page.pageCount) {
                Page.goPage(Page.currentPage + 1);
            }
        },
        goPrev: function(evt){
            evt.preventDefault();
            if (Page.currentPage - 1 > 0) {
                Page.goPage(Page.currentPage - 1);
            }
        },
        goPage: function(num) {
            var start = (num - 1) * Page.pageSize;
            var to = num * Page.pageSize;
            var template = $("#article-template").text();
            var content = '';
            var sub_articles = articles.slice(start, to);
            for (var i in sub_articles) {
                var article = sub_articles[i];
                content += template.replace(/@{article-author}/g, article.author)
                    .replace(/@{article-time}/g, article.time)
                    .replace(/@{article-link}/g, "link") //todo
                    .replace(/@{article-title}/g, article.title)
                    .replace(/@{article-description}/g, article.description)
                    .replace(/@{article-thumb}/g, article.thumb_url);
            }
            $(".articles").html(content);
            Page.currentPage = num;
            var pagination = $("#pagination");
            if (num === 1) {
                pagination.find("li:first-child").addClass("disabled");
            } else {
                pagination.find("li:first-child").removeClass("disabled");
            }
            if (num === Page.pageCount) {
                pagination.find("li:last-child").addClass("disabled");
            } else {
                pagination.find("li:last-child").removeClass("disabled");
            }
            pagination.find(".active").removeClass("active");
            pagination.find("li:nth-child(" + (num + 1) + ")").addClass("active");
        }
    };
});