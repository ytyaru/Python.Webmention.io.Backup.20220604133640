
#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# HTTPローカルサーバを起動する
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"
	pip3 freeze | grep 'requests==' > requirements.txt
	#pip3 install -r requirements.txt
}
Run "$@"
