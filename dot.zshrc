# oh-my-zsh config ******************************************

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="simple"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled	# disable automatic updates
# zstyle ':omz:update' mode auto			# update automatically without asking
zstyle ':omz:update' mode reminder	# just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 13

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration
# ******************************************

# Set nvim as default editor
export EDITOR=nvim
export VISUAL=nvim;

# My paths
# ******************************************
export PATH="/home/luis/.cargo/bin:$PATH"
export PATH="/home/luis/.local/share/bob/nvim-bin:$PATH"
export PATH="/home/luis/.local/kitty.app/bin:$PATH"
export PATH="/var/lib/flatpak/exports/bin:$PATH"

# My aliases
# ******************************************
alias hi="echo \"Hello! I'm $(hostname).\nHere's my IP: $(hostname -I | awk '{print $1}')\""
alias home="clear && cd ~"
alias open="xdg-open"
alias phone="scrcpy --turn-screen-off --window-borderless"
alias py="python"

# Prevent accidental removal
alias rm="rm -i"

# Flatpak aliases
alias vscode="flatpak run com.visualstudio.code"
