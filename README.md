Pretty YAML
===========

Prettify YAML plugin for Sublime Text 2 & 3 (Based on [Pretty
JSON](<https://github.com/dzhibas/SublimePrettyJson>))

This fork uses [yamlloader](https://github.com/Phynix/yamlloader) to preserve order of keys in YAML document.
Additionally multi-document YAML can be prettyfied.
It does however enforce linebreaks and collapses multiline strings - this will likely only by fixable
by using other yaml implementation, like ruamel.

Installation 
-------------

Install this sublime text package via [Package
Control](<http://wbond.net/sublime_packages/package_control>)



Usage To prettify YAML, make selection of YAML and press keys:
--------------------------------------------------------------

-   Linux: <kbd>ctrl+alt+y</kbd>

-   Windows: <kbd>ctrl+alt+y</kbd>

-   OS X: <kbd>cmd+ctrl+y</kbd>

If selection is empty and configuration entry
**use_entire_file_if_no_selection** is true, tries to prettify whole file.

If YAML is not valid it will be displayed in status bar of sublime.



Default configuration
---------------------

This plugin uses PyYAML to process YAML files. You can specify the arguments for
the [Dumper](<http://pyyaml.org/wiki/PyYAMLDocumentation#Dumper>) in the
plugin's preferences.



Thanks
------

-   @dzhibas https://github.com/dzhibas/



License
-------

-   View LICENSE files in plugin root and yaml/ subfolders (both MIT)
