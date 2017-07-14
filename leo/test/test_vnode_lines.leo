<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="vitalije.20170714212045.1"><vh>@settings</vh>
<v t="vitalije.20170714212122.1"><vh>@shortcuts</vh></v>
</v>
<v t="vitalije.20170714212519.1"><vh>unit tests</vh>
<v t="vitalije.20170714204148.1"><vh>@test lines property</vh></v>
<v t="vitalije.20170714211600.1"><vh>@test _sync</vh></v>
<v t="vitalije.20170714214214.1"><vh>@test hasBody</vh></v>
<v t="vitalije.20170714215056.1"><vh>@test break it</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="vitalije.20170714204148.1">lns = ('bla\n','foo\n','bar')
p1 = p.insertAsLastChild()
p1.lines = lns
try:
    assert p1.b == 'bla\nfoo\nbar', repr(p1.b)
    p1.b = 'spam'
    assert p1.lines == ('spam',), repr(p1.lines)
finally:
    p.deleteAllChildren()
</t>
<t tx="vitalije.20170714211600.1">p1 = p.insertAsLastChild()
try:
    assert p1.v._sync is None, '_sync should be None'
    lns = ('1\n', '2\n', '3\n')
    p1.lines = lns
    assert p1.v._sync is 'body', '_sync should be body'
    s = p1.b
    assert p1.v._sync is None, '_sync should be now None'
    p1.b = s
    assert p1.v._sync is None, '_sync should be still None'
    p1.lines = lns
    assert p1.v._sync is None, '_sync should be still None'
    p1.b = s + '4'
    assert p1.v._sync is 'lines', '_sync should be lines'
    lns2 = p1.lines
    assert p1.v._sync is None, '_sync should be now None'
finally:
    p.deleteAllChildren()</t>
<t tx="vitalije.20170714212045.1"></t>
<t tx="vitalije.20170714212122.1">run-all-unit-tests-locally = Alt+Key-4
run-selected-unit-tests-locally = Alt+Key-5
</t>
<t tx="vitalije.20170714212519.1"></t>
<t tx="vitalije.20170714214214.1">p1 = p.insertAsLastChild()
v = p1.v
try:
    p1.b = ' '
    p1.b = ''
    assert not v.hasBody(), 'hasBody should be False'
    assert v._sync is 'lines', '_sync [%r] should be lines'%v._sync
    p1.lines = tuple()
    assert v._sync is 'body', '_sync  [%r] should be body'%v._sync
    assert not v.hasBody(), 'should be empty'
    assert p1.b == '', 'should be empty'
    
    v.lines = ('1',)
    assert v.hasBody(), 'should not be empty'
    assert v._sync is 'body', '_sync [%r] should be body'%v._sync
    v.b = '1'
    assert v._sync is 'lines', '_sync [%r] should be lines'%v._sync
finally:
    p.deleteAllChildren()</t>
<t tx="vitalije.20170714215056.1">p1 = p.insertAsLastChild()
v = p1.v
try:
    v.b = ' '
    assert v._sync is 'lines', '_sync should be lines'
    v.lines = tuple()
    assert v.b == '', 'should be empty now'
    v.b = ' '
    v.lines = (' ',)
    v.lines = ('\n', ' ')
    v.lines = ('\n', ' ')
    assert v.b == '\n '
finally:
    p.deleteAllChildren()</t>
</tnodes>
</leo_file>
