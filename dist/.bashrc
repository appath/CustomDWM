function about() {
cat <<EOF

This program is free software
You can redistribute it or modify it under the terms of the
GNU General Public License.

EOF
}

# 
[ -z "$PS1" ] && return

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Ruby
#if which ruby >/dev/null && which gem >/dev/null; then
#    PATH="$(ruby -rubygems -e 'puts Gem.user_dir')/bin:$PATH"
#fi

# NodeJS
#PATH="$HOME/.builds/node-v14.16.0/bin:$PATH"

alias ls='ls --color=auto'
alias cls='printf "\033c"'
alias dir='dir --color=auto'
alias grep='grep --colour=auto'

export LANG='en_US.UTF-8'
export HISTSIZE=10000
export HISTCONTROL=ignoreboth:erasedups
export VISUAL='vim'
export EDITOR='$VISUAL'
export HISTTIMEFORMAT='%d/%m/%Y %H:%M'
export HISTIGNORE='ls:ps:history*'

PROMPT_COMMAND='history -a'
HISTCONTROL=ignoredups:ignorespace
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000

if [ "$TERM" = "linux" ]; then
     echo -en "\e]P00a0f0d" #black
     echo -en "\e]P8567366" #darkgrey
     echo -en "\e]P1134f4b" #darkred
     echo -en "\e]P9134f4b" #red
     echo -en "\e]P2fcfefe" #darkgreen
     echo -en "\e]PAfcfefe" #green
     echo -en "\e]P37ea298" #brown
     echo -en "\e]PB7ea298" #yellow
     echo -en "\e]P41E7D77" #darkblue
     echo -en "\e]PC626E68" #blue
     echo -en "\e]P5134f4b" #darkmagenta
     echo -en "\e]PD1D7872" #magenta
     echo -en "\e]P61db5a2" #darkcyan
     echo -en "\e]PE1db5a2" #cyan
     echo -en "\e]P7d0d1d2" #lightgrey
     echo -en "\e]PFd0d1d2" #white
     clear #for background artifacting
fi

if [[ $(id -u) -eq 0 ]];then
    PS1="./# "
else
    PS1="./$ "
fi
