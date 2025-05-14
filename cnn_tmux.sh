#!/bin/bash

session_name="cnn_from_scratch"

# Create the new detached session
tmux new-session -d -s "$session_name"

# Send the 'cd' command to the first window (index 0)
tmux send-keys -t "$session_name:0" "cd ~/cnn_from_scratch" C-m

# Rename the first window
tmux rename-window -t "$session_name:0" "bash"

# Create the second window named "vim" and set its starting directory
tmux new-window -t "$session_name" -n "vim" -c "$HOME/cnn_from_scratch"

# Attach to the session
tmux attach-session -t "$session_name"
