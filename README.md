# xml2json

Convert XML to JSON.

This is a non-preserving shell pipe converter from XML to JSON.

- Currently written in Python3

It tries to be clever, such that you can easily post-process the XML using `jq`.

- It does not distinguish names of attributes and subtags
  - Both will be merged
- It ignores namespaces when merging names
  - The namespace is given as `@` in the object instead
  - This is usually what you want
- It converts `.` in names to `$`
  - `$` is a valid JavaScript identifier
  - allows to distinguish between `a$b` and `a.b`


## Usage

	git submodule add https://github.com/hilbix/xml2json.git
	ln -s xml2json.py bin/xml2json

Then someting like

	cat XML | bin/xml2json | jq

See [`xml2json.py`](xml2json.py) for details.


## Future

When I need it, following might be added in future:

- JSON to XML
- JavaScript/NodeJS module


## FAQ

License?

- Free as free beer, free speech and free baby.
- Covering this code with a Copyright again violates German Urheberrecht!

PyPi? NPM? Skypack?

- I refuse to support highly dangerous registries like CPAN, PyPi, NPM, Composer, Maven, Gradle, Bower, Docker etc.  (Crates?  Dunno yet.)
  - Registries like those always look for me like the idea to light christmas tree candles with a military grade flamethrower on full power.
  - Those registries lack globally trusted well known signatures which are verified.  Like in Debian.
  - Or some hole-free blockchains which protect against cheating history.  Like in `git` (accompanied with not-so-well-known dev sigs).
  - And it must be extremely hard to impossible to get past verification when data was compromized.  Now.  And in 25 years.
- But as this code here is entirely free, you can publish it anywhere, of course.
- Recommendation:
  - Create a fresh new `git` repo
  - Add this as a submodule
  - Use CirrusCI or GitHub Workflows to autodrive the publish process
  - If this neatly fits away into a single file (`.cirrus.yml`) or subdirectory (`.github`), I am willing to accept a PR for this.
  - (But if you instead use some CI which I consider too dangerous to be used on GH - like TravisCI -, I probably will refuse such a patch.)
  - However, it is likely that I will neither check nor support this patch myself.

Bugs/Questions/Contrib/Patches?

- Open issue/PR on GitHUb
- Eventually I listen

