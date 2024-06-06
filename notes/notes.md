### 6/6/24
1. Can access distro with:
     wsl -d \<distro name\>
   Instead of:
     wsl --distribution \<distro name\>
2. Tab works to autofill in all cmd ln terminals
3. To end running of wsl distro enter:
     wsl --terminate \<distro name\>
4. Wsl settings, such as the default launch profile, can be accessed from any dir with:
     sudo nano /etc/wsl.conf
   This will open the file, and to change/create the default launch user, write:
     ...\<preexisting code\>...

     \[user\]
     default=\<username\>

   ...Ad Can..., the blank lines might be meakev, so write them
5.
