echo Installation de pygame et de vscode
nix-shell -p "python311Packages.pygame vscode vscode-extensions.ms-python.python (ps: [ ps.pygame ])"

rm ~/.cache/dmenu_run
