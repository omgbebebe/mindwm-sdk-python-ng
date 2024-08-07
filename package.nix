{ lib
, pkgs
, my_python
#, parliament
#, mindwm-sdk-python
}:
with pkgs;

python3.pkgs.buildPythonApplication {
  pname = "mindwm-knfunc";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = [ my_python ];
#  buildInputs = [ my_python ];
#  dependencies = [
#    parliament
#    mindwm-sdk-python
#  ];

  pythonImportsCheck = [
    "mindwm.model"
    "mindwm.model.events"
    "mindwm.model.graph"
  ];
  format = "pyproject";
  nativeBuildInputs = with python3.pkgs; [ setuptools ];
}
