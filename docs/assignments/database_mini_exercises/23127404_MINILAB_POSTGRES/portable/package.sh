#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"

folder_name="23127404_MINILAB_POSTGRES"
portable_root="$(pwd)"
lab_root="$(dirname "$portable_root")"
zip_path="$(dirname "$lab_root")/$folder_name.zip"
stage_dir="$(mktemp -d)"
trap 'rm -rf "$stage_dir"' EXIT

cp -R "$lab_root" "$stage_dir/$folder_name"
rm -rf "$stage_dir/$folder_name/portable/node_modules"

(cd "$stage_dir" && zip -qr "$zip_path" "$folder_name")
echo "Created $zip_path"
