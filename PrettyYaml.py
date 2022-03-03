import sublime
import sublime_plugin
import decimal
try:
    from . import yaml
    from . import yamlloader
    Loader = yamlloader.ordereddict.CSafeLoader
    Dumper = yamlloader.ordereddict.CSafeDumper
except (ImportError, ValueError):
    import yaml
    Loader = yaml.Loader
    Dumper = yaml.Dumper

s = sublime.load_settings("Pretty YAML.sublime-settings")

class PrettyyamlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """ Pretty print YAML """
        regions = self.view.sel()
        for region in regions:

            selected_entire_file = False
            if region.empty() and len(regions) > 1:
                continue
            elif region.empty() and s.get("use_entire_file_if_no_selection", True):
                selection = sublime.Region(0, self.view.size())
                selected_entire_file = True
            else:
                selection = region

            try:
                obj = list(yaml.load_all(self.view.substr(selection), Loader=Loader))
                print(obj)
                dumper_args = s.get("dumper_args") or {}
                self.view.replace(edit, selection, yaml.dump_all(obj, Dumper=Dumper, **dumper_args))

                if selected_entire_file:
                    self.change_syntax()

            except Exception:
                import sys
                exc = sys.exc_info()[1]
                sublime.status_message(str(exc))

    def change_syntax(self):        
        if "Plain text" in self.view.settings().get('syntax'):
            self.view.set_syntax_file("Packages/YAML/YAML.tmLanguage")


def plugin_loaded():
    global s
    s = sublime.load_settings("Pretty YAML.sublime-settings")
