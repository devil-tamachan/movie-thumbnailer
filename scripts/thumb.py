import glob, os
scantypes = ('*.ts', '*.mp4', '*.mpg')
flists = []
for scantype in scantypes:
  flists.extend(glob.glob(scantype))

def isNeedUpdate(file, thumbpath):
  if not os.path.isfile(thumbpath):
    return True
  if os.stat(file).st_mtime > os.stat(thumbpath).st_mtime:
    return True
  return False

def GenThumbnail(file, col, row):
  os.system('C:\\Projects\\mtn\\Release\\mtn.exe -z -P -c '+str(col)+' -r '+str(row)+' "'+file+'"')

for file in flists:
    thumbpath = os.path.splitext(file)[0]+'_s.jpg'
    #print(thumbpath)
    if isNeedUpdate(file, thumbpath):
      #print(file)
      for n in range(5, 0, -1):
        GenThumbnail(file, n, n)
        if os.path.isfile(thumbpath):
          break
