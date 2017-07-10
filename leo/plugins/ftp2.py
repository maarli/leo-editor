#@+leo-ver=5-thin
#@+node:ekr.20170710161023.1: * @file ftp2.py
'''
ftp2.py: Upload files via ftp

Original by Ivanov Dmitriy. Rewritten by EKR.
'''

#@+<< ftp2 imports >>
#@+node:ekr.20170710161023.2: ** << ftp2 imports >>
import leo.core.leoGlobals as g
import leo.core.leoPlugins as leoPlugins
from leo.core.leoQt import isQt5,QtGui,QtWidgets
# pylint: disable=no-name-in-module,no-member
QAction = QtWidgets.QAction if isQt5 else QtGui.QAction
import json
import os
from ftplib import FTP
#@-<< ftp2 imports >>
#@+others
#@+node:ekr.20170710161023.3: ** init
def init ():
    '''Return True if the plugin has loaded successfully.'''
    if g.app.gui.guiName() != "qt":
        print('ftp.py plugin not loading because gui is not Qt')
        return False
    else:
        leoPlugins.registerHandler("after-create-leo-frame", onCreate)
        g.plugin_signon(__name__)
        return True
#@+node:ekr.20170710161023.4: ** onCreate
def onCreate (tag, keys):
    c = keys.get('c')
    if c:
        # Check whether the node @data ftp exists in the file being opened.
        # If so, create a button and register.
        p = g.findTopLevelNode(c, '@data ftp')
        if p:
            pluginController(c)
#@+node:ekr.20170710161023.5: ** class pluginController
class pluginController(object):

    #@+others
    #@+node:ekr.20170710161023.6: *3* ftp2.__init
    def __init__ (self,c):
        self.c = c
        if 1:
            c.k.registerCommand('upload',shortcut=None,func=self.upload)
            script = "c.k.simulateCommand('upload')"
            g.app.gui.makeScriptButton(c,script=script,buttonText='Upload')
        else:
            ib_w = self.c.frame.iconBar.w
            action = QAction('Upload', ib_w)
            self.c.frame.iconBar.add(qaction = action, command = self.upload)
    #@+node:ekr.20170710161023.7: *3* ftp2.upload
    def upload (self,event=None):
        '''Upload files to the server.'''
        c = self.c
        ok = True
        p = g.findTopLevelNode(c, '@data ftp')
        if not p:
            return g.es('No top-level "@data ftp" node')
        g.es_print('upload started')
        try:
            files = json.loads(p.b)
        except Exception:
            g.es_exception()
            return
        # credentials - array of (name, host, pass)
        credential = files[0]
        try:
            username, host, password = credential
        except ValueError:
            g.es_print('Invalid credential', repr(credential))
            return
        try:
            ftp = FTP(host)
            g.es_print('Connected to', host)
        except Exception:
            g.es_print('Can not connect to host:', repr(host))
            g.es_exception()
            return
        try:
            ftp.login(username, password)
            g.es_print('Logged in as', username)
        except Exception:
            g.es_print('Loggin failed for:', repr(username))
            g.es_exception()
            return
        # upload all the modified files
        for i, file_ in enumerate(files[1:]):
            if isinstance(file_, list):
                fn = file_[0]
                if len(file_) == 0:
                    g.es_print('Empty filespec')
                    continue
                if len(file_) == 1:
                    file_.append(1)
                t1 = file_[1]
            else:
                g.es_print('file spec must be a list:', repr(file_))
                continue
            if not g.os_path_exists(fn):
                g.es_print('Does not exit:', fn)
                ok = False
                continue
            time = os.path.getmtime(fn)
            if time == t1:
                g.es_print('Time matches. Not uploaded:', time, fn)
                ok = False
                continue
            try:
                fn2 = g.os_path_basename(fn)
                with open(fn,"rb") as f:
                    ftp.storbinary('STOR ' + fn2, f)
                file_[1] = time
                    # Don't set this until all is well.
                g.es_print('Uploaded', fn2)
            except Exception:
                g.es_print('Exception uploading', fn)
                g.es_exception()
                ok = False
        try:
            ftp.quit()
        except Exception:
            g.es_print('Exception quitting', ftp)
            g.es_exception()
            return
        if ok:
            # p.b = json.dumps(files)
            g.es_print("Upload complete")
    #@-others
#@-others
#@@language python
#@@tabwidth -4
#@-leo
