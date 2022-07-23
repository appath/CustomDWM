function license() {
cat <<EOF

This program is free software
You can redistribute it or modify it under the terms of the
GNU General Public License.

EOF
}

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Ruby
#if which ruby >/dev/null && which gem >/dev/null; then
#    PATH="$(ruby -rubygems -e 'puts Gem.user_dir')/bin:$PATH"
#fi

# NodeJS
#PATH="$HOME/.builds/node-v14.17.0/bin:$PATH"

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

if [[ $(id -u) -eq 0 ]];then
    PS1="./# "
else
    PS1="./$ "
fi



