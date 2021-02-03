#!/bin/bash

# script for github action - update CHANGELOG.md with generated changes
# following the "keep a changelog" format

auto_run(){
    # make back up
    cp CHANGELOG.md CHANGELOG.bak

    # get new version
    new_tag=$1
    echo "the new tag is: $new_tag"
    # get previous version
    pre_tag=$(sed -n 3p mysdk/version.py)

    # add generated contant
    sed -i "/^.*new release here/a \\n## [v$new_tag](https://github.com/leandergangso/pymysharesdk/compare/v$pre_tag...v$new_tag) - $(date + %Y-%d-%m)\\n\\n$2" CHANGELOG.md
    # Check if i can use <details> to hide som stuff away!             ^ 




    # update version
    sed -i -e "s/__version__.*/__version__ = $new_tag/" mysdk/version.py




    # # Text always on top
    # sed -n '1,9p' CHANGELOG.md > NEW_CHANGELOG.md

    # # Version title
    # echo -e "[v$1] - $(date + %Y-%d-%m)\n" >> NEW_CHANGELOG.md

    # # Add new content
    # echo "$2" >> NEW_CHANGELOG.md

    # # Add existing content
    # sed -n 

    # # Get previous tag
    # export pre_tag=$(sed '$!d' CHANGELOG.md | sed "s/.*\///")

    # # Update hyperlinks
    # sed -e "s/$pre_tag...HEAD/v$1...HEAD/" CHANGELOG.md
    # echo "[$new_tag]: https://github.com/leandergangso/pymysharesdk/compare/$pre_tag...$github.ref" >> NEW_CHANGELOG.md

    # replace old file with new
    # cp NEW_CHANGELOG.md CHANGELOG.md
}

# run script
run
