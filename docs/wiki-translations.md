# Maintaining the wiki translations

The three version-controlled wiki families (`Home`, `Connection` and
`Troubleshooting`) contain full pages in the 24 languages listed in
[`wiki/languages.json`](../wiki/languages.json). This uses the language catalog of
the [ha-homelab organization](https://github.com/ha-homelab/.github/blob/main/languages.json).
The README and detailed hardware documents retain their existing language scope.

Start at the [wiki home](../wiki/Home.md). Every translated page links to every
language of the same page. These are ordinary files in this repository; adding
them does not publish or synchronize the separate GitHub Wiki service.

When changing English instructions, update the complete corresponding translated
pages. Preserve safety conditions, validation limits, all numbered steps, source
links and technical identifiers. Keep the additional Russian guide link in the
Russian pages. Localized page filenames use `Family-<language>.md`; English keeps
`Family.md`. Internal family links use these local filenames so they work before
any separate wiki deployment. Detailed technical references remain canonical.

Keep the language navigation between its `language-navigation` comment markers.
Each link declares `lang` and `dir`. Arabic, Persian and Hebrew prose uses an RTL
container; any future command blocks must explicitly retain LTR direction.

Run the existing documentation check from the repository root:

```sh
python3 scripts/check_docs.py
```

The check verifies all 72 pages, complete navigation, local links, required source
references, numbered steps, reference bullets and RTL markup. It cannot establish
translation accuracy or hardware acceptance: review the prose against English,
and preserve the explicit statement that physical commissioning is still pending.
