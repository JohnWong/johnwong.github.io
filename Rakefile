require 'html-proofer'

task :test do
    sh "bundle exec jekyll build"
    HTMLProofer.check_directory("./_site", {
        :url_ignore => [
            /archive.org/,
            /developer.limneos.net/,
            /formalfriday.club/,
            /riddle.arthurluk.net/,
            /thirdcog.eu/,
            /www.ui.cn/
        ],
        :http_status_ignore => [521],
        :check_html => true,
        :typhoeus => { 
            :timeout => 60
        },
        :cache => { 
            :timeframe => '30d' 
        },
        :log_level => :debug
    }).run
end