let
  pkgs = import <nixpkgs> {};
in
  with pkgs;
  stdenv.mkDerivation {
    name = "nodejs_shell";
    buildInputs = [
      pkgs.nodejs
    ];
  }

