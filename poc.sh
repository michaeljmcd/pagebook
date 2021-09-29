#!/bin/sh

temp_dir=$(mktemp -d)
index=0

pushd ${temp_dir}

for url in "$@"
do
  ((index=$index + 1))
  curl "${url}" -o $index-orig.html
  readabilipy -i $index-orig.html -o $index.json
  jq -r '.content | @text' $index.json > $index.html
  rm $index-orig.html
done

zip book.htmlz *.html

title=$(jq -r '.title' 1.json)
author=$(jq -r '.byline' 1.json)

ebook-convert book.htmlz book.epub  --use-auto-toc --title="${title}" --authors="${author}"
popd
mv ${temp_dir}/book.epub .
rm -rf ${temp_dir}
