# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'password.png', '.' )
         ]
a = Analysis(['PyCred.py'],
             pathex=['C:\\Users\\hendersona\\Dropbox\\Public\\PYTHON\\Scripts\\Test\\Py-Cred'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PyCred',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')