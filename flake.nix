{
  description = "A MindWM SDK for Python";

  inputs = {
    #nixpkgs.url = "github:nixos/nixpkgs/24.05";
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    neontology-py.url = "github:omgbebebe/neontology.py-nix";
    neontology-py.inputs.nixpkgs.follows = "nixpkgs";
    devshell.url = "github:numtide/devshell/main";
    devshell.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ flake-parts, nixpkgs, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.devshell.flakeModule
      ];
      systems = [ "x86_64-linux" "aarch64-linux" ];
      perSystem = { config, self', inputs', pkgs, system, ... }:
      let
        my_python = pkgs.python3.withPackages (ps: with ps; [
          inputs.neontology-py.packages.${system}.default
          pydantic dateutil urllib3
          opentelemetry-sdk opentelemetry-exporter-otlp
          neo4j
          pandas
          fastapi uvicorn
          pyyaml
        ]);
        project = pkgs.callPackage ./package.nix {
          my_python = pkgs.python3;
          neontology = inputs.neontology-py.packages.${system}.default;
        };
      in { 
        packages.default = project;
        devshells.default = {
            env = [];
            devshell.startup.pypath = pkgs.lib.noDepEntry ''
              export PYTHONPATH="$PYTHONPATH:./src:./test"
            '';
            commands = [
            {
              help = "serve knfunc: serve_knfunc <type>; i.e. serve_knfunc iodocument";
              name = "serve_knfunc";
              command = ''
                func_name="$1"
                uvicorn --host 127.0.0.1 --port 8080 knfunc.$func_name:app
              '';
            }
            ];
            packages = [
              my_python
            ] ++ (with pkgs; [
            ]);
        };
      };
      flake = {
      };
    };
}
