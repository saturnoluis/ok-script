# oh-my-zsh config ******************************************

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="eastwood" # set by `omz`

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled	# disable automatic updates
# zstyle ':omz:update' mode auto			# update automatically without asking
zstyle ':omz:update' mode reminder	# just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 13

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration
# ******************************************

# Setup NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"	# This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"	# This loads nvm bash_completion

# Set nvim as default editor
export EDITOR=nvim

# My functions
# ******************************************
# 
# Handy function to force git to push
function git-force-push() { # Force push with lease
	BRANCH="$(git rev-parse --abbrev-ref HEAD)"
	REMOTE="$(git remote)"
	echo "Are you sure you want to force-push to \e[33m$BRANCH\e[0m? \e[34m(y/\e[32;1mN\e[0m)"
	read REPLY
	if [[ $REPLY =~ ^[Yy]$ ]]
	then
		eval git push --force-with-lease $REMOTE $BRANCH
	fi
}

# This function opens ranger and changes the working directory
# to the current directory in ranger when you quit the program.
function ranger-cd() {
	tempfile="$(mktemp -t ranger_cd.XXXXXX)"
	ranger --choosedir="$tempfile" "${@:-$(pwd)}"
	test -f "$tempfile" &&
	if [ "$(cat -- "$tempfile")" != "$(echo -n `pwd`)" ]; then
		cd -- "$(cat "$tempfile")"
	fi
	rm -f -- "$tempfile"
}

# Create my usual tmux session to work
function tmux-work() {
	if tmux has-session -t work 2>/dev/null; then
		tmux attach-session -t work
	else
		tmux new-session -d -s work -n nvim

		tmux new-window -t work:2 -n services
		tmux split-window -h
		tmux split-window -v

		tmux select-window -t work:1
		tmux select-pane -t 0

		tmux attach-session -t work
	fi
}

# Function to list and stop all running docker containers
function docker-stop-all() {
	if command -v docker >/dev/null 2>&1; then
		container_ids=$(docker ps -q)
		if [[ -n $container_ids ]]; then
			echo "Stopping running Docker containers..."
			for container_id in $container_ids; do
				echo "> docker stop $($container_ids)"
				docker stop "$container_id"
			done
		else
			echo "No running Docker containers found."
		fi
	else
		echo "Docker is not installed."
	fi
}

# Function to export all variables declared in any given .env file
function export-env() {
  local file="$1"  # Get the file argument

  if [ ! -f "$file" ]; then
    echo "File $file does not exist."
    return 1
  fi

  export $(grep -v '^#' "$file" | xargs)
}

function list-env() {
  env | grep -E '^[a-zA-Z_][a-zA-Z0-9_]*='
}

# My paths
# ******************************************
export PATH="/home/luis/.cargo/bin:$PATH"
export PATH="/home/luis/.local/share/bob/nvim-bin:$PATH"
export PATH="/home/luis/.local/kitty.app/bin:$PATH"

# My aliases
# ******************************************
alias hi="echo \"Hello! I'm $(hostname).\nHere's my IP: $(hostname -I | awk '{print $1}')\""
alias home="clear && cd ~"
alias open="xdg-open"
alias phone="scrcpy --turn-screen-off --window-borderless"
alias py="python"
alias minecraft-server="/mnt/my_games/minecraft/oklands/run.sh"

# Flatpak aliases
alias vscode="flatpak run com.visualstudio.code"

# Prevent accidental removal
alias rm="rm -i"

# Start docker service
alias docker-start="sudo systemctl start docker"
