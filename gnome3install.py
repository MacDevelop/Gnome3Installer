from os import system
system('add-apt-repository ppa:gnome3-team/gnome3')
system('apt-get update')
system('apt-get install gnome-session&&apt-get install gnome-shell')
print('gnome instalado com sucesso !')
print('Para utilizar o gnome execute (gnome-shell --replace) :D')