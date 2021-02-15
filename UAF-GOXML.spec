# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src\\wsgi.py'],
             pathex=['C:\\Users\\Maxly Garcia\\Desktop\\UAF-GoXML'],
             binaries=[],
             datas=[('src\\data\\*', 'data'), ('src\\data\\*.xlsx', 'data'), ('src\\data\\*.xml', 'data')],
             hiddenimports=['waitress'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='UAF-GOXML',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
