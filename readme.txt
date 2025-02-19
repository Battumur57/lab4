dell@DESKTOP-3M048OE MINGW64 ~
$ mkdir lab4
mkdir: cannot create directory ‘lab4’: File exists

dell@DESKTOP-3M048OE MINGW64 ~
$ mkdir lab4

dell@DESKTOP-3M048OE MINGW64 ~
$ cd lab4

dell@DESKTOP-3M048OE MINGW64 ~/lab4
$ git init
Initialized empty Git repository in C:/Users/dell/lab4/.git/

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ touch readme.txt

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        dasgal1.py
        dasgal2.py
        readme.txt

nothing added to commit but untracked files present (use "git add" to track)

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git add dasgal1.py

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git commit -m "Ehnii dasgal"
[master (root-commit) 9eaa665] Ehnii dasgal
 1 file changed, 12 insertions(+)
 create mode 100644 dasgal1.py

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git add dasgal2.py

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git commit -m "dasgal2"
[master 8820f5c] dasgal2
 1 file changed, 22 insertions(+)
 create mode 100644 dasgal2.py

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git remote add origin https://github.com/Battumur57/lab4.git

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ git push origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1018 bytes | 1018.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Battumur57/lab4.git
 * [new branch]      master -> master

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$ code readme.txt

dell@DESKTOP-3M048OE MINGW64 ~/lab4 (master)
$
