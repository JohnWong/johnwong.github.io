require 'html-proofer'

task :test do
    sh "bundle exec jekyll build"
    HTMLProofer.check_directory("./_site", {
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