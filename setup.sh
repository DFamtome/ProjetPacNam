echo Installation de vscode et des extentions

nix-shell -p "vscode"
nix profile install nixpkgs#vscode-extensions.ms-python.python

echo Installation de pygame
nix profile install nixpkgs#python311Packages.pygame

nix-shell -p "python3.withPackages (ps: [ ps.pygame ])"

rm ~/.cache/dmenu_run
