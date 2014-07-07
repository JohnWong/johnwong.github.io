[![NPM version](https://badge.fury.io/js/markdown.png)](http://badge.fury.io/js/markdown)
[![Build Status](https://secure.travis-ci.org/evilstreak/markdown-js.png)](https://travis-ci.org/evilstreak/markdown-js)
[![Dependency Status](https://gemnasium.com/evilstreak/markdown-js.png)](https://gemnasium.com/evilstreak/markdown-js)

# markdown-js

Yet another Markdown parser, this time for JavaScript. There's a few
options that precede this project but they all treat Markdown to HTML
conversion as a single step process. You pass Markdown in and get HTML
out, end of story. We had some pretty particular views on how the
process should actually look, which include:

  * Producing well-formed HTML. This means that `em` and `strong` nesting
    is important, as is the ability to output as both HTML and XHTML
  * Having an intermediate representation to allow processing of parsed
    data (we in fact have two, both [JsonML]: a markdown tree and an HTML tree)
  * Being easily extensible to add new dialects without having to
    rewrite the entire parsing mechanics
  * Having a good test suite. The only test suites we could find tested
    massive blocks of input, and passing depended on outputting the HTML
    with exactly the same whitespace as the original implementation

[JsonML]: http://jsonml.org/ "JSON Markup Language"

## Installation

Just the `markdown` library:

    npm install markdown

Optionally, install `md2html` into your path

    npm install -g markdown

### In the browser

If you want to use from the browser go to the [releases] page on GitHub and
download the version you want (minified or not).

[releases]: https://github.com/evilstreak/markdown-js/releases

## Usage

### Node

The simple way to use it with Node is:

```js
var markdown = require( "markdown" ).markdown;
console.log( markdown.toHTML( "Hello *World*!" ) );
```

### Browser

It also works in a browser; here is a complete example:

```html
<!DOCTYPE html>
<html>
  <body>
    <textarea id="text-input" oninput="this.editor.update()"
              rows="6" cols="60">Type **Markdown** here.</textarea>
    <div id="preview"> </div>
    <script src="lib/markdown.js"></script>
    <script>
      function Editor(input, preview) {
        this.update = function () {
          preview.innerHTML = markdown.toHTML(input.value);
        };
        input.editor = this;
        this.update();
      }
      var $ = function (id) { return document.getElementById(id); };
      new Editor($("text-input"), $("preview"));
    </script>
  </body>
</html>
```

### Command Line

Assuming you've installed the `md2html` script (see Installation,
above), you can convert Markdown to HTML:

```bash
# read from a file
md2html /path/to/doc.md > /path/to/doc.html

# or from stdin
echo 'Hello *World*!' | md2html
```

### More Options

If you want more control check out the documentation in
[the .js files under src/][src_folder] which details all the methods and parameters
available (including examples!). One day we'll get the docs generated
and hosted somewhere for nicer browsing.

[src_folder]: https://github.com/evilstreak/markdown-js/blob/master/src

Meanwhile, here's an example of using the multi-step processing to
make wiki-style linking work by filling in missing link references:

```js
var md = require( "markdown" ).markdown,
    text = "[Markdown] is a simple text-based [markup language]\n" +
           "created by [John Gruber]\n\n" +
           "[John Gruber]: http://daringfireball.net";

// parse the markdown into a tree and grab the link references
var tree = md.parse( text ),
    refs = tree[ 1 ].references;

// iterate through the tree finding link references
( function find_link_refs( jsonml ) {
  if ( jsonml[ 0 ] === "link_ref" ) {
    var ref = jsonml[ 1 ].ref;

    // if there's no reference, define a wiki link
    if ( !refs[ ref ] ) {
      refs[ ref ] = {
        href: "http://en.wikipedia.org/wiki/" + ref.replace(/\s+/, "_" )
      };
    }
  }
  else if ( Array.isArray( jsonml[ 1 ] ) ) {
    jsonml[ 1 ].forEach( find_link_refs );
  }
  else if ( Array.isArray( jsonml[ 2 ] ) ) {
    jsonml[ 2 ].forEach( find_link_refs );
  }
} )( tree );

// convert the tree into html
var html = md.renderJsonML( md.toHTMLTree( tree ) );
console.log( html );
```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
