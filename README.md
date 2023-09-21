# Quarto template for the _Journal of Fish and Wildlife Management_

#### Authors:          Richard A. Erickson, Althea A. Archer, Michael N. Fienen
#### Point of contact: Richard A. Erickson (rerickson@usgs.gov)
#### Repository Type:  Quarto template
#### Year of Origin:   2023 (original publication)
#### Year of Version:  2023
#### Version:          1.0.0 
#### Digital Object Identifier (DOI): https://doi.org/10.5066/P9FPFKKS
#### USGS Information Product Data System (IPDS) no.: IP-XXXX

***

_Suggested Citation:_

Erickson, R.A., Peterman L.L, 2023,
Quarto template for the _Journal of Fish and Wildlife Management_
U.S. Geological Survey software release. Reston, Va.,
https://doi.org/10.5066/XXXXXX.

_Authors' [ORCID](https://orcid.org) nos.:_

- Richard A. Erickson, [0000-0003-4649-482X](https://orcid.org/0000-0003-4649-482X)
- Althea A. Archer, [0000-0003-1927-0783](https://orcid.org/0000-0003-1927-0783)
- Michael N. Fienen, [0000-0002-7756-4651](https://orcid.org/0000-0002-7756-4651)

***
***

This repository contains a journal template for the [_Journal of Fish and Wildlife Management_][jfwm].
The template uses [Quarto][quarto], a Markdown-based "open-source scientific and technical publishing system."
The template uses an MS Word file as a template to format a manuscript for the _Journal of Fish and Wildlife Management_.
Users will want to edit the `qmd` file and the `bib` file if they adapt this template for their own manuscripts.

# Repository Files

This repository contains a Quarto-based template for the _Journal of Fish and Wildlife Management_.
To support this, the following files are located here:

- `README.md` is this file.
- `LICENSE.md` is the Official USGS License. 
- `code.json` is the code metadata.
- `CONTRIBUTING.md` describes how to contribute to this project.
- `DISCLAIMER.md` is the standard USGS disclaimer.
- `.gitignore` is a file telling git which files to not track.
- `council-of-science-editors-author-date.csl` is a the reference citation style file.
- `jfwm_template_raw.docx` is the compiled outputs from the Quarto file.
- `jfwm_template_raw.qmd` is the the Quarto file for the template. _Users will want to edits this file_.
- `quarto.png` is a figure for the manuscript.
- `references.bib` is the reference file. _Users will want to edits this file_.
- `updated_refs.py` is a Python script that updates the references based upon DOIs.

# Background knowledge

This template assumes the user knows, or at least wants to learn, how to use Markdown-based text programs such as Quarto.
Knowing basic Markdown commands will help.
Additionally, knowing LaTeX will assist in helping to write equations and do advanced formatting.
A domain specific language such as Python or R are necessary to include your own code.
Additionally, Python is required to use the option tools to convert DOI in text to be entires a a `bib` file.

# Acknowledgments

We thank the U.S. Geological Survey Biological Threats and Invasive Species Research Program and U.S. Geological Survey Water Mission Area Integrated Information Dissemination Division for funding.
Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.
The findings and opinions expressed in this manuscript are those of the authors and do not necessarily represent the views of the US Fish and Wildlife Service.

[quarto]: https://quarto.org/

[jfwm]: https://meridian.allenpress.com/jfwm/
