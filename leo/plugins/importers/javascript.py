#@+leo-ver=5-thin
#@+node:ekr.20140723122936.18144: * @file importers/javascript.py
'''The @auto importer for JavaScript.'''
import re
import leo.core.leoGlobals as g
import leo.plugins.importers.linescanner as linescanner
Importer = linescanner.Importer
#@+others
#@+node:ekr.20140723122936.18049: ** class JS_Importer
class JS_Importer(Importer):

    def __init__(self, importCommands, language=None, alternate_language=None):
        '''The ctor for the JS_ImportController class.'''
        # Init the base class.
        Importer.__init__(self,
            importCommands,
            gen_refs = True,
            language = 'javascript',
            state_class = JS_ScanState,
        )

    #@+others
    #@+node:ekr.20161105140842.5: *3* js_i.scan_line & helpers
    #@@nobeautify

    op_table = [
        # Longest first in each line.
        # '>>>', '>>>=',
        # '<<<', '<<<=',
        # '>>=',  '<<=',
        '>>', '>=', '>',
        '<<', '<=', '<',
        '++', '+=', '+',
        '--', '-=', '-',
              '*=', '*',
              '/=', '/',
              '%=', '%',
        '&&', '&=', '&',
        '||', '|=', '|',
                    '~',
                    '=',
                    '!', # Unary op can trigger regex.
    ]
    op_string = '|'.join([re.escape(z) for z in op_table])
    op_pattern = re.compile(op_string)

    def scan_line(self, s, prev_state):
        '''
        Update the scan state at the *end* of the line by scanning all of s.

        Distinguishing the the start of a regex from a div operator is tricky:
        http://stackoverflow.com/questions/4726295/
        http://stackoverflow.com/questions/5519596/
        (, [, {, ;, and binops can only be followed by a regexp.
        ), ], }, ids, strings and numbers can only be followed by a div operator.
        '''
        trace = False # and not g.unitTesting
        trace_ch = True
        context = prev_state.context
        curlies, parens = prev_state.curlies, prev_state.parens
        expect = None # (None, 'regex', 'div')
        i = 0
        # Special case for the start of a *file*
        # if not context:
            # i = g.skip_ws(s, i)
            # m = self.start_pattern.match(s, i)
            # if m:
                # i += len(m.group(0))
                # if g.match(s, i, '/'):
                    # i = self.skip_regex(s, i)
        while i < len(s):
            assert expect is None, expect
            progress = i
            ch, s2 = s[i], s[i:i+2]
            if trace and trace_ch: g.trace(repr(ch)) #, repr(s2))
            if context == '/*':
                if s2 == '*/':
                    i += 2
                    context = ''
                    expect = 'div'
                else:
                    i += 1 # Eat the next comment char.
            elif context:
                assert context in ('"', "'"), repr(context)
                if ch == '\\':
                    i += 2
                elif context == ch:
                    i += 1
                    context = '' # End the string.
                    expect = 'regex'
                else:
                    i += 1 # Eat the string character.
            elif s2 == '//':
                break # The single-line comment ends the line.
            elif s2 == '/*':
                # Start a comment.
                i += 2
                context = '/*'
            elif ch in ('"', "'"):
                # Start a string.
                i += 1
                context = ch
            elif ch in '_$' or ch.isalpha():
                # An identifier. Only *approximately* correct.
                # http://stackoverflow.com/questions/1661197/
                i += 1
                while i < len(s) and (s[i] in '_$' or s[i].isalnum()):
                    i += 1
                expect = 'div'
            elif ch.isdigit():
                i += 1
                # Only *approximately* correct.
                while i < len(s) and (s[i] in '.+-e' or s[i].isdigit()):
                    i += 1
                # This should work even if the scan ends with '+' or '-'
                expect = 'div'
            elif ch in '?:':
                i += 1
                expect = 'regex'
            elif ch in ';,':
                i += 1
                expect = 'regex'
            elif ch == '\\':
                i += 2
            elif ch == '{':
                i += 1
                curlies += 1
                expect = 'regex'
            elif ch == '}':
                i += 1
                curlies -= 1
                expect = 'div'
            elif ch == '(':
                i += 1
                parens += 1
                expect = 'regex'
            elif ch == ')':
                i += 1
                parens -= 1
                expect = 'div'
            elif ch == '[':
                i += 1
                expect = 'regex'
            elif ch == ']':
                i += 1
                expect = 'div'
            else:
                m = self.op_pattern.match(s, i)
                if m:
                    if trace: g.trace('OP', m.group(0))
                    i += len(m.group(0))
                    expect = 'regex'
                elif ch == '/':
                    g.trace('no lookahead for "/"', repr(s))
                    assert False, i
                else:
                    i += 1
                    expect = None
            # Look for a '/' in the expected context.
            if expect:
                assert not context, repr(context)
                i = g.skip_ws(s, i)
                # Careful // is the comment operator.
                if g.match(s, i, '//'):
                    break
                elif g.match(s, i, '/'):
                    if expect == 'div':
                        i += 1
                    else:
                        assert expect == 'regex', repr(expect)
                        i = self.skip_regex(s,i)
            expect = None
            assert progress < i
        d = {'context':context, 'curlies':curlies, 'parens':parens}
        state = JS_ScanState(d)
        if trace: g.trace(state)
        return state
    #@+node:ekr.20161011045426.1: *4* js_i.skip_regex
    def skip_regex(self, s, i):
        '''Skip an *actual* regex /'''
        trace = False # and not g.unitTesting
        trace_ch = True
        if trace: g.trace('ENTRY', i, repr(s[i:]))
        assert s[i] == '/', (i, repr(s))
        i1 = i
        i += 1
        while i < len(s):
            progress = i
            ch = s[i]
            if trace and trace_ch: g.trace(repr(ch))
            if ch == '\\':
                i += 2
            elif ch == '/':
                i += 1
                if i < len(s) and s[i] in 'igm':
                    i += 1 # Skip modifier.
                if trace: g.trace('FOUND', i, s[i1:i])
                return i
            else:
                i += 1
            assert progress < i
        return i1 # Don't skip ahead.
    #@+node:ekr.20161101183354.1: *3* js_i.clean_headline
    def clean_headline(self, s):
        '''Return a cleaned up headline s.'''
        s = s.strip()
        # Don't clean a headline twice.
        if s.endswith('>>') and s.startswith('<<'):
            return s
        elif 1:
            # Imo, showing the whole line is better than truncating it.
            # However the lines must have a reasonable length.
            return g.truncate(s, 100)
        else:
            i = s.find('(')
            if i > -1:
                s = s[:i]
            return g.truncate(s, 100)
    #@-others
#@+node:ekr.20161105092745.1: ** class JS_ScanState
class JS_ScanState:
    '''A class representing the state of the javascript line-oriented scan.'''

    def __init__(self, d=None):
        '''JS_ScanState ctor'''
        if d:
            # d is *different* from the dict created by i.scan_line.
            self.context = d.get('context')
            self.curlies = d.get('curlies')
            self.parens = d.get('parens')
        else:
            self.context = ''
            self.curlies = self.parens = 0

    def __repr__(self):
        '''JS_ScanState.__repr__'''
        return 'JS_ScanState context: %r curlies: %s parens: %s' % (
            self.context, self.curlies, self.parens)

    __str__ = __repr__

    #@+others
    #@+node:ekr.20161119115505.1: *3* js_state.level
    def level(self):
        '''JS_ScanState.level.'''
        return (self.curlies, self.parens)
    #@+node:ekr.20161119051049.1: *3* js_state.update
    def update(self, data):
        '''
        Update the state using the 6-tuple returned by i.scan_line.
        Return i = data[1]
        '''
        context, i, delta_c, delta_p, delta_s, bs_nl = data
        # self.bs_nl = bs_nl
        self.context = context
        self.curlies += delta_c
        self.parens += delta_p
        # self.squares += delta_s
        return i

    #@-others

#@-others
importer_dict = {
    'class': JS_Importer,
    'extensions': ['.js',],
}
#@@language python
#@@tabwidth -4
#@-leo
