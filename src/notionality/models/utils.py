import enum


# TODO: Rewrite these in the API order. Also double check they're up to date
class FullColor(enum.StrEnum):
    DEFAULT = 'default'
    GRAY = 'gray'
    BROWN = 'brown'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    PURPLE = 'purple'
    PINK = 'pink'
    RED = 'red'

    GRAY_BACKGROUND = 'gray_background'
    BROWN_BACKGROUND = 'brown_background'
    ORANGE_BACKGROUND = 'orange_background'
    YELLOW_BACKGROUND = 'yellow_background'
    GREEN_BACKGROUND = 'green_background'
    BLUE_BACKGROUND = 'blue_background'
    PURPLE_BACKGROUND = 'purple_background'
    PINK_BACKGROUND = 'pink_background'
    RED_BACKGROUND = 'red_background'


class CodingLanguage(enum.StrEnum):
    ABAP = 'abap'
    ARDUINO = 'arduino'
    BASH = 'bash'
    BASIC = 'basic'
    C = 'c'
    CLOJURE = 'clojure'
    COFFEESCRIPT = 'coffeescript'
    CPP = 'c++'
    CSHARP = 'c#'
    CSS = 'css'
    DART = 'dart'
    DIFF = 'diff'
    DOCKER = 'docker'
    ELIXIR = 'elixir'
    ELM = 'elm'
    ERLANG = 'erlang'
    FLOW = 'flow'
    FORTRAN = 'fortran'
    FSHARP = 'f#'
    GHERKIN = 'gherkin'
    GLSL = 'glsl'
    GO = 'go'
    GRAPHQL = 'graphql'
    GROOVY = 'groovy'
    HASKELL = 'haskell'
    HTML = 'html'
    JAVA = 'java'
    JAVASCRIPT = 'javascript'
    JSON = 'json'
    JULIA = 'julia'
    KOTLIN = 'kotlin'
    LATEX = 'latex'
    LESS = 'less'
    LISP = 'lisp'
    LIVESCRIPT = 'livescript'
    LUA = 'lua'
    MAKEFILE = 'makefile'
    MARKDOWN = 'markdown'
    MARKUP = 'markup'
    MATLAB = 'matlab'
    MERMAID = 'mermaid'
    NIX = 'nix'
    OBJECTIVE_C = 'objective-c'
    OCAML = 'ocaml'
    PASCAL = 'pascal'
    PERL = 'perl'
    PHP = 'php'
    PLAIN_TEXT = 'plain text'
    POWERSHELL = 'powershell'
    PROLOG = 'prolog'
    PROTOBUF = 'protobuf'
    PYTHON = 'python'
    R = 'r'
    REASON = 'reason'
    RUBY = 'ruby'
    RUST = 'rust'
    SASS = 'sass'
    SCALA = 'scala'
    SCHEME = 'scheme'
    SCSS = 'scss'
    SHELL = 'shell'
    SQL = 'sql'
    SWIFT = 'swift'
    TOML = 'toml'
    TYPESCRIPT = 'typescript'
    VB_NET = 'vb.net'
    VERILOG = 'verilog'
    VHDL = 'vhdl'
    VISUAL_BASIC = 'visual basic'
    WEBASSEMBLY = 'webassembly'
    XML = 'xml'
    YAML = 'yaml'
    MISC = 'java/c/c++/c#'
